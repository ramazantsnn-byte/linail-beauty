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

posts = []
print("Starting sequential modal walk through all Linail Beauty posts...")

# Maximum 90 posts
for i in range(90):
    js_extract_and_next = '''
    (() => {
        // Extract caption
        let h1 = document.querySelector("div[role='dialog'] h1") || document.querySelector("article h1");
        let caption = h1 ? h1.innerText : "";
        
        // Extract time
        let timeEl = document.querySelector("div[role='dialog'] time") || document.querySelector("article time");
        let postTime = timeEl ? timeEl.getAttribute("datetime") : "";
        
        // Extract likes
        let likesText = "";
        let likesSection = document.querySelector("section");
        if (likesSection) {
            let spans = likesSection.querySelectorAll("span");
            for (let s of spans) {
                if (s.innerText && (s.innerText.includes("beğenme") || s.innerText.includes("like") || s.innerText.includes("diğer kişi"))) {
                    likesText = s.innerText;
                    break;
                }
            }
        }
        
        // Current URL
        let url = window.location.href;
        
        // Find next button
        let nextBtn = document.querySelector("svg[aria-label='İleri'], svg[aria-label='Next']")?.closest("button") || 
                      document.querySelector("div[role='dialog'] a[role='link'] svg[aria-label='İleri']")?.closest("a") ||
                      document.querySelector("div[role='dialog'] svg[aria-label='İleri']")?.closest("div[role='button']");
        
        let hasNext = false;
        if (nextBtn) {
            hasNext = true;
            nextBtn.click();
        } else {
            // Also try pressing ArrowRight on document
            document.dispatchEvent(new KeyboardEvent('keydown', {'key': 'ArrowRight', 'code': 'ArrowRight', 'keyCode': 39, 'bubbles': true}));
        }
        
        return JSON.stringify({
            index: ''' + str(i + 1) + ''',
            url: url,
            caption: caption,
            time: postTime,
            likesText: likesText,
            hasNext: hasNext
        });
    })()
    '''
    
    raw = run_js(js_extract_and_next)
    try:
        data = json.loads(raw)
        posts.append(data)
        caption_preview = data['caption'].replace('\n', ' ')[:65]
        print(f"[{i+1}] {data['url'].split('?')[0]} -> {caption_preview}")
        if not data.get('hasNext') and i > 5:
            # Check if next button is really gone
            time.sleep(1.0)
            check_next = run_js("!!(document.querySelector(\"svg[aria-label='İleri'], svg[aria-label='Next']\"))")
            if check_next != "true":
                print("Reached the end of posts!")
                break
    except Exception as e:
        print(f"Error at step {i+1}: {e}")
    
    time.sleep(0.7)

print(f"\nCompleted! Walked {len(posts)} posts.")

with open("/tmp/linail_posts_full_modal.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("Saved to /tmp/linail_posts_full_modal.json")
