#!/usr/bin/env python3
import json
import re

# Load modal walked posts
with open("/tmp/linail_posts_full_modal.json", "r", encoding="utf-8") as f:
    modal_posts = json.load(f)

# Load previously extracted captions from top reels
with open("/tmp/linail_extracted_captions.json", "r", encoding="utf-8") as f:
    top_posts = json.load(f)

all_posts_map = {}

# Process top posts first
for p in top_posts:
    url = p["url"].split("?")[0].rstrip("/")
    if "linail.beautystudio" in url and ("/p/" in url or "/reel/" in url):
        caption = p.get("metaDesc") or p.get("ogDesc") or ""
        # Clean caption from prefix "X likes, Y comments - linail.beautystudio, Date: "
        clean_cap = re.sub(r'^[0-9,.]+\s*likes?,\s*[0-9,.]+\s*comments?\s*-\s*linail\.beautystudio[^:]*:\s*\"?', '', caption)
        clean_cap = clean_cap.rstrip('". ')
        if clean_cap:
            all_posts_map[url] = {
                "url": url,
                "caption": clean_cap,
                "time": ""
            }

# Add modal posts
for p in modal_posts:
    url = p["url"].split("?")[0].rstrip("/")
    caption = p.get("caption", "").strip()
    if caption:
        all_posts_map[url] = {
            "url": url,
            "caption": caption,
            "time": p.get("time", "")
        }

unified_posts = list(all_posts_map.values())
print(f"Total unified unique posts: {len(unified_posts)}")

# Categorization and Analysis
categorized = {
    "Protez Tırnak & Jel Güçlendirme & Nail Art": [],
    "Kaş & İpek Kirpik (Laminasyon / Lifting)": [],
    "Cam Cilt & Cilt Protokolü": [],
    "Boutique Salon Deneyimi & Hijyen & Mizah": []
}

hashtag_freq = {}
emojis_found = {}

emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)

for post in unified_posts:
    cap = post["caption"]
    cap_lower = cap.lower()
    
    # Emojis
    for em in emoji_pattern.findall(cap):
        emojis_found[em] = emojis_found.get(em, 0) + 1
        
    # Hashtags
    tags = re.findall(r'#([A-Za-z0-9_ğüşıöçĞÜŞİÖÇ]+)', cap)
    post["hashtags"] = tags
    for t in tags:
        tl = t.lower()
        hashtag_freq[tl] = hashtag_freq.get(tl, 0) + 1
        
    # Category
    if any(k in cap_lower for k in ["cam cilt", "hydrafacial", "genosys", "cilt", "gözenek", "somon dna"]):
        cat = "Cam Cilt & Cilt Protokolü"
    elif any(k in cap_lower for k in ["kirpik", "lashes", "laminasyon", "lifting", "kaş", "brow"]):
        cat = "Kaş & İpek Kirpik (Laminasyon / Lifting)"
    elif any(k in cap_lower for k in ["tırnak", "nail", "manikür", "pedikür", "protez", "jel", "kalıcı oje", "french", "cat eye tırnak", "luxio"]):
        cat = "Protez Tırnak & Jel Güçlendirme & Nail Art"
    else:
        cat = "Boutique Salon Deneyimi & Hijyen & Mizah"
        
    post["category"] = cat
    categorized[cat].append(post)

# Save Master Unified JSON
with open("/tmp/linail_master_unified_posts.json", "w", encoding="utf-8") as f:
    json.dump(unified_posts, f, ensure_ascii=False, indent=2)

print("Unified posts saved successfully.")
