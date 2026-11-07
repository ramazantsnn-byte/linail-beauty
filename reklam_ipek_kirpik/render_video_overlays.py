import os
import asyncio
from playwright.async_api import async_playwright

output_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"

logo_path = f"file://{assets_dir}/linail_full_logo_clean.png"

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: transparent;
    font-family: 'Montserrat', sans-serif;
    color: #FAF8F5;
    -webkit-font-smoothing: antialiased;
  }}
  .overlay-canvas {{
    width: 1080px;
    height: 1920px;
    position: relative;
    overflow: hidden;
    background: transparent;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 90px 70px 100px 70px;
    margin-bottom: 50px;
  }}
  
  .serif-title {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
  }}
  .gold-gradient-text {{
    background: linear-gradient(135deg, #FFF0BE 0%, #D4AF37 50%, #AA8222 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  
  .glass-card {{
    background: rgba(18, 7, 24, 0.78);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(212, 175, 55, 0.4);
    border-radius: 28px;
    padding: 32px 36px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  }}

  .pill {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 24px;
    background: rgba(0,0,0,0.75);
    border: 1px solid rgba(212,175,55,0.4);
    border-radius: 100px;
    font-size: 15px;
    color: #FFF0BE;
    font-weight: 600;
    letter-spacing: 0.1em;
  }}
  
  .header-logo {{
    height: 52px;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,0.8));
  }}
</style>
</head>
<body>

<!-- ================= SCENE 1 OVERLAY ================= -->
<div class="overlay-canvas" id="scene1">
  <!-- Top Section -->
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 35px;">
      <img src="{logo_path}" class="header-logo">
      <div class="pill">📍 Ataşehir Uphill Towers</div>
    </div>
    
    <div class="glass-card" style="text-align: center;">
      <span style="font-size: 14px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 8px;">
        Göz Mimari Rehberi
      </span>
      <h1 class="serif-title" style="font-size: 56px; line-height: 1.15; margin-bottom: 12px;">
        <span class="gold-gradient-text">Cat Eye</span> mı, <span class="gold-gradient-text">Wispy</span> mi? 👁️
      </h1>
      <p style="font-size: 20px; color: #DDD8CF; font-weight: 400;">
        Arkadaşın kararsızsa bu videoyu ona gönder 💜
      </p>
    </div>
  </div>

  <!-- Bottom Section -->
  <div style="text-align: center;">
    <div class="pill" style="font-size: 16px; padding: 12px 28px;">
      ✨ Göz Kapağına Özel Kişiselleştirilmiş Tasarım
    </div>
  </div>
</div>

<!-- ================= SCENE 2 OVERLAY ================= -->
<div class="overlay-canvas" id="scene2">
  <!-- Top Section -->
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 35px;">
      <img src="{logo_path}" class="header-logo">
      <div class="pill">Usta Zanaatı</div>
    </div>
    
    <div class="glass-card">
      <span style="font-size: 14px; letter-spacing: 0.25em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 8px;">
        Tek Bir Kalıp Yoktur
      </span>
      <h2 class="serif-title" style="font-size: 48px; line-height: 1.18; margin-bottom: 14px;">
        Göz Yapınıza Göre <br/><span class="gold-gradient-text">Milimetrik Tasarım</span>
      </h2>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 18px; color: #DDD8CF;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="color: #D4AF37;">✦</span> 0.07 mm İpek Lifler &bull; Sıfır Ağırlık Hissi
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="color: #D4AF37;">✦</span> Medikal Hipoalerjenik &bull; Sıfır Yanma ve Sulanma
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom Section -->
  <div style="text-align: center;">
    <div class="pill" style="font-size: 16px; padding: 12px 28px; background: rgba(18,7,24,0.85);">
      🤎 Kahve İpek Kirpik • Doğal Buğulu Derinlik
    </div>
  </div>
</div>

<!-- ================= SCENE 3 OVERLAY ================= -->
<div class="overlay-canvas" id="scene3">
  <!-- Top Section -->
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 35px;">
      <img src="{logo_path}" class="header-logo">
      <div class="pill">VIP Süit Konforu</div>
    </div>
    
    <div class="glass-card" style="text-align: center;">
      <span style="font-size: 14px; letter-spacing: 0.25em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 8px;">
        Sabahları Zahmetsiz Güzellik
      </span>
      <h2 class="serif-title" style="font-size: 52px; line-height: 1.15; margin-bottom: 10px;">
        Sabah <span class="gold-gradient-text">Rimele Son ✨</span>
      </h2>
      <p style="font-size: 20px; color: #DDD8CF; font-weight: 300;">
        4–6 hafta boyunca formu bozulmayan taze bakışlar.
      </p>
    </div>
  </div>

  <!-- Bottom Section -->
  <div style="text-align: center;">
    <div class="glass-card" style="padding: 22px; display: inline-block;">
      <div style="font-size: 17px; color: #FFF0BE; font-weight: 600;">☕️ Uphill Towers 14. Kat Butik Deneyimi</div>
      <div style="font-size: 14px; color: #DDD8CF; margin-top: 4px;">Günde yalnızca sınırlı sayıda VIP misafir kabul edilir.</div>
    </div>
  </div>
</div>

<!-- ================= SCENE 4 OVERLAY ================= -->
<div class="overlay-canvas" id="scene4">
  <!-- Top Section -->
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 35px;">
      <img src="{logo_path}" class="header-logo">
      <div class="pill">Randevu & Analiz</div>
    </div>
  </div>

  <!-- Center Call To Action Card -->
  <div class="glass-card" style="text-align: center; padding: 42px 36px;">
    <span style="font-size: 15px; letter-spacing: 0.25em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 12px;">
      Ücretsiz Göz Yapısı Analizi
    </span>
    <h2 class="serif-title" style="font-size: 52px; line-height: 1.15; margin-bottom: 16px;">
      Göz Fotoğrafınızı <br/><span class="gold-gradient-text">DM’den Gönderin 🌸</span>
    </h2>
    <p style="font-size: 19px; color: #DDD8CF; line-height: 1.45; margin-bottom: 28px; font-weight: 300;">
      Hangi modelin göz kapağınızı en güzel kaldıracağını birlikte belirleyelim.
    </p>
    
    <div style="display: inline-flex; align-items: center; gap: 12px; padding: 16px 36px; background: linear-gradient(135deg, #D4AF37 0%, #AA8222 100%); color: #18091E; font-weight: 700; font-size: 18px; border-radius: 100px; box-shadow: 0 12px 30px rgba(212,175,55,0.4);">
      <span>Randevu Al: DM Gönderin</span>
      <span>➔</span>
    </div>
  </div>

  <!-- Bottom Section -->
  <div style="text-align: center;">
    <div style="font-size: 16px; color: #FFF0BE; font-weight: 600; margin-bottom: 6px;">
      📍 Barbaros Mah. Uphill Towers B Blok D:14 &bull; Ataşehir
    </div>
    <div style="font-size: 15px; color: #D4AF37; font-weight: 500;">
      ☎️ WhatsApp VIP: 0531 869 67 64
    </div>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(output_dir, "video_overlays.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

async def render_overlays():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        await page.goto(f"file://{html_path}")
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(1)

        for scene in ["scene1", "scene2", "scene3", "scene4"]:
            elem = page.locator(f"#{scene}")
            out_png = os.path.join(output_dir, f"overlay_{scene}.png")
            await elem.screenshot(path=out_png, omit_background=True)
            print(f"Rendered overlay: {out_png}")

        await browser.close()

asyncio.run(render_overlays())
