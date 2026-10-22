#!/usr/bin/env python3
"""
Linail Beauty Studio - Automated AI & Search Engine Direct Pinger
Submits linailbeauty.com, llms.txt, and services directly to IndexNow (Bing & OpenAI SearchGPT) and Yandex.
"""

import json
import ssl
import urllib.request
import urllib.error

INDEXNOW_KEY = "8d0264458c1d4d1dbe44ae92a93d2206"
HOST = "linailbeauty.com"
URLS = [
    "https://linailbeauty.com/",
    "https://linailbeauty.com/llms.txt",
    "https://linailbeauty.com/atasehir-protez-tirnak/",
    "https://linailbeauty.com/sitemap.xml"
]

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

def ping_engines():
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{HOST}/{INDEXNOW_KEY}.txt",
        "urlList": URLS
    }
    data = json.dumps(payload).encode("utf-8")

    # SSL context handling for macOS Python
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for endpoint in ENDPOINTS:
        req = urllib.request.Request(
            endpoint,
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                print(f"[OK] {endpoint} -> HTTP {response.status}")
        except urllib.error.HTTPError as e:
            print(f"[HTTP ERROR] {endpoint} -> HTTP {e.code}: {e.read().decode('utf-8')}")
        except Exception as e:
            print(f"[ERROR] {endpoint} -> {e}")

if __name__ == "__main__":
    print("Linail Beauty AI Search Indexing Pipeline Started...")
    ping_engines()
    print("Finished direct AI engine submission.")
