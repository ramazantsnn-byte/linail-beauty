#!/usr/bin/env python3
import os
import re

DIR_PATH = "/Users/applesupport/Desktop/linail beauty/reklam_calisma_defteri_20_kasim"
HTML_PATH = "/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html"

# 1. Update markdown files
for fname in os.listdir(DIR_PATH):
    if fname.endswith(".md"):
        fpath = os.path.join(DIR_PATH, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replacements
        c2 = content
        c2 = re.sub(r'ManyChat Otomatik VIP DM', 'Doğrudan Instagram DM & WhatsApp VIP Danışma', c2, flags=re.I)
        c2 = re.sub(r'ManyChat Tetikleyicisi:[^\n]*', 'Randevu & İletişim: Doğrudan Instagram DM veya WhatsApp VIP Hattı (0531 869 67 64)', c2, flags=re.I)
        c2 = re.sub(r'MANYCHAT OTOMASYON YANITI[^\n]*', 'GÜLŞAH HANIM / STÜDYO DM YANIT METNİ (KOPYALA-YAPIŞTIR)', c2, flags=re.I)
        c2 = re.sub(r'ManyChat akışını ve bio\'yu kontrol et', 'WhatsApp iletişim hattını ve bio\'yu kontrol et', c2, flags=re.I)
        c2 = re.sub(r'ManyChat veya doğrudan reklam üzerinden', 'DM veya doğrudan reklam üzerinden', c2, flags=re.I)
        c2 = re.sub(r'ManyChat tek kelime hunileri', 'Doğrudan DM ve WhatsApp VIP yönlendirmesi', c2, flags=re.I)
        c2 = re.sub(r'ManyChat yorum hunileri', 'Doğrudan DM ve WhatsApp VIP dönüşüm hattı', c2, flags=re.I)
        c2 = re.sub(r'ManyChat kelimesi', 'WhatsApp VIP / DM linki', c2, flags=re.I)
        c2 = re.sub(r'ManyChat Çıkartması:[^\n]*', 'İletişim Çıkartması: "DM\'den veya WhatsApp\'tan (0531 869 67 64) yazın, bu haftaki boş saatleri iletelim 🌸"', c2, flags=re.I)
        c2 = re.sub(r'ManyChat hunisi', 'Doğrudan DM ve WhatsApp VIP hattı', c2, flags=re.I)
        c2 = re.sub(r'ManyChat DM hunisi', 'Doğrudan DM & WhatsApp VIP hattı', c2, flags=re.I)
        c2 = re.sub(r'ManyChat Huni Mimarisi', 'Doğrudan DM & VIP Satış Mimarisi', c2, flags=re.I)
        c2 = re.sub(r'ManyChat & CTA', 'WhatsApp VIP & DM Randevu', c2)
        c2 = re.sub(r'ManyChat', 'Doğrudan DM & WhatsApp VIP', c2, flags=re.I)
        
        if c2 != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c2)
            print(f"Updated {fname}")

# 2. Update HTML file
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

html_c2 = html_content
html_c2 = re.sub(r'ManyChat', 'Doğrudan DM & WhatsApp VIP', html_c2, flags=re.I)
html_c2 = re.sub(r'manychat', 'whatsapp_vip', html_c2, flags=re.I)

if html_c2 != html_content:
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_c2)
    print("Updated gulsah-reels/index.html")

print("All ManyChat references successfully replaced with Direct DM & WhatsApp VIP!")
