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

def inspect_reels(links, output_file, label):
    print(f"\n--- Analyzing {label} ({len(links)} reels) ---")
    results = []
    for idx, url in enumerate(links[:15]):
        print(f"[{idx+1}/15] {url}...")
        apple_script = f'''
        tell application "Google Chrome"
            set activeTab to active tab of front window
            set URL of activeTab to "{url}"
        end tell
        '''
        run_applescript(apple_script)
        time.sleep(2.5)
        
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
            # parse likes
            m = re.search(r'([0-9,\.Kk]+)\s*likes?', desc)
            likes = m.group(1) if m else "?"
            clean_cap = re.sub(r'^[0-9,\.Kk]+\s*likes?,\s*[0-9,\.Kk]+\s*comments?\s*-\s*[^:]+:\s*\"?', '', desc).strip('\" .')
            dur = data.get("duration", 0)
            data["likes"] = likes
            data["cleanCaption"] = clean_cap
            data["firstLine"] = clean_cap.split('\n')[0] if clean_cap else "Empty"
            results.append(data)
            print(f"   Likes: {likes} | Dur: {dur:.1f}s | Hook: {data['firstLine'][:75]}")
        except Exception as e:
            print(f"   Error: {e}")
            
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file}")

# Load blick lashes
with open("/tmp/blick_lashes_links.json") as f:
    blick_links = json.load(f)

# Load thefacespace
with open("/tmp/thefacespace_links.json") as f:
    facespace_links = json.load(f)

inspect_reels(blick_links, "/tmp/blick_lashes_analyzed.json", "BLICK LASHES (Lash Lifting)")
inspect_reels(facespace_links, "/tmp/thefacespace_analyzed.json", "THE FACE SPACE (Brow Lamination)")
print("\nALL REELS INSPECTED SUCCESSFULLY!")
