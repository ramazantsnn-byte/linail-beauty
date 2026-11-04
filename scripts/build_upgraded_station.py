import json
import re
import sys
import os

sys.path.append('/Users/applesupport/Desktop/linail beauty/scripts/programs')
from make_transformation import get_transformation_days
from make_authority import get_authority_cues_and_psychology
from make_storytelling import get_storytelling_cues_and_psychology
from make_luxury import get_luxury_cues_and_psychology
from make_asmr import get_asmr_psychology

HTML_PATH = '/Users/applesupport/Desktop/linail beauty/gulsah-reels/index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

match = re.search(r'const programsData = (\[.*?\]);', html_content, re.DOTALL)
if not match:
    print("Error: programsData not found in HTML!")
    sys.exit(1)

programs = json.loads(match.group(1))
print(f"Loaded {len(programs)} programs from HTML.")

# 1. Update ASMR (id: asmr)
asmr_psy = get_asmr_psychology()
for p in programs:
    if p['id'] == 'asmr':
        for i, day in enumerate(p['days']):
            if i < len(asmr_psy):
                day['psychology'] = asmr_psy[i]

# 2. Update Transformation (id: transformation)
trans_data = get_transformation_days()
for p in programs:
    if p['id'] == 'transformation':
        for i, t in enumerate(trans_data):
            if i < len(p['days']):
                day = p['days'][i]
                title, hook_v, hook_t, script, tripod, focus, hands, action, trig, reac, tone = t
                day['title'] = title
                day['hook_visual'] = hook_v
                day['hook_text'] = hook_t
                day['script'] = script
                day['director_cue'] = {
                    "tripod": tripod,
                    "focus": focus,
                    "hands": hands,
                    "action": action
                }
                day['psychology'] = {
                    "trigger": trig,
                    "audience_reaction": reac,
                    "gulsah_tone": tone
                }
                day['caption'] = f"İmkansız diye bir şey yoktur; doğru mimari ve uzmanlık vardır: {title}.\n\nAtaşehir Uphill Towers stüdyomuzda kendi ellerinizin zarafetini keşfetmek için yoruma DÖNÜŞÜM yazın veya WhatsApp'tan bize ulaşın 🤍"
                day['timeline'] = [
                    {"time": "0:00 - 0:03", "label": "🪝 KANCA (İLK 3 SANİYE)", "desc": f"Hasarlı başlangıç anı veya görsel şok. Ekranda kalın yazı: \"{hook_t}\""},
                    {"time": "0:03 - 0:11", "label": "⚙️ İŞLEM & ZANAAT", "desc": f"Zanaat anı: {action[:80]}..."},
                    {"time": "0:11 - 0:18", "label": "✨ DÖNÜŞÜM & ZAFER", "desc": "Kusursuz apeks, cam pürüzsüzlüğü ve danışanın ellerine kavuşma sevinci."},
                    {"time": "0:18 - 0:22", "label": "🎯 VIP ÇAĞRI (CTA)", "desc": "Linail altın amblemi + 'Ataşehir Uphill Towers VIP randevu için yoruma DÖNÜŞÜM yazın'"}
                ]

# 3. Update Authority (id: authority)
auth_data = get_authority_cues_and_psychology()
for p in programs:
    if p['id'] == 'authority':
        for i, a in enumerate(auth_data):
            if i < len(p['days']):
                day = p['days'][i]
                day['director_cue']['tripod'] = a['tripod']
                day['director_cue']['focus'] = a['focus']
                day['director_cue']['hands'] = a['hands']
                day['director_cue']['action'] = a['action']
                day['psychology'] = {
                    "trigger": a['trigger'],
                    "audience_reaction": a['audience_reaction'],
                    "gulsah_tone": a['gulsah_tone']
                }

# 4. Update Storytelling (id: storytelling)
story_data = get_storytelling_cues_and_psychology()
for p in programs:
    if p['id'] == 'storytelling':
        for i, s in enumerate(story_data):
            if i < len(p['days']):
                day = p['days'][i]
                day['director_cue']['tripod'] = s['tripod']
                day['director_cue']['focus'] = s['focus']
                day['director_cue']['hands'] = s['hands']
                day['director_cue']['action'] = s['action']
                day['psychology'] = {
                    "trigger": s['trigger'],
                    "audience_reaction": s['audience_reaction'],
                    "gulsah_tone": s['gulsah_tone']
                }

# 5. Update Luxury (id: luxury)
lux_data = get_luxury_cues_and_psychology()
for p in programs:
    if p['id'] == 'luxury':
        for i, l in enumerate(lux_data):
            if i < len(p['days']):
                day = p['days'][i]
                day['director_cue']['tripod'] = l['tripod']
                day['director_cue']['focus'] = l['focus']
                day['director_cue']['hands'] = l['hands']
                day['director_cue']['action'] = l['action']
                day['psychology'] = {
                    "trigger": l['trigger'],
                    "audience_reaction": l['audience_reaction'],
                    "gulsah_tone": l['gulsah_tone']
                }

print("All 150 days successfully enriched with psychology and bespoke director cues.")

# Verify uniqueness
for p in programs:
    scripts = [d.get('script', '') for d in p['days']]
    hooks = [d.get('hook_text', '') for d in p['days']]
    actions = [d.get('director_cue', {}).get('action', '') for d in p['days']]
    psy = [d.get('psychology', {}).get('trigger', '') for d in p['days']]
    print(f"[{p['name']}] Days: {len(p['days'])} | Unique Scripts: {len(set(scripts))} | Unique Hooks: {len(set(hooks))} | Unique Actions: {len(set(actions))} | Unique Psychology: {len(set(psy))}")

# Convert back to JSON
new_json_str = json.dumps(programs, ensure_ascii=False)

# Replace in HTML
start_idx = match.start(1)
end_idx = match.end(1)
updated_html = html_content[:start_idx] + new_json_str + html_content[end_idx:]

# Add CSS for psychology-box if not already present
psy_css = """
    /* İNSAN DAVRANIŞI & KİTLE PSİKOLOJİSİ ANALİZ KUTUSU */
    .psychology-box {
      background: linear-gradient(135deg, rgba(56, 239, 125, 0.08) 0%, rgba(62, 27, 71, 0.5) 100%);
      border: 1.5px solid rgba(56, 239, 125, 0.4);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      margin-bottom: 20px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
      position: relative;
    }
    .psychology-title {
      font-size: 13px;
      font-weight: 800;
      color: #38ef7d;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .psychology-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
    }
    .psy-item {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 8px;
      padding: 12px 14px;
    }
    .psy-label {
      font-size: 11px;
      font-weight: 800;
      color: var(--gold-light);
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .psy-desc {
      font-size: 13.5px;
      color: #f1f5f9;
      line-height: 1.55;
    }
"""

if '.psychology-box' not in updated_html:
    updated_html = updated_html.replace('/* RAMAZAN HIZLI ÇEKİM MODU */', psy_css + '\n    /* RAMAZAN HIZLI ÇEKİM MODU */')

# Add psychology box into renderCard()
psy_card_html = """
          <!-- 🧠 İNSAN DAVRANIŞI & KİTLE PSİKOLOJİSİ ANALİZİ -->
          ${day.psychology ? `
          <div class="psychology-box">
            <div class="psychology-title">
              <span>🧠</span>
              <span>İnsan Davranışı Analizi: "İzleyici Neden Ekrana Kilitlenecek & Yorum Atacak?"</span>
            </div>
            <div class="psychology-grid">
              <div class="psy-item">
                <div class="psy-label">🎯 Bilinçaltı Tetikleyici & Duygu Analizi</div>
                <div class="psy-desc">${day.psychology.trigger}</div>
              </div>
              <div class="psy-item">
                <div class="psy-label">💬 Beklenen İzleyici Tepkisi & Algoritma Refleksi</div>
                <div class="psy-desc">${day.psychology.audience_reaction}</div>
              </div>
              <div class="psy-item">
                <div class="psy-label">🎙️ Gülşah'ın Masadaki Doğal Tavrı (Anti-AI Samimiyet)</div>
                <div class="psy-desc">${day.psychology.gulsah_tone}</div>
              </div>
            </div>
          </div>
          ` : ''}

          <!-- 3-Second Hook Box -->"""

if '<!-- 🧠 İNSAN DAVRANIŞI & KİTLE PSİKOLOJİSİ ANALİZİ -->' not in updated_html:
    updated_html = updated_html.replace('<!-- 3-Second Hook Box -->', psy_card_html)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("index.html successfully updated and written to disk!")
