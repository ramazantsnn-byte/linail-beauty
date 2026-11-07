#!/usr/bin/env python3
import json
import re

HTML_PATH = '/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const programsData = (\[.*?\]);', content, re.DOTALL)
programs = json.loads(match.group(1))

md = """# 👑 150 GÜNLÜK HİKAYE (STORY) & REELS USTALIK ÇALIŞMA DEFTERİ
## Gülşah Taşan & Linail Beauty Studio İçin %100 Organik, Zanaatkar ve Viral İçerik Kılavuzu

> **Hazırlanma Tarihi:** 7 Kasım 2026  
> **Kapsam:** 5 Tematik Program × 30 Gün = **Tam 150 Günlük Günlük Hikaye & Reels Senaryosu**  
> **Referans Alınan Dünya Standartları:**  
> 1. `@milkgel_official` (True 60 FPS, Blik yansıma çizgisi, taktil ASMR, hız kurgusu)  
> 2. `@blick.lashes` (Lash lifting shield geometrisi L vs C, Lami glue balm, reverse zone)  
> 3. `@thefacespace.co` (Under-processing esneklik testi, cımbız siyah noktası, kaş kesim/trimming hatası, mullet kuralı)  
> 4. `@beatrizbmkt` (2 Video Kuralı: Viral keşif vs Satış kapatma, ManyChat tek kelime hunileri)  
> 5. `@yanina_rai` (Masa mengeneli pantograf kol, ters telefon montajı, 3x telefoto makro, -0.3 EV pozlama)  
> **Görsel Web Arayüzü:** Tüm bu 150 gün interaktif olarak `gulsah-reels/index.html` sayfasında da canlı olarak filtrelenebilir ve incelenebilir durumdadır.

---

## 1. YÜRÜTME FELSEFESİ & GÜLŞAH HANIM'IN REDDETTİĞİ HATALARIN ÇÖZÜMÜ

1. **Sıfır Yapay Zeka Klişesi:** *"Kendinizi şımartın"*, *"Güzelliğin adresi"*, *"Paha biçilemez"* gibi içi boş sloganlar çöpe atıldı. Masada kahvesini yudumlayan kadına Staleks makasla et kesen, otoklav poşetini yırtan usta sesi yerleştirildi.
2. **2 Video, 2 Hedef İlkesi:** Her gün körü körüne satış yapılmaz. Bazı günler sadece hipnotik ASMR ve viral mizahla hesap büyütülür; bazı günler ise sterilizasyon ve mimari apeks kanıtlanarak 3.000 ₺ / 2.400 ₺ VIP randevu kapatılır.
3. **4 Slaytlık Kusursuz Hikaye Mimarisi:**
   - **Slide 1 (Kanca Anket):** İzleyicinin acısına dokunan merak sorusu & anket/çıkartma.
   - **Slide 2 (Masadan Makro Kanıt):** 60 FPS telefon çekimiyle zanaat ve kimyasal hassasiyet.
   - **Slide 3 (Eğitici Çözüm):** Neden diğer yerlerde bozulduğu ve Linail'in koruyucu formülü.
   - **Slide 4 (Net CTA):** ManyChat kelimesi veya WhatsApp VIP (`0531 869 67 64`) link çıkartması.

---

"""

for p_idx, prog in enumerate(programs, 1):
    md += f"""## PROGRAM {p_idx}: {prog['name']}
### {prog['tagline']}
> **Açıklama:** {prog['desc']}  
> **Stratejik Rol:** {prog['badge']}  

| Gün | Başlık / Konu | Kanca (Hook / İlk Cümle) | Kamera & Açı (Yanina Rai) | 4 Slaytlık Hikaye (Story) Planı | ManyChat & CTA |
|---|---|---|---|---|---|
"""
    for day in prog['days']:
        d_num = day['day']
        title = day['title'].replace('|', '-')
        hook = day['hook_text'].replace('|', '-').replace('\n', ' ')
        cam = day.get('camera', '').replace('|', '-')
        story_plan = day.get('story', '').replace('\n', '<br/>').replace('|', '-')
        
        # Determine CTA
        cta = "WhatsApp VIP: 0531 869 67 64"
        if "TIRNAK" in day.get('caption', ''):
            cta = "Yoruma 'TIRNAK' yazın 💅"
        elif "LİFTİNG" in day.get('caption', ''):
            cta = "Yoruma 'LİFTİNG' yazın ✨"
        elif "CAM CİLT" in day.get('caption', ''):
            cta = "Yoruma 'CAM CİLT' yazın 🤍"
            
        md += f"| **Gün {d_num}** | {title} | {hook} | {cam} | {story_plan} | {cta} |\n"

    md += "\n---\n\n"

md += """## 2. GÜLŞAH HANIM İÇİN 15 DAKİKALIK GÜNLÜK ÇEKİM SOP'Sİ (MASA PROTOKOLÜ)

1. **Sabah Hazırlığı (2 Dakika):**
   - Masa mengeneli pantograf kolu masanın kenarına sabitleyin.
   - iPhone'u tutucuya **baş aşağı (ters monte)** takın.
   - Tepe Hilal Lambasını (5000K) tırnak/kaş hizasının 25 cm üstüne getirin.
2. **Kamera Ayarı (1 Dakika):**
   - Kamera $\rightarrow$ Video $\rightarrow$ `4K 60 FPS`.
   - `3x Telefoto Lens`i seçin.
   - Masadaki tırnağa/kaşa dokunup **AE/AF Kilitleyin**.
   - Güneş simgesini parmağınızla hafifçe aşağı çekerek **-0.3 EV pozlama** yapın (tırnaktaki ışık parlamasını önleyin).
3. **Kayıt (8 Dakika):**
   - Müşterinin elini 15° açıyla hafif kameraya doğru eğik tutmasını rica edin.
   - İşlemin en tatmin edici 3 anını çekin:
     * Kütikülün tek şerit halinde kesilişi / Pede kirpiklerin taranışı (15 sn)
     * Jelin tırnakta kendiliğinden yayılıp ayna gibi düzleşmesi (15 sn)
     * Tırnağın hilal lamba altında sağa sola çevrilip dümdüz ışık çizgisinin (Blik) gösterilmesi (10 sn).
4. **CapCut Hızlı Montaj (4 Dakika):**
   - 3 videoyu CapCut'a atın.
   - Tekrarlayan kısımları 2.5x hızlandırın; kütikül kesimini ve jel yayılışını 1x normal hızda bırakın.
   - Orijinal sesi %150 yapın (makas çıtırtısı netleşsin). Arkaya kısık (%10) lofi ritim koyun.
   - Dışa aktar: `1080p / 60 FPS`.
"""

OUTPUT_PATH = '/Users/applesupport/Desktop/linail beauty/reklam_calisma_defteri_20_kasim/10_150_GUNLUK_HIKAYE_VE_REELS_USTALIK_DEFTERI.md'
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Master 150-Day Workbook written to {OUTPUT_PATH}")
