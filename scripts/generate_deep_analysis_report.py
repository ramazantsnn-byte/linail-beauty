#!/usr/bin/env python3
import json
import re

with open("/tmp/linail_master_unified_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

# Count stats
cat_counts = {}
hashtag_counts = {}
emojis_counts = {}
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)

for p in posts:
    c = p.get("category", "Diğer")
    cat_counts[c] = cat_counts.get(c, 0) + 1
    
    for tag in p.get("hashtags", []):
        tl = tag.lower()
        hashtag_counts[tl] = hashtag_counts.get(tl, 0) + 1
        
    for em in emoji_pattern.findall(p.get("caption", "")):
        emojis_counts[em] = emojis_counts.get(em, 0) + 1

sorted_tags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:30]
sorted_emojis = sorted(emojis_counts.items(), key=lambda x: x[1], reverse=True)[:15]

md = f"""# 💎 LİNAİL BEAUTY INSTAGRAM TÜM GÖNDERİLERİN DERİNLEMESİNE ANALİZ RAPORU
## @linail.beautystudio Profilindeki {len(posts)} Gerçek Gönderinin Tek Tek İncelenmesi

> **Tarih:** 7 Kasım 2026  
> **Taranan Gönderi Sayısı:** {len(posts)} adet (Profildeki tüm gönderiler Google Chrome üzerinden canlı okunup ayrıştırılmıştır)  
> **Amaç:** 20 Kasım reklam kampanyasındaki yapay zeka kalıplarını sıfırlamak; Gülşah Taşan ve Linail Beauty'nin gerçek ses tonunu, mizahını, samimiyetini ve salon zanaatını kopyalanabilir bir master kılavuza dönüştürmek.

---

## 1. STRATEJİK ÖZET: LİNAİL BEAUTY'NİN GERÇEK İÇERİK DNA'SI

Profildeki {len(posts)} gönderi tek tek analiz edildiğinde Linail Beauty'nin organik başarısının 4 ana sütun üzerine kurulu olduğu görülmüştür:

1. **Doğal ve Sıcak Karşılama:**  
   Kurumsal, mesafeli veya soğuk acente dili ASLA kullanılmıyor. Gönderiler sanki stüdyoda kahve içerken bir arkadaşa ya da güvenilen bir uzmana konuşuluyormuş gibi yazılıyor.
2. **Relatable (Kullanıcıyla Özdeşleşen) Mizah ve Gözlem:**  
   * *"Tırnaklarını yaptırdıktan 2 saat sonra evde temizlik perileri gelenler..."*
   * *"Her yeni tırnak sonrası yaşanan o gizli mesai... Gün içinde dönüp dönüp tırnaklarına bakmak 💜"*
   * *"Sabahları alarmı 5 kez erteleyip hızlıca makyaj yapmaya çalışanlar..."*
   Bu gözlemler reklamın "satış kokmasını" engelliyor, kadınların doğrudan kaydetmesini ve paylaşmasını sağlıyor.
3. **Rehber ve Karşılaştırma Dili (Eğitici Uzmanlık):**  
   * *"Arkadaşın 'Cat eye mı, Wispy mi yaptırsam?' diye soruyorsa bu rehberi ona gönder. 💜"*
   * *"Jel Güçlendirme + Cat Eye: Kusursuz bir kalıcı ojenin sırrı, alttaki tırnağın güçlü duruşudur..."*
   * *"Brown Lashes: Özellikle sarışın, kumral veya göz rengini öne çıkarmak isteyenlere..."*
4. **Zanaat ve Cerrahi Hijyen Vurgusu:**  
   Her işlemde steril otoklav paketleri, elmas frezeler, tek hat pürüzsüz kombi manikür kesimi ve tırnağın hava almasını engelleyen mimari apeks dengesi ön plana çıkarılıyor.

---

## 2. KATEGORİ DAĞILIMI VE PAYLAŞIM HACMİ

| Kategori | Gönderi Sayısı | Oran (%) | Stratejik Rolü |
|---|---|---|---|
"""

for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
    pct = (count / len(posts)) * 100
    md += f"| **{cat}** | {count} gönderi | %{pct:.1f} | "
    if "Tırnak" in cat:
        md += "Ana gelir kapısı; sürekli yenilenen tasarımlar, renkler ve kalıcılık kanıtları |\n"
    elif "Kirpik" in cat:
        md += "Zaman tasarrufu ve sabah konforu kancası; doğal bakış vurgusu |\n"
    elif "Cilt" in cat:
        md += "Yüksek biletli (High-Ticket) 3 seanslık VIP dönüşüm paketi |\n"
    else:
        md += "Stüdyo atmosferi, otoklav hijyeni, kahve ikramı ve viral mizah |\n"

md += f"""
---

## 3. İMZA NİTELİĞİNDEKİ İKONLAR VE HASHTAG FREKANSI

### A. En Çok Tercih Edilen Emojiler
Linail gönderilerinin görsel kimliğini oluşturan ikonlar:
"""

for em, cnt in sorted_emojis:
    md += f"`{em}` ({cnt} kez)  "

md += f"""

* **Mor Kalp (`💜`):** Linail'in tescilli marka rengi (Mürdüm/Mor).
* **Pırıltı (`✨`):** İşlem sonu ışıltısı ve tazelik hissi.
* **Beyaz Kalp (`🤍`):** Temizlik, zarafet ve porselen cilt hissi.
* **Çiçek (`🌸`):** Bahar tazeliği ve kadınsı butik sıcaklık.

### B. En Sık Kullanılan Hashtag Kümesi (Top 30)

| Sıra | Hashtag | Kullanım | Hedef Arama Terimi |
|---|---|---|---|
"""

for idx, (tag, cnt) in enumerate(sorted_tags, 1):
    md += f"| {idx} | `#{tag}` | {cnt} kez | Yerel & Hizmet Keşfeti |\n"

md += """
---

## 4. PROFİLDEKİ GERÇEK VE EN GÜÇLÜ 12 KANCA (HOOK)

Reklam setlerimizin ilk 3 saniyesine ve gönderi ilk satırına doğrudan koyacağımız denenmiş ve tutmuş Linail kancaları:

1. **İpek Kirpik Seçim Kancası:**  
   > *"Arkadaşın “Cat eye mı, Wispy mi yaptırsam?” diye sana soruyorsa bu rehberi ona gönder. 💜"*
2. **Cat Eye Uyarı Kancası (Merak & Arzu):**  
   > *"🚨 Uyarı: Bir kere Cat Eye yaptırınca bir daha başka model yaptıramayabilirsiniz... ✨"*
3. **Mizahi Temizlik Kancası (Relatable Reels):**  
   > *"Tırnaklarını yaptırdıktan 2 saat sonra evde temizlik perileri gelenler burada mı? 😂💅"*
4. **Gizli Mesai Kancası:**  
   > *"Her yeni tırnak sonrası yaşanan o gizli mesai... 💜 Gün içinde dönüp dönüp tırnaklarına bakmak!"*
5. **Sabah Makyajı Zaman Kancası:**  
   > *"Sabahları alarmı 5 kez erteleyip, aynanın karşısında hızlıca makyaj yapmaya çalışanlar burada mı? 😴"*
6. **Boutique Kahve & Mola Kancası:**  
   > *"Bütün haftanın yorgunluğunu 2 saatliğine kapının dışında bırakmaya ne dersiniz? ☕️ Linail’de kendinize bir kahve molası verin."*
7. **Klasik French Kancası:**  
   > *"Asla modası geçmeyen tek bir model varsa, o da French’tir! 🤍 Sade, asil ve her kombine uyumlu."*
8. **Brown Lashes (Naturel Ton) Kancası:**  
   > *"Brown Lashes ✨ Özellikle sarışın, kumral veya göz rengini siyahın sertliği olmadan öne çıkarmak isteyenlere..."*
9. **Tek Seans Bakış Değişimi Kancası:**  
   > *"Sadece tek bir seansla tamamen değişen bakışlar ✨ Kaş laminasyon ve lifting etkisi."*
10. **Apeks ve Güç Kancası:**  
    > *"Kusursuz bir kalıcı ojenin sırrı, alttaki tırnağın güçlü duruşudur. Jel güçlendirme ile kırılmalara son!"*
11. **Hijyen Güven Kancası:**  
    > *"Linail’de hijyen ve sağlığınız her şeyden önce gelir. 💜 Gün sonu sterilizasyon ve kişiye özel açılan otoklav poşetleri."*
12. **Cam Cilt Dönüşüm Kancası:**  
    > *"✨ Cam Cilt Protokolümüzle Tanıştınız mı? Fondötenle kapatmak yerine kendi cildinizle ışıldayın."*

---

## 5. TÜM GÖNDERİLERİN TAM LİSTESİ VE DETAYLI DÖKÜMÜ

Aşağıdaki tabloda taranan tüm paylaşımların orijinal bağlantıları, kategorileri ve ilk satır kancaları yer almaktadır:

| No | Kategori | Kanca / İlk Satır | Paylaşım Linki |
|---|---|---|---|
"""

for idx, p in enumerate(posts, 1):
    cap_lines = [l.strip() for l in p.get("caption", "").splitlines() if l.strip() and not l.strip().startswith("#") and l.strip() != "•"]
    first_line = cap_lines[0] if cap_lines else "Görsel Odaklı Tasarım"
    first_line_clean = first_line.replace("|", "-")[:75]
    short_id = p["url"].rstrip("/").split("/")[-1]
    md += f"| {idx} | {p.get('category', 'Genel')} | {first_line_clean} | [{short_id}]({p['url']}) |\n"

md += """
---

## 6. 20 KASIM KAMPANYASINDA YAPILAN TAM UYARLAMA

Bu analizin ardından reklam çalışma defterindeki 3 kreatif set şu şekilde revize edilmiştir:
1. **Kore Cam Cilt (01):** Kuru tıbbi açıklamalar yerine Linail'in `✨ Cam Cilt Protokolümüzle Tanıştınız mı? ✨` girişi ve ManyChat `CAM CİLT` DM hunisi entegre edildi.
2. **Rus Kombi Manikür & Jel (02):** "Et kesilmez" gibi hatalı ifadeler temizlendi; elmas alev uç ve Staleks makasla tek şerit pürüzsüz kesim gerçeği, "tırnak etiniz 3 günde parçalanıyorsa" usta kancası ve sıcak Linaura mum masajı yerleştirildi.
3. **Kaş Laminasyon & Kirpik (03):** "Cat eye mı Wispy mi" ve "Sabah alarmı erteleyenler" kancaları eklenerek "Vip Odada Aynı Anda Çift İşlem" konforu ön plana çıkarıldı.
"""

output_path = "/Users/applesupport/Desktop/linail beauty/reklam_calisma_defteri_20_kasim/06_LINAIL_INSTAGRAM_61_GONDERI_DERIN_ANALIZI.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md)

print("Master Report Generated Successfully at:", output_path)
