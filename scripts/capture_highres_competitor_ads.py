import os
import re
import json
import asyncio
import urllib.request
from playwright.async_api import async_playwright

output_dir = "/Users/applesupport/Desktop/linail beauty/reklam_calisma_defteri_20_kasim/rakip_reklam_gorselleri"
os.makedirs(output_dir, exist_ok=True)

async def capture_all():
    url = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=TR&q=ipek%20kirpik&search_type=keyword_unordered&media_type=all"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use device_scale_factor=2 for razor sharp Retina screenshots
        context = await browser.new_context(
            viewport={"width": 1440, "height": 1000},
            device_scale_factor=2,
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        print("Navigating to Meta Ad Library...")
        await page.goto(url, wait_until="domcontentloaded", timeout=25000)
        await page.wait_for_timeout(4000)

        # Scroll down to load cards
        for i in range(10):
            await page.mouse.wheel(0, 1500)
            await page.wait_for_timeout(1000)

        # Query all individual ad card containers
        cards = await page.locator("div.xh8yej3").all()
        print(f"Total potential card containers: {len(cards)}")

        extracted_ads = []
        count = 0

        for idx, card in enumerate(cards):
            box = await card.bounding_box()
            if not box or box["width"] < 350 or box["width"] > 550 or box["height"] < 350:
                continue

            text = await card.inner_text()
            if "Kütüphane Kodu" not in text:
                continue
            if not any(w in text.lower() for w in ["kirpik", "güzellik", "beauty", "lounge", "studio", "manikür"]):
                continue

            img = card.locator("img[src*='fbcdn']").first
            img_src = ""
            if await img.count() > 0:
                img_src = await img.get_attribute("src")

            count += 1
            card_img_filename = f"kart_{count}.png"
            card_img_path = os.path.join(output_dir, card_img_filename)
            await card.screenshot(path=card_img_path)

            # Download raw creative if available
            raw_creative_filename = f"kreatif_{count}.jpg"
            raw_creative_path = os.path.join(output_dir, raw_creative_filename)
            if img_src and img_src.startswith("http"):
                try:
                    urllib.request.urlretrieve(img_src, raw_creative_path)
                except Exception as e:
                    pass

            # Extract details
            sponsor_match = re.search(r'Reklam Detaylarını Gör\s*\n\s*([^\n]+)', text)
            sponsor = sponsor_match.group(1).strip() if sponsor_match else "Güzellik Stüdyosu"

            date_match = re.search(r'(\d+\s+[A-Za-zğüşıöçĞÜŞİÖÇ]+\s+\d{4})', text)
            start_date = date_match.group(1) if date_match else "Aktif Reklam"

            # Clean caption snippet
            caption = text.replace("Reklam Detaylarını Gör", "").replace("Açılır Menüyü Aç", "").strip()
            lines = [l.strip() for l in caption.split("\n") if len(l.strip()) > 3]

            extracted_ads.append({
                "id": count,
                "sponsor": sponsor,
                "start_date": start_date,
                "card_screenshot": card_img_filename,
                "raw_creative": raw_creative_filename if os.path.exists(raw_creative_path) else "",
                "snippet": "\n".join(lines[:8])
            })

            print(f"Captured Ad #{count}: {sponsor} ({start_date})")
            if count >= 8:
                break

        # Generate HTML Showcase
        html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Meta Ad Library • Canlı Rakip İpek Kirpik Reklamları Galerisi</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Cormorant+Garamond:wght@600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #0B0F19;
    color: #F3F4F6;
    font-family: 'Inter', sans-serif;
    padding: 40px 24px;
    line-height: 1.6;
  }
  .container { max-width: 1400px; margin: 0 auto; }
  header {
    text-align: center;
    padding-bottom: 30px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 40px;
  }
  .badge-meta {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    background: rgba(37, 99, 235, 0.15);
    border: 1px solid rgba(59, 130, 246, 0.4);
    border-radius: 100px;
    font-size: 13px;
    font-weight: 600;
    color: #60A5FA;
    margin-bottom: 12px;
  }
  h1 {
    font-size: 34px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
  }
  p.subtitle {
    font-size: 16px;
    color: #9CA3AF;
    max-width: 750px;
    margin: 0 auto;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
    gap: 32px;
  }
  .ad-box {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    overflow: hidden;
    padding: 24px;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }
  .ad-box:hover {
    transform: translateY(-4px);
    border-color: #3B82F6;
  }
  .ad-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  }
  .sponsor-title {
    font-size: 18px;
    font-weight: 700;
    color: #F9FAFB;
  }
  .date-pill {
    font-size: 12px;
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.4);
    color: #34D399;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 600;
  }
  .img-wrapper {
    background: #000;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 18px;
    text-align: center;
  }
  .img-wrapper img {
    width: 100%;
    height: auto;
    max-height: 550px;
    object-fit: contain;
    display: block;
  }
  .caption-box {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 10px;
    padding: 14px;
    font-size: 13px;
    color: #D1D5DB;
    white-space: pre-line;
    max-height: 140px;
    overflow-y: auto;
    border: 1px solid rgba(255, 255, 255, 0.05);
  }
  .btn-open {
    display: inline-block;
    margin-top: 14px;
    padding: 8px 18px;
    background: #2563EB;
    color: white;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    border-radius: 8px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="container">
  <header>
    <div class="badge-meta">⚡ Meta Ad Library &bull; Canlı İstihbarat</div>
    <h1>Türkiye'deki Aktif İpek Kirpik Reklamları & Görselleri</h1>
    <p class="subtitle">
      Meta Reklam Kütüphanesi'nden çekilmiş gerçek reklam kartları. Rakiplerin hangi fotoğrafları, modelleri ve kancaları kullandığını inceleyebilirsiniz.
    </p>
  </header>

  <div class="grid">
"""

        for ad in extracted_ads:
            html_content += f"""
    <div class="ad-box">
      <div class="ad-header">
        <div class="sponsor-title">{ad['sponsor']}</div>
        <div class="date-pill">🟢 {ad['start_date']}</div>
      </div>
      <div class="img-wrapper">
        <img src="{ad['card_screenshot']}" alt="{ad['sponsor']}">
      </div>
      <div class="caption-box">{ad['snippet']}</div>
      <a href="{ad['card_screenshot']}" target="_blank" class="btn-open">🔍 Görseli Büyüt</a>
    </div>
"""

        html_content += """
  </div>
</div>

</body>
</html>
"""

        showcase_path = os.path.join(output_dir, "index.html")
        with open(showcase_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Created visual showcase: {showcase_path}")
        await browser.close()

asyncio.run(capture_all())
