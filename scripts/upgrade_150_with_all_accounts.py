#!/usr/bin/env python3
import json
import re
import sys

HTML_PATH = '/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const programsData = (\[.*?\]);', content, re.DOTALL)
if not match:
    print("Could not find programsData in HTML")
    sys.exit(1)

programs = json.loads(match.group(1))
print(f"Loaded {len(programs)} programs from gulsah-reels/index.html")

# Let's inspect each program and inject the new empirical lessons into every single day
# The 5 programs:
# 1. asmr (Hipnotik ASMR & Zanaat) -> Yanina Rai + Milk Gel (Staleks makas çıtırtısı, blik ışık yansıması, 60 FPS, vacuum pop, brush leveling)
# 2. transformation (Dramatik Dönüşüm & Kurtarma) -> Blick Lashes + The Face Space (3 gün sonra ayrışan kaş, düşük göz kapağına L-ped, tırnak apeks dengesi, tırnak etini yırtmadan kurtarma)
# 3. authority (Klinik Otorite & Mit Çökertme) -> The Face Space + Milk Gel (Under-processing, cımbız siyah noktası, kaş kesim/trimming hatası, 4 haftadan fazla taşınan tırnağın kırılması)
# 4. studio (Stüdyo Hikayeleri & Diyaloglar) -> Beatriz + Linail (Temizlik perileri, gizli mesai, sabah alarmı 5 kez erteleyenler, Cat eye mı Wispy mi)
# 5. luxury (Sessiz Lüks & VIP Rezidans) -> Blick Lashes + Yanina Rai (VIP odada aynı anda 2 işlem, 1.5 saatte çıkış, Uphill 14. kat manzarası, Linaura botanik mumu)

camera_standards = [
    "3x Telefoto Makro, Ters Monte Telefon, -0.3 EV, 60 FPS, Tepe Hilal Lamba (5000K)",
    "3x Makro Odak, AE/AF Kilitli, 45° Usta Açısı, Tepe Blik Çizgisi, 60 FPS",
    "90° Profil Yan Açı, Sığ Alan Derinliği (f/1.8), Masaüstü Pantograf Kol, 60 FPS",
    "Extreme Telefoto Makro, Göz İrisine Kilitli Odak, Hilal Lamba Yansıması, 60 FPS"
]

for p_idx, prog in enumerate(programs):
    pid = prog['id']
    print(f"Upgrading program {p_idx+1}: {prog['name']} ({len(prog['days'])} days)...")
    
    for d_idx, day in enumerate(prog['days']):
        d_num = day['day']
        cam = camera_standards[(d_idx) % len(camera_standards)]
        day['camera'] = cam
        
        # Inject realistic salon craft into director cue
        if 'director_cue' in day:
            day['director_cue']['tripod'] = "Telefonu masa mengeneli pantograf kola 'baş aşağı (ters monte)' takın. Masadan 20-25 cm mesafede, 45° açıyla tırnak/kaş çalışma alanına baksın."
            day['director_cue']['focus'] = "iPhone 3x Telefoto Lens. Tırnak/kirpik merkezine 2 saniye basıp AE/AF kilitleyin. Güneş simgesini hafifçe aşağı çekip -0.3 EV pozlama yapın (parlama engelleme)."
            
        # Ensure ManyChat keywords are prominent
        if pid in ['asmr', 'luxury', 'transformation']:
            if d_idx % 3 == 0:
                day['caption'] = day['caption'].replace('FİYAT', 'TIRNAK').replace('RANDEVU', 'TIRNAK')
            elif d_idx % 3 == 1:
                day['caption'] = day['caption'].replace('FİYAT', 'LİFTİNG').replace('RANDEVU', 'LİFTİNG')
            else:
                day['caption'] = day['caption'].replace('FİYAT', 'CAM CİLT').replace('RANDEVU', 'CAM CİLT')
                
        # Upgrade Story field to be a complete 3-4 slide interactive plan
        story_hook = day.get('hook_text', '✨')
        day['story'] = f"""Slide 1 (Kanca Anket): {story_hook} • İzleyiciyi durduran soru & Etkileşim çıkartması
Slide 2 (Masadan Makro Kanıt): Gülşah Hanım'ın ellerinden 60 FPS zanaat / elmas freze / glue balm videosu.
Slide 3 (Eğitici Çözüm): Neden diğer yerlerde bozulduğu ve Linail'in koruyucu kimyası.
Slide 4 (CTA): Yoruma veya DM'ye anahtar kelime yazın / WhatsApp VIP 0531 869 67 64"""

        # Upgrade Psychology gulsah tone
        if 'psychology' in day:
            day['psychology']['gulsah_tone'] = "Sıfır yapay zeka klişesi. Tırnak masasının karşısında kahve ikram eden, Uphill Towers manzarasında steril paketleri açan, işinin ehli artisan usta sesi."

print("All 150 days upgraded in memory.")

# Serialize back into index.html
new_json_str = json.dumps(programs, ensure_ascii=False, indent=2)
new_content = content[:match.start(1)] + new_json_str + content[match.end(1):]

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully updated {HTML_PATH} with updated programsData!")
