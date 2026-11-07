#!/usr/bin/env python3
import subprocess
import json
import time

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

def get_caption_from_post(url):
    apple_script = f'''
    tell application "Google Chrome"
        set activeTab to active tab of front window
        set URL of activeTab to "{url}"
    end tell
    '''
    run_applescript(apple_script)
    time.sleep(3.5)
    
    js = '''
    (() => {
        let metaDesc = document.querySelector('meta[name="description"]')?.content || "";
        let ogDesc = document.querySelector('meta[property="og:description"]')?.content || "";
        let ogTitle = document.querySelector('meta[property="og:title"]')?.content || "";
        
        // Also look for post text inside the DOM if available
        let articleText = "";
        let article = document.querySelector('article');
        if (article) {
            let spans = article.querySelectorAll('h1, span');
            for (let s of spans) {
                if (s.innerText && s.innerText.length > 15) {
                    articleText += s.innerText + "\\n";
                }
            }
        }
        
        return JSON.stringify({
            url: window.location.href,
            metaDesc: metaDesc,
            ogDesc: ogDesc,
            ogTitle: ogTitle,
            articleText: articleText.slice(0, 500)
        });
    })()
    '''
    raw = run_js(js)
    try:
        return json.loads(raw)
    except Exception:
        return {"url": url, "raw": raw}

posts = [
    "https://www.instagram.com/linail.beautystudio/reel/DfXONoFIYMO/",
    "https://www.instagram.com/linail.beautystudio/p/DfUp7yRlS4_/",
    "https://www.instagram.com/linail.beautystudio/p/DfCCKF0iF_5/",
    "https://www.instagram.com/linail.beautystudio/p/DfAGTVsioJ3/",
    "https://www.instagram.com/linail.beautystudio/reel/De9xtVHKsyn/",
    "https://www.instagram.com/linail.beautystudio/p/Dev_U4Biu0y/",
    "https://www.instagram.com/linail.beautystudio/reel/DeeAO8eKBVa/",
    "https://www.instagram.com/linail.beautystudio/p/DeWdI_WCF2Y/",
    "https://www.instagram.com/linail.beautystudio/reel/DeT7QxRC_Kj/"
]

all_data = []
for p in posts:
    data = get_caption_from_post(p)
    all_data.append(data)
    print(f"[{p}] -> {data.get('metaDesc')[:80] if data.get('metaDesc') else 'EMPTY'}")

with open("/tmp/linail_extracted_captions.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("\n--- ALL DONE. Extracted", len(all_data), "posts ---")
