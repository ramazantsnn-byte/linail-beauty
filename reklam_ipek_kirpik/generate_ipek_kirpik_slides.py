import os
import asyncio
from playwright.async_api import async_playwright

output_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
os.makedirs(output_dir, exist_ok=True)

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #000;
    font-family: 'Montserrat', sans-serif;
    color: #FAF8F5;
    -webkit-font-smoothing: antialiased;
  }
  .slide {
    width: 1080px;
    height: 1350px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(160deg, #18091E 0%, #2A1136 45%, #13051A 100%);
    display: flex;
    flex-direction: column;
    padding: 70px 70px 60px 70px;
  }
  
  /* Background subtle luxury glow */
  .glow-top-right {
    position: absolute;
    top: -150px;
    right: -150px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(212,175,55,0.20) 0%, rgba(62,27,71,0) 70%);
    pointer-events: none;
  }
  .glow-bottom-left {
    position: absolute;
    bottom: -150px;
    left: -150px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(142,68,173,0.25) 0%, rgba(20,5,27,0) 70%);
    pointer-events: none;
  }
  .gold-border {
    position: absolute;
    inset: 24px;
    border: 1px solid rgba(212,175,55,0.32);
    pointer-events: none;
    border-radius: 28px;
  }
  .gold-border::after {
    content: '';
    position: absolute;
    inset: 8px;
    border: 1px solid rgba(212,175,55,0.12);
    border-radius: 20px;
  }

  /* Header */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
    padding-bottom: 25px;
    border-bottom: 1px solid rgba(212,175,55,0.25);
  }
  .logo-box {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .logo-img {
    height: 46px;
    object-fit: contain;
  }
  .location-pill {
    font-size: 14px;
    padding: 9px 20px;
    background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.35);
    border-radius: 100px;
    color: #FFF0BE;
    letter-spacing: 0.1em;
    font-weight: 500;
  }

  /* Typography */
  .serif-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    line-height: 1.12;
    color: #FAF8F5;
  }
  .gold-gradient-text {
    background: linear-gradient(135deg, #FFF0BE 0%, #D4AF37 50%, #AA8222 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  /* Glass Card */
  .glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 24px;
    padding: 32px 36px;
    position: relative;
    z-index: 5;
  }

  /* Bullet item */
  .bullet-item {
    display: flex;
    align-items: flex-start;
    gap: 18px;
    margin-bottom: 22px;
  }
  .bullet-item:last-child { margin-bottom: 0; }
  .bullet-icon {
    width: 42px;
    height: 42px;
    background: rgba(212,175,55,0.18);
    border: 1px solid rgba(212,175,55,0.45);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 19px;
    color: #FFF0BE;
  }
  .bullet-text h4 {
    font-size: 21px;
    font-weight: 600;
    color: #FFF0BE;
    margin-bottom: 5px;
  }
  .bullet-text p {
    font-size: 17px;
    font-weight: 300;
    line-height: 1.5;
    color: #E6E2DB;
  }

  .swipe-tag {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 14px 28px;
    background: linear-gradient(135deg, rgba(212,175,55,0.22) 0%, rgba(212,175,55,0.06) 100%);
    border: 1px solid rgba(212,175,55,0.45);
    border-radius: 100px;
    font-size: 16px;
    font-weight: 600;
    color: #FFF0BE;
    letter-spacing: 0.15em;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<!-- SLIDE 1: KAPAK (HERO HOOK) -->
<div class="slide" id="slide1">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <div class="logo-box">
      <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/linail_full_logo_clean.png" class="logo-img">
    </div>
    <div class="location-pill">📍 Ataşehir Uphill Towers</div>
  </div>

  <div style="margin-top: 42px; position: relative; z-index: 10;">
    <span style="display:inline-block; font-size: 15px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; margin-bottom: 16px;">
      Sessiz Lüks • Butik İpek Kirpik
    </span>
    <h1 class="serif-title" style="font-size: 64px; margin-bottom: 20px;">
      Gözlerinizin Doğal Işıltısını Ortaya Çıkaran <span class="gold-gradient-text">Ağırlıksız</span> Zarafet.
    </h1>
    <p style="font-size: 21px; line-height: 1.5; color: #DDD8CF; font-weight: 300; max-width: 880px;">
      Kendi kirpiğinizle kusursuz bütünleşen, sabahları zahmetsizce dinlenmiş ve taze bakışlar sunan <strong style="color: #FFF0BE; font-weight: 600;">Kahverengi Naturel İpek Kirpik Tasarımı.</strong>
    </p>
  </div>

  <!-- Fotoğraf Vitrini -->
  <div style="flex: 1; margin: 35px 0 30px 0; border-radius: 24px; overflow: hidden; border: 1px solid rgba(212,175,55,0.4); position: relative; box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
    <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/lash_perfect.jpg" style="width: 100%; height: 100%; object-fit: cover; object-position: center 30%;">
    <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(24,9,30,0.85) 100%);"></div>
    <div style="position: absolute; bottom: 24px; left: 30px; display: flex; gap: 12px;">
      <span style="font-size: 14px; background: rgba(0,0,0,0.7); backdrop-filter: blur(10px); padding: 8px 18px; border-radius: 100px; border: 1px solid rgba(212,175,55,0.3); color: #FFF0BE; font-weight: 500;">✨ Naturel Kahve Doku</span>
      <span style="font-size: 14px; background: rgba(0,0,0,0.7); backdrop-filter: blur(10px); padding: 8px 18px; border-radius: 100px; border: 1px solid rgba(212,175,55,0.3); color: #FFF0BE; font-weight: 500;">🌿 Sıfır Ağırlık Hissi</span>
    </div>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 10;">
    <span style="font-size: 15px; color: #AA8222; letter-spacing: 0.15em; font-weight: 600;">01 / 04</span>
    <div class="swipe-tag">
      <span>Keşfetmek İçin Kaydırın</span>
      <span style="font-size: 18px;">→</span>
    </div>
  </div>
</div>

<!-- SLIDE 2: AHENK & DOKU -->
<div class="slide" id="slide2">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <div class="logo-box">
      <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/linail_full_logo_clean.png" class="logo-img">
    </div>
    <div class="location-pill">Adım 01 • Doku & Ahenk</div>
  </div>

  <div style="margin-top: 36px; margin-bottom: 28px; position: relative; z-index: 10;">
    <h2 class="serif-title" style="font-size: 52px; margin-bottom: 14px;">
      Neden <span class="gold-gradient-text">Kahve İpek Dokunuş?</span>
    </h2>
    <p style="font-size: 20px; line-height: 1.45; color: #DDD8CF; font-weight: 300;">
      Ten renginize ve göz renginize sıcak bir ahenk katarak çaba harcanmamış bir duruluk yaratır.
    </p>
  </div>

  <div style="height: 380px; border-radius: 22px; overflow: hidden; border: 1px solid rgba(212,175,55,0.35); margin-bottom: 30px; position: relative;">
    <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/ipek_kirpik_centered.jpg" style="width: 100%; height: 100%; object-fit: cover;">
  </div>

  <div class="glass-card" style="flex: 1;">
    <div class="bullet-item">
      <div class="bullet-icon">✦</div>
      <div class="bullet-text">
        <h4>Sıcak & Zarif Geçiş</h4>
        <p>Güneş ışığında göz renginizi derinleştiren ve yapaylık hissi vermeyen tüy kadar hafif lifler.</p>
      </div>
    </div>
    <div class="bullet-item">
      <div class="bullet-icon">✦</div>
      <div class="bullet-text">
        <h4>Kendi Kirpiğinizi Koruyan Yapı</h4>
        <p>Ağırlık yapmayan medikal standarttaki ipek lifler, doğal kirpiğinizin nefes almasını ve sağlıklı uzamasını sağlar.</p>
      </div>
    </div>
    <div class="bullet-item">
      <div class="bullet-icon">✦</div>
      <div class="bullet-text">
        <h4>Sabahları Zahmetsiz Güzellik</h4>
        <p>Her sabah makyaj yapma ihtiyacı duymadan, aynaya baktığınızda taze ve canlı bakışlar.</p>
      </div>
    </div>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 25px; position: relative; z-index: 10;">
    <span style="font-size: 15px; color: #AA8222; letter-spacing: 0.15em; font-weight: 600;">02 / 04</span>
    <div class="swipe-tag">
      <span>Devamını Görün</span>
      <span style="font-size: 18px;">→</span>
    </div>
  </div>
</div>

<!-- SLIDE 3: ZANAAT & VIP DENEYİMİ -->
<div class="slide" id="slide3">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <div class="logo-box">
      <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/linail_full_logo_clean.png" class="logo-img">
    </div>
    <div class="location-pill">Adım 02 • Butik Standart</div>
  </div>

  <div style="margin-top: 36px; margin-bottom: 28px; position: relative; z-index: 10;">
    <h2 class="serif-title" style="font-size: 52px; margin-bottom: 14px;">
      Gülşah Taşan <span class="gold-gradient-text">Ustalığıyla.</span>
    </h2>
    <p style="font-size: 20px; line-height: 1.45; color: #DDD8CF; font-weight: 300;">
      Fabrikasyon değil; göz yapınızın milimetrik açısına göre tek tek şekillendirilen kişiye özel mimari.
    </p>
  </div>

  <div style="height: 380px; border-radius: 22px; overflow: hidden; border: 1px solid rgba(212,175,55,0.35); margin-bottom: 30px; position: relative;">
    <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/services/service_ipek_kirpik.jpg" style="width: 100%; height: 100%; object-fit: cover;">
  </div>

  <div class="glass-card" style="flex: 1;">
    <div class="bullet-item">
      <div class="bullet-icon">✓</div>
      <div class="bullet-text">
        <h4>Milimetrik Açı Hesaplaması</h4>
        <p>Göz kapağınızın düşüklüğü ve göz pınarınızın açısı analiz edilerek en ideal kıvrım ve uzunluk belirlenir.</p>
      </div>
    </div>
    <div class="bullet-item">
      <div class="bullet-icon">✓</div>
      <div class="bullet-text">
        <h4>Hipoalerjenik & Medikal Hijyen</h4>
        <p>Hassas gözler için özel formüle edilmiş tıbbi yapıştırıcı ve tek kullanımlık steril çalışma ortamı.</p>
      </div>
    </div>
    <div class="bullet-item">
      <div class="bullet-icon">✓</div>
      <div class="bullet-text">
        <h4>Sakin VIP Stüdyo Huzuru</h4>
        <p>Sıra beklemeden, gürültüden uzak, tamamen size ayrılmış konforlu bir kabin ortamı.</p>
      </div>
    </div>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 25px; position: relative; z-index: 10;">
    <span style="font-size: 15px; color: #AA8222; letter-spacing: 0.15em; font-weight: 600;">03 / 04</span>
    <div class="swipe-tag">
      <span>Randevu Detayı</span>
      <span style="font-size: 18px;">→</span>
    </div>
  </div>
</div>

<!-- SLIDE 4: KAPANIŞ & WHATSAPP ÇAĞRISI -->
<div class="slide" id="slide4">
  <div class="gold-border"></div>
  <div class="glow-top-right"></div>
  <div class="glow-bottom-left"></div>

  <div class="header">
    <div class="logo-box">
      <img src="file:///Users/applesupport/Desktop/linail%20beauty/assets/linail_full_logo_clean.png" class="logo-img">
    </div>
    <div class="location-pill">📍 Ataşehir Uphill Towers</div>
  </div>

  <div style="margin-top: 45px; text-align: center; position: relative; z-index: 10;">
    <span style="display:inline-block; font-size: 15px; letter-spacing: 0.3em; text-transform: uppercase; color: #D4AF37; font-weight: 600; margin-bottom: 16px;">
      Özel Randevu Planlaması
    </span>
    <h2 class="serif-title" style="font-size: 60px; margin-bottom: 18px;">
      Ataşehir'de Sakin Bir <br><span class="gold-gradient-text">Güzellik Molası.</span>
    </h2>
    <p style="font-size: 21px; line-height: 1.5; color: #DDD8CF; font-weight: 300; max-width: 750px; margin: 0 auto;">
      Gülşah Taşan ile kahvenizi yudumlarken, tamamen size ayrılmış huzurlu bir seans için yerinizi ayırtın.
    </p>
  </div>

  <div class="glass-card" style="margin: 45px 0; text-align: center; padding: 40px;">
    <div style="font-size: 18px; color: #D4AF37; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; font-weight: 600;">
      LİNAİL BEAUTY STUDIO
    </div>
    <div style="font-size: 24px; color: #FAF8F5; font-weight: 500; margin-bottom: 24px;">
      Uphill Towers B Blok Daire 14 • Ataşehir
    </div>
    <div style="height: 1px; background: rgba(212,175,55,0.25); width: 80%; margin: 0 auto 24px auto;"></div>
    <p style="font-size: 18px; color: #DDD8CF; line-height: 1.6; font-weight: 300;">
      Kişiye özel tasarım ve sakin stüdyo deneyimi için seanslarımız randevu ile planlanmaktadır.
    </p>
    <div style="display: inline-flex; align-items: center; gap: 12px; margin-top: 24px; background: rgba(212,175,55,0.18); border: 1px solid rgba(212,175,55,0.45); padding: 14px 28px; border-radius: 100px;">
      <span style="font-size: 20px;">💬</span>
      <span style="font-size: 18px; font-weight: 600; color: #FFF0BE; letter-spacing: 0.05em;">WhatsApp: 0531 869 67 64</span>
    </div>
  </div>

  <div style="background: linear-gradient(135deg, #D4AF37 0%, #AA8222 100%); border-radius: 20px; padding: 26px; text-align: center; margin-top: auto; position: relative; z-index: 10; box-shadow: 0 15px 35px rgba(212,175,55,0.25);">
    <h3 style="font-size: 24px; color: #18091E; font-weight: 700; margin-bottom: 6px;">
      Bu Haftaki Müsait Seansları Öğrenin
    </h3>
    <p style="font-size: 17px; color: #2A1136; font-weight: 500;">
      Aşağıdaki "WhatsApp'ta Mesaj Gönder" butonuna tıklayarak doğrudan bilgi alabilirsiniz.
    </p>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 25px; position: relative; z-index: 10;">
    <span style="font-size: 15px; color: #AA8222; letter-spacing: 0.15em; font-weight: 600;">04 / 04</span>
    <span style="font-size: 14px; color: #D4AF37; letter-spacing: 0.1em; font-weight: 500;">Linail Beauty Studio • 2026</span>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(output_dir, "slides.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(f"file://{html_path}")
        await page.wait_for_timeout(1000)
        
        for i in range(1, 5):
            slide_el = await page.query_selector(f"#slide{i}")
            if slide_el:
                out_png = os.path.join(output_dir, f"slide_{i}.png")
                await slide_el.screenshot(path=out_png)
                print(f"Rendered: {out_png}")
        await browser.close()

asyncio.run(render())
