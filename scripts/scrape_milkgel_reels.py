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

print("Collecting milkgel_official reels...")
all_reels = set()

for i in range(10):
    js = '''
    (() => {
        let links = Array.from(document.querySelectorAll('a[href*="/reel/"]')).map(a => a.href);
        window.scrollBy(0, 1500);
        return JSON.stringify(links);
    })()
    '''
    raw = run_js(js)
    try:
        batch = json.loads(raw)
        for l in batch:
            clean = l.split('?')[0]
            if '/reel/' in clean and 'milkgel_official' in clean:
                all_reels.add(clean)
    except:
        pass
    print(f"Scroll {i+1}: found {len(all_reels)} reels")
    time.sleep(1.8)

reels_list = sorted(list(all_reels))
print(f"Total collected: {len(reels_list)}")

with open("/tmp/milkgel_reel_links.json", "w", encoding="utf-8") as f:
    json.dump(reels_list, f, ensure_ascii=False, indent=2)

print("Saved to /tmp/milkgel_reel_links.json")
