import os
import re
import json
import asyncio
from playwright.async_api import async_playwright

output_dir = "/Users/applesupport/Desktop/linail beauty/reklam_calisma_defteri_20_kasim"
os.makedirs(output_dir, exist_ok=True)

async def scrape():
    url = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=TR&q=ipek%20kirpik&search_type=keyword_unordered&media_type=all"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1400, "height": 950},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        print("Connecting to Meta Ad Library...")
        await page.goto(url, wait_until="domcontentloaded", timeout=25000)
        await page.wait_for_timeout(4000)

        # Scroll down multiple times to load real competitor ads
        print("Scrolling down to load competitor ads...")
        for i in range(12):
            await page.mouse.wheel(0, 1800)
            await page.wait_for_timeout(1200)

        # Get full page inner text
        full_text = await page.evaluate("() => document.body.innerText")
        print(f"Captured page text: {len(full_text)} characters")

        # Parse with Python regex
        chunks = re.split(r'Kütüphane Kodu:\s*(\d+)', full_text)
        print(f"Detected {len(chunks)//2} ad blocks")

        ads_data = []
        for i in range(1, len(chunks), 2):
            lib_id = chunks[i].strip()
            content = chunks[i+1] if (i+1) < len(chunks) else ""

            # Extract start date
            date_match = re.search(r'(\d+\s+[A-Za-zğüşıöçĞÜŞİÖÇ]+\s+\d{4})\s+tarihinde yayınlanmaya başladı', content)
            start_date = date_match.group(1) if date_match else "Bilinmiyor"

            # Extract sponsor page
            sponsor_match = re.search(r'Reklam Detaylarını Gör\s*\n\s*([^\n]+)\s*\n\s*Sponsorlu', content)
            page_name = sponsor_match.group(1).strip() if sponsor_match else "Bilinmiyor"

            # Extract text after 'Sponsorlu'
            caption = ""
            if "Sponsorlu" in content:
                parts = content.split("Sponsorlu", 1)
                after = parts[1].strip()
                lines = [l.strip() for l in after.split("\n") if l.strip()]
                # remove generic footer lines if present
                clean_lines = []
                for l in lines[:15]:
                    if any(stop in l for stop in ["Kütüphane Kodu", "Açılır Menüyü Aç", "Reklam Detaylarını Gör", "Birden fazla"]):
                        break
                    clean_lines.append(l)
                caption = "\n".join(clean_lines)

            if page_name != "Bilinmiyor" or len(caption) > 30:
                ads_data.append({
                    "lib_id": lib_id,
                    "start_date": start_date,
                    "page_name": page_name,
                    "caption": caption[:400]
                })

        print(f"Parsed {len(ads_data)} valid ads")

        # Save to JSON
        out_json = os.path.join(output_dir, "meta_ad_library_raw_ads.json")
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(ads_data, f, ensure_ascii=False, indent=2)

        print(f"Saved to {out_json}")
        await browser.close()

asyncio.run(scrape())
