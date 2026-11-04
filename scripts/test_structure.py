import json

with open('/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'const programsData = (\[.*?\]);', text, re.DOTALL)
data = json.loads(match.group(1))

print("Total programs:", len(data))
for p in data:
    print(p['id'], len(p['days']))
