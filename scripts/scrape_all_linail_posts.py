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

print("Starting link collection by scrolling...")
all_links = set()

# Scroll 15 times to load all posts
for i in range(18):
    js_get_links = '''
    (() => {
        let links = Array.from(document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]'))
                         .map(a => a.href);
        window.scrollBy(0, 1200);
        return JSON.stringify(links);
    })()
    '''
    raw = run_js(js_get_links)
    try:
        current_batch = json.loads(raw)
        for l in current_batch:
            clean_url = l.split('?')[0]
            if '/linail.beautystudio/' in clean_url or '/p/' in clean_url or '/reel/' in clean_url:
                all_links.add(clean_url)
    except Exception as e:
        pass
    print(f"Scroll {i+1}/18: found {len(all_links)} unique posts so far")
    time.sleep(2.0)

all_links_list = sorted(list(all_links))
print(f"Total collected links: {len(all_links_list)}")

with open("/tmp/linail_all_links.json", "w", encoding="utf-8") as f:
    json.dump(all_links_list, f, ensure_ascii=False, indent=2)

print("Saved links to /tmp/linail_all_links.json")
