import os
import asyncio
from playwright.async_api import async_playwright

output_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"
os.makedirs(output_dir, exist_ok=True)

logo_path = f"file://{assets_dir}/linail_full_logo_clean.png"
emblem_path = f"file://{assets_dir}/linail_emblem_symbol.png"
macro_lash_path = f"file://{assets_dir}/luxury_silk_lash_macro.jpg"
cateye_lash_path = f"file://{assets_dir}/cat_eye_silk_lashes.jpg"
lash_perfect_path = f"file://{assets_dir}/lash_perfect.jpg"

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #0d0412;
    font-family: 'Montserrat', sans-serif;
    color: #FAF8F5;
    -webkit-font-smoothing: antialiased;
  }}
  .ad-canvas {{
    width: 1080px;
    height: 1350px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(160deg, #18091E 0%, #2A1136 45%, #13051A 100%);
    display: flex;
    flex-direction: column;
    padding: 60px 65px;
    margin-bottom: 50px;
  }}
  
  /* Glows */
  .glow-top-right {{
    position: absolute;
    top: -150px;
    right: -150px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(212,175,55,0.22) 0%, rgba(62,27,71,0) 70%);
    pointer-events: none;
  }}
  .glow-bottom-left {{
    position: absolute;
    bottom: -150px;
    left: -150px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(142,68,173,0.28) 0%, rgba(20,5,27,0) 70%);
    pointer-events: none;
  }}
  .gold-border {{
    position: absolute;
    inset: 22px;
    border: 1px solid rgba(212,175,55,0.32);
    pointer-events: none;
    border-radius: 28px;
  }}
  .gold-border::after {{
    content: '';
    position: absolute;
    inset: 8px;
    border: 1px solid rgba(212,175,55,0.12);
    border-radius: 20px;
  }}

  /* Header */
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
    padding-bottom: 22px;
    border-bottom: 1px solid rgba(212,175,55,0.25);
  }}
  .logo-img {{
    height: 48px;
    object-fit: contain;
  }}
  .location-pill {{
    font-size: 14px;
    padding: 8px 20px;
    background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.35);
    border-radius: 100px;
    color: #FFF0BE;
    letter-spacing: 0.1em;
    font-weight: 500;
  }}

  /* Typography */
  .serif-title {{
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    line-height: 1.14;
    color: #FAF8F5;
  }}
  .gold-gradient-text {{
    background: linear-gradient(135deg, #FFF0BE 0%, #D4AF37 50%, #AA8222 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}

  /* Glass Card */
  .glass-card {{
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 22px;
    padding: 26px 30px;
    position: relative;
    z-index: 5;
  }}

  .pill-badge {{
    font-size: 13px;
    background: rgba(0,0,0,0.72);
    backdrop-filter: blur(10px);
    padding: 8px 18px;
    border-radius: 100px;
    border: 1px solid rgba(212,175,55,0.35);
    color: #FFF0BE;
    font-weight: 500;
  }}

  .footer-cta {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
    margin-top: auto;
    padding-top: 18px;
  }}
  .btn-dm {{
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 14px 30px;
    background: linear-gradient(135deg, #D4AF37 0%, #AA8222 100%);
    color: #18091E;
    font-weight: 700;
    font-size: 16px;
    border-radius: 100px;
    letter-spacing: 0.05em;
    box-shadow: 0 10px 25px rgba(212,175,55,0.35);
  }}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- 1. STATİK İLAN: KAHVERENGİ NATUREL İPEK KİRPİK -->
<!-- ========================================== -->
<div class="ad-canvas" id="ad_statik_kahve">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">📍 Ataşehir • Uphill Towers</div>
  </div>

  <div style="margin-top: 36px; position: relative; z-index: 10;">
    <span style="font-size: 14px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 12px;">
      Sessiz Lüks • Butik İpek Kirpik
    </span>
    <h1 class="serif-title" style="font-size: 58px; margin-bottom: 14px;">
      Siyah Kirpiğin Sertliğini Sevmeyenlere: <br/>
      <span class="gold-gradient-text">Kahverengi Naturel İpek Kirpik</span>
    </h1>
    <p style="font-size: 19px; line-height: 1.45; color: #DDD8CF; font-weight: 300;">
      Kendi kirpiğinizle kusursuz bütünleşen, göz kapağında sıfır ağırlık hissiyle sabahları rimelsiz dinlenmiş bakışlar.
    </p>
  </div>

  <!-- Fotoğraf Vitrini -->
  <div style="flex: 1; margin: 26px 0 22px 0; border-radius: 22px; overflow: hidden; border: 1px solid rgba(212,175,55,0.4); position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
    <img src="{macro_lash_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 38%;">
    <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(24,9,30,0.92) 100%);"></div>
    <div style="position: absolute; bottom: 20px; left: 24px; display: flex; gap: 10px; flex-wrap: wrap;">
      <span class="pill-badge">✨ Sıcak Moka & Espresso Tonları</span>
      <span class="pill-badge">🌿 0.07 mm Ultra İnce Lifler</span>
      <span class="pill-badge">🛡️ Medikal Hipoalerjenik Konfor</span>
    </div>
  </div>

  <div class="footer-cta">
    <div>
      <div style="font-size: 14px; color: #FFF0BE; font-weight: 600; margin-bottom: 4px;">UPHILL TOWERS B BLOK D:14</div>
      <div style="font-size: 13px; color: #AA8222;">WhatsApp VIP: 0531 869 67 64</div>
    </div>
    <div class="btn-dm">
      <span>Randevu & Analiz: DM</span>
      <span>➔</span>
    </div>
  </div>
</div>


<!-- ========================================== -->
<!-- 2. KARŞILAŞTIRMA İLANI: CAT EYE MI, WISPY Mİ? -->
<!-- ========================================== -->
<div class="ad-canvas" id="ad_karsilastirma">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">Göz Mimari Analizi</div>
  </div>

  <div style="margin-top: 30px; text-align: center; position: relative; z-index: 10;">
    <span style="font-size: 14px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 10px;">
      Göz Kapağınıza Hangisi Yakışır?
    </span>
    <h1 class="serif-title" style="font-size: 58px; margin-bottom: 12px;">
      <span class="gold-gradient-text">Cat Eye</span> mı, yoksa <span class="gold-gradient-text">Wispy</span> mi?
    </h1>
    <p style="font-size: 18px; color: #DDD8CF; font-weight: 300;">
      Kirpikte tek bir kalıp yoktur. Bakışınızın ifadesini milimetrik tasarlıyoruz.
    </p>
  </div>

  <!-- Karşılaştırma Grid -->
  <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 26px 0;">
    
    <!-- Kart 1: Cat Eye -->
    <div class="glass-card" style="display: flex; flex-direction: column; padding: 18px;">
      <div style="height: 380px; border-radius: 16px; overflow: hidden; border: 1px solid rgba(212,175,55,0.3); margin-bottom: 16px; position: relative;">
        <img src="{cateye_lash_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 30%;">
        <div style="position: absolute; top: 12px; left: 12px;" class="pill-badge">Lifting Etkisi</div>
      </div>
      <h3 class="serif-title" style="font-size: 32px; color: #FFF0BE; margin-bottom: 6px;">Cat Eye Tasarım</h3>
      <p style="font-size: 15px; color: #DDD8CF; line-height: 1.45; font-weight: 300;">
        Dış köşelere doğru uzayan kanat etkisi. Düşük göz kapağını anında yukarı çeken, çekik ve eyeliner görünümlü stil.
      </p>
    </div>

    <!-- Kart 2: Wispy -->
    <div class="glass-card" style="display: flex; flex-direction: column; padding: 18px;">
      <div style="height: 380px; border-radius: 16px; overflow: hidden; border: 1px solid rgba(212,175,55,0.3); margin-bottom: 16px; position: relative;">
        <img src="{macro_lash_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 38%;">
        <div style="position: absolute; top: 12px; left: 12px;" class="pill-badge">Doğal & Tülümsü</div>
      </div>
      <h3 class="serif-title" style="font-size: 32px; color: #FFF0BE; margin-bottom: 6px;">Wispy Naturel</h3>
      <p style="font-size: 15px; color: #DDD8CF; line-height: 1.45; font-weight: 300;">
        Farklı uzunluklarla oluşturulan katmanlı doku. Günlük kullanımda rimelli, yumuşak ve tamamen doğal duruş.
      </p>
    </div>

  </div>

  <div class="footer-cta">
    <div style="font-size: 15px; color: #DDD8CF;">
      📷 <strong style="color: #FFF0BE;">Kararsızsanız:</strong> DM'den göz fotoğrafınızı atın, modeli birlikte belirleyelim.
    </div>
    <div class="btn-dm">
      <span>Fotoğraf Gönder: DM</span>
      <span>➔</span>
    </div>
  </div>
</div>


<!-- ========================================== -->
<!-- 3. CAROUSEL SLAYT 1 (KAPAK) -->
<!-- ========================================== -->
<div class="ad-canvas" id="carousel_slide_1">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">📍 Ataşehir • Uphill Towers</div>
  </div>

  <div style="margin-top: 40px; position: relative; z-index: 10;">
    <span style="font-size: 15px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 14px;">
      Rehber • İpek Kirpik Sanatı
    </span>
    <h1 class="serif-title" style="font-size: 62px; margin-bottom: 18px;">
      Sabahları Alarmı 5 Kez Erteleyip <br/>
      <span class="gold-gradient-text">Rimelle Savaşmaktan</span> Yorulmadınız mı? 😴
    </h1>
    <p style="font-size: 21px; line-height: 1.5; color: #DDD8CF; font-weight: 300;">
      Ataşehir Uphill Towers'ta göz yapınıza özel tasarlanan hafif, batmayan ve 4-6 hafta kalıcı ipek kirpik mimarisi.
    </p>
  </div>

  <div style="flex: 1; margin: 30px 0 24px 0; border-radius: 22px; overflow: hidden; border: 1px solid rgba(212,175,55,0.4); position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
    <img src="{macro_lash_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 38%;">
    <div style="position: absolute; bottom: 20px; left: 24px; display: flex; gap: 10px;">
      <span class="pill-badge">✨ Naturel Doku</span>
      <span class="pill-badge">🌿 Sıfır Yanma Garantisi</span>
    </div>
  </div>

  <div class="footer-cta">
    <span style="font-size: 15px; color: #AA8222; font-weight: 600; letter-spacing: 0.15em;">01 / 04</span>
    <div style="display: flex; align-items: center; gap: 10px; padding: 12px 26px; border: 1px solid rgba(212,175,55,0.4); border-radius: 100px; color: #FFF0BE; font-size: 15px; font-weight: 600;">
      <span>Keşfetmek İçin Kaydırın</span>
      <span>➔</span>
    </div>
  </div>
</div>


<!-- ========================================== -->
<!-- 4. CAROUSEL SLAYT 2 (HAFİFLİK & DOĞALLIK) -->
<!-- ========================================== -->
<div class="ad-canvas" id="carousel_slide_2">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">Adım 01 • Konfor</div>
  </div>

  <div style="margin-top: 36px; margin-bottom: 24px; position: relative; z-index: 10;">
    <h2 class="serif-title" style="font-size: 54px; margin-bottom: 12px;">
      Kendi Kirpiğiniz Gibi <span class="gold-gradient-text">Hafif & Güvenli</span>
    </h2>
    <p style="font-size: 19px; line-height: 1.45; color: #DDD8CF; font-weight: 300;">
      Ağırlaşan, göz kapağını yoran veya dökülme yapan eski usul kalın kirpikleri unutun.
    </p>
  </div>

  <div style="height: 380px; border-radius: 20px; overflow: hidden; border: 1px solid rgba(212,175,55,0.35); margin-bottom: 24px;">
    <img src="{cateye_lash_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 30%;">
  </div>

  <div class="glass-card" style="flex: 1; display: flex; flex-direction: column; justify-content: space-around;">
    <div style="display: flex; gap: 16px; align-items: flex-start;">
      <div style="width: 38px; height: 38px; border-radius: 50%; background: rgba(212,175,55,0.2); border: 1px solid rgba(212,175,55,0.4); display: flex; align-items: center; justify-content: center; color: #FFF0BE; font-size: 18px; flex-shrink: 0;">01</div>
      <div>
        <h4 style="font-size: 20px; color: #FFF0BE; margin-bottom: 4px;">0.07 mm Ultra İnce İpek Lifler</h4>
        <p style="font-size: 15px; color: #DDD8CF; line-height: 1.4;">Doğal kirpiğinize sıfır yük bindirir, gözünüzde ağırlık veya batma hissettirmez.</p>
      </div>
    </div>
    <div style="display: flex; gap: 16px; align-items: flex-start;">
      <div style="width: 38px; height: 38px; border-radius: 50%; background: rgba(212,175,55,0.2); border: 1px solid rgba(212,175,55,0.4); display: flex; align-items: center; justify-content: center; color: #FFF0BE; font-size: 18px; flex-shrink: 0;">02</div>
      <div>
        <h4 style="font-size: 20px; color: #FFF0BE; margin-bottom: 4px;">Medikal Hipoalerjenik Yapıştırıcı</h4>
        <p style="font-size: 15px; color: #DDD8CF; line-height: 1.4;">Hassas gözlerde sulanma ve kızarıklık yapmaz; kontakt lens kullananlar için %100 konforludur.</p>
      </div>
    </div>
  </div>

  <div class="footer-cta">
    <span style="font-size: 15px; color: #AA8222; font-weight: 600; letter-spacing: 0.15em;">02 / 04</span>
    <span style="font-size: 14px; color: #FFF0BE;">Kaydırın ➔</span>
  </div>
</div>


<!-- ========================================== -->
<!-- 5. CAROUSEL SLAYT 3 (BROWN LASHES TRENDİ) -->
<!-- ========================================== -->
<div class="ad-canvas" id="carousel_slide_3">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">Adım 02 • Renk & Ton</div>
  </div>

  <div style="margin-top: 36px; margin-bottom: 24px; position: relative; z-index: 10;">
    <h2 class="serif-title" style="font-size: 54px; margin-bottom: 12px;">
      Brown Lashes: <span class="gold-gradient-text">Zarif & Buğulu Derinlik</span>
    </h2>
    <p style="font-size: 19px; line-height: 1.45; color: #DDD8CF; font-weight: 300;">
      Özellikle sarışın, kumral ve açık tenli danışanlarımızın vazgeçilmezi.
    </p>
  </div>

  <div style="height: 380px; border-radius: 20px; overflow: hidden; border: 1px solid rgba(212,175,55,0.35); margin-bottom: 24px;">
    <img src="{lash_perfect_path}" style="width: 100%; height: 100%; object-fit: cover; object-position: center 30%;">
  </div>

  <div class="glass-card" style="flex: 1; display: flex; flex-direction: column; justify-content: space-around;">
    <div style="display: flex; gap: 16px; align-items: flex-start;">
      <div style="width: 38px; height: 38px; border-radius: 50%; background: rgba(212,175,55,0.2); border: 1px solid rgba(212,175,55,0.4); display: flex; align-items: center; justify-content: center; color: #FFF0BE; font-size: 18px; flex-shrink: 0;">✦</div>
      <div>
        <h4 style="font-size: 20px; color: #FFF0BE; margin-bottom: 4px;">Siyahın Sertliğini Kırar</h4>
        <p style="font-size: 15px; color: #DDD8CF; line-height: 1.4;">Gözü kısıp yapay gösteren sert siyah kontrast yerine sıcak moka ışıltısı verir.</p>
      </div>
    </div>
    <div style="display: flex; gap: 16px; align-items: flex-start;">
      <div style="width: 38px; height: 38px; border-radius: 50%; background: rgba(212,175,55,0.2); border: 1px solid rgba(212,175,55,0.4); display: flex; align-items: center; justify-content: center; color: #FFF0BE; font-size: 18px; flex-shrink: 0;">✦</div>
      <div>
        <h4 style="font-size: 20px; color: #FFF0BE; margin-bottom: 4px;">Sessiz Lüks Estetiği</h4>
        <p style="font-size: 15px; color: #DDD8CF; line-height: 1.4;">Makyajsızken bile 'kendi kirpiği bu kadar gür ve uzun' dedirten incelik.</p>
      </div>
    </div>
  </div>

  <div class="footer-cta">
    <span style="font-size: 15px; color: #AA8222; font-weight: 600; letter-spacing: 0.15em;">03 / 04</span>
    <span style="font-size: 14px; color: #FFF0BE;">Kaydırın ➔</span>
  </div>
</div>


<!-- ========================================== -->
<!-- 6. CAROUSEL SLAYT 4 (VIP SÜİT & KİLİT CTA) -->
<!-- ========================================== -->
<div class="ad-canvas" id="carousel_slide_4">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <img src="{logo_path}" class="logo-img">
    <div class="location-pill">Ayrıcalıklı Randevu</div>
  </div>

  <div style="margin-top: 40px; text-align: center; position: relative; z-index: 10;">
    <span style="font-size: 15px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; display: block; margin-bottom: 12px;">
      Ataşehir Uphill Towers 14. Kat
    </span>
    <h1 class="serif-title" style="font-size: 58px; margin-bottom: 16px;">
      Sakin, Butik ve <br/>
      <span class="gold-gradient-text">Yalnızca Size Özel Seans</span>
    </h1>
    <p style="font-size: 20px; color: #DDD8CF; line-height: 1.5; font-weight: 300; max-width: 820px; margin: 0 auto;">
      Günde sınırlı sayıda VIP misafir kabul ediyoruz. Kalabalık salon gürültüsü yok; kahvenizi yudumlarken 75 dakikada taze bir ifade.
    </p>
  </div>

  <div class="glass-card" style="margin: 36px 0; padding: 34px; text-align: center;">
    <h3 class="serif-title" style="font-size: 34px; color: #FFF0BE; margin-bottom: 14px;">
      Bu Haftaki Müsait Saatler İçin:
    </h3>
    <p style="font-size: 18px; color: #DDD8CF; margin-bottom: 24px; font-weight: 300;">
      DM üzerinden göz yapınızı belirtebilir veya WhatsApp VIP hattımızdan doğrudan Gülşah Hanım'a ulaşabilirsiniz.
    </p>
    <div style="display: inline-flex; align-items: center; gap: 12px; padding: 16px 36px; background: linear-gradient(135deg, #D4AF37 0%, #AA8222 100%); color: #18091E; font-weight: 700; font-size: 18px; border-radius: 100px; box-shadow: 0 12px 30px rgba(212,175,55,0.4);">
      <span>Randevu İçin: DM Gönderin 🌸</span>
    </div>
  </div>

  <div style="text-align: center; margin-top: auto; position: relative; z-index: 10;">
    <div style="font-size: 15px; color: #FFF0BE; font-weight: 600; margin-bottom: 4px;">📍 Barbaros Mah. Uphill Towers B Blok D:14 • Ataşehir</div>
    <div style="font-size: 14px; color: #AA8222;">☎️ WhatsApp VIP: 0531 869 67 64 &bull; Instagram: @linail.beautystudio</div>
  </div>
</div>

</body>
</html>
"""

html_file = os.path.join(output_dir, "creatives_canvas.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created HTML template: {html_file}")

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        await page.goto(f"file://{html_file}")
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(1)

        targets = [
            ("ad_statik_kahve", "01_STATIK_KAHVERENGI_IPEK_KIRPIK.png"),
            ("ad_karsilastirma", "02_KARSILASTIRMA_CATEYE_WISPY.png"),
            ("carousel_slide_1", "CAROUSEL_SLIDE_1.png"),
            ("carousel_slide_2", "CAROUSEL_SLIDE_2.png"),
            ("carousel_slide_3", "CAROUSEL_SLIDE_3.png"),
            ("carousel_slide_4", "CAROUSEL_SLIDE_4.png"),
        ]

        for elem_id, filename in targets:
            elem = page.locator(f"#{elem_id}")
            out_path = os.path.join(output_dir, filename)
            await elem.screenshot(path=out_path)
            print(f"Rendered: {out_path} ({os.path.getsize(out_path)} bytes)")

        await browser.close()

asyncio.run(render())
