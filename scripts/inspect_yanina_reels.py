#!/usr/bin/env python3
import subprocess
import json
import time
import re

def run_applescript(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def run_js(js_code):
    escaped_js = js_code.replace('\\', '\\\\').replace('"', '\\"')
    apple_script = f'''
    tell application "Google Chrome"
        set activeTab to active tab of front window
        execute activeTab javascript "{escaped_js}"
    end tell
    '''
    return run_applescript(apple_script)

pinned_and_top = [
    "https://www.instagram.com/yanina_rai/reel/DX9vl8GoZkc/",
    "https://www.instagram.com/yanina_rai/reel/DQ56y1yiIRa/",
    "https://www.instagram.com/yanina_rai/reel/DXETruwCIP0/",
    "https://www.instagram.com/yanina_rai/reel/DfZY-vmoa-2/",
    "https://www.instagram.com/yanina_rai/reel/DfMY7WHo9z2/",
    "https://www.instagram.com/yanina_rai/reel/DfH_YToIa7o/",
    "https://www.instagram.com/yanina_rai/reel/DfHg0vvIXKZ/",
    "https://www.instagram.com/yanina_rai/reel/De44xCHon2Z/",
    "https://www.instagram.com/yanina_rai/reel/Dew4_yGoErr/",
    "https://www.instagram.com/yanina_rai/reel/DetllrEoYfP/",
    "https://www.instagram.com/yanina_rai/reel/DeI3y7aIBz_/",
    "https://www.instagram.com/yanina_rai/reel/Dd-1n3_opW2/",
    "https://www.instagram.com/yanina_rai/reel/Dc96H7uo6Zk/",
    "https://www.instagram.com/yanina_rai/reel/Dc2x7H4IK_n/",
    "https://www.instagram.com/yanina_rai/reel/DcrH4oYoe_7/"
]

results = []
print(f"Inspecting {len(pinned_and_top)} top reels from Yanina Rai...")

for idx, url in enumerate(pinned_and_top):
    print(f"[{idx+1}/{len(pinned_and_top)}] Navigating to {url}...")
    apple_script = f'''
    tell application "Google Chrome"
        set activeTab to active tab of front window
        set URL of activeTab to "{url}"
    end tell
    '''
    run_applescript(apple_script)
    time.sleep(2.6)
    
    js = '''
    (() => {
        let metaDesc = document.querySelector('meta[name="description"]')?.content || "";
        let ogDesc = document.querySelector('meta[property="og:description"]')?.content || "";
        let video = document.querySelector('video');
        let duration = video ? video.duration : 0;
        let title = document.title;
        
        return JSON.stringify({
            url: window.location.href,
            title: title,
            metaDesc: metaDesc,
            ogDesc: ogDesc,
            duration: duration
        });
    })()
    '''
    raw = run_js(js)
    try:
        data = json.loads(raw)
        desc = data.get("metaDesc") or data.get("ogDesc") or ""
        m = re.search(r'([0-9,\.Kk]+)\s*likes?', desc)
        likes = m.group(1) if m else "?"
        clean_cap = re.sub(r'^[0-9,\.Kk]+\s*likes?,\s*[0-9,\.Kk]+\s*comments?\s*-\s*[^:]+:\s*\"?', '', desc).strip('\" .')
        data["likes"] = likes
        data["cleanCaption"] = clean_cap
        data["firstLine"] = clean_cap.split('\n')[0] if clean_cap else "Empty"
        dur = data.get("duration", 0)
        results.append(data)
        print(f"   Likes: {likes:<6} | Dur: {dur:.1f}s | Hook: {data['firstLine'][:75]}")
    except Exception as e:
        print(f"   Error: {e}")

with open("/tmp/yanina_rai_analyzed.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved Yanina Rai reels to /tmp/yanina_rai_analyzed.json")
