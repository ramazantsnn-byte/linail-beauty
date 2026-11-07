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

with open("/tmp/milkgel_reel_links.json", "r", encoding="utf-8") as f:
    links = json.load(f)

# Pick top 20 reels (some latest, some pinned, some random distributed)
selected_links = links[:25]

results = []

for idx, url in enumerate(selected_links):
    print(f"[{idx+1}/{len(selected_links)}] Navigating to {url}...")
    apple_script = f'''
    tell application "Google Chrome"
        set activeTab to active tab of front window
        set URL of activeTab to "{url}"
    end tell
    '''
    run_applescript(apple_script)
    time.sleep(2.8)
    
    js = '''
    (() => {
        let metaDesc = document.querySelector('meta[name="description"]')?.content || "";
        let ogDesc = document.querySelector('meta[property="og:description"]')?.content || "";
        let video = document.querySelector('video');
        let videoSrc = video ? (video.src || video.currentSrc) : "";
        let duration = video ? video.duration : 0;
        let title = document.title;
        
        // Also get any visible text in article or main
        let bodyText = "";
        let article = document.querySelector('article') || document.querySelector('main');
        if (article) {
            let spans = article.querySelectorAll('h1, span, p');
            for (let s of spans) {
                if (s.innerText && s.innerText.length > 20) {
                    bodyText += s.innerText + "\\n";
                }
            }
        }
        
        return JSON.stringify({
            url: window.location.href,
            title: title,
            metaDesc: metaDesc,
            ogDesc: ogDesc,
            duration: duration,
            videoSrc: videoSrc,
            bodyText: bodyText.slice(0, 500)
        });
    })()
    '''
    raw = run_js(js)
    try:
        data = json.loads(raw)
        results.append(data)
        desc = data.get("metaDesc") or data.get("ogDesc") or ""
        print(f"   -> {desc[:100]}")
    except Exception as e:
        print(f"   -> Error parsing JSON: {e}")

with open("/tmp/milkgel_analyzed_reels.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved 25 analyzed reels to /tmp/milkgel_analyzed_reels.json")
