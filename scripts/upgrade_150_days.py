import json
import re
import sys
import os

HTML_PATH = '/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html'

def load_data():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'const programsData = (\[.*?\]);', content, re.DOTALL)
    if not match:
        raise ValueError("Could not find programsData in HTML")
    return json.loads(match.group(1)), content, match.start(1), match.end(1)

print("Script template ready.")
