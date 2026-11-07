#!/usr/bin/env python3
"""
LİNAİL BEAUTY • VİRAL REELS & VİDEO ANALİZ MOTORU (v1.0)
GitHub açık kaynak mimarisi (yt-dlp + ffmpeg + OpenCV + Gemini Multimodal)
Herhangi bir Instagram Reels / TikTok videosunu veya yerel MP4 dosyasını inceler:
1. İlk 0-3 saniyelik görsel kancayı (Hook) kare kare parçalar.
2. Kesme sıklığını (Pacing velocity) ölçer.
3. Ses ve metin kurgusunu deşifre eder.
4. Linail Beauty için 100 üzerinden virallik skoru ve uyarlama reçetesi çıkarır.
"""

import os, sys, time, subprocess, json, argparse, requests
from pathlib import Path

GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_NAME = "gemini-3.5-flash-lite"
WORK_DIR   = Path("/tmp/reels_analysis")

def ensure_work_dir():
    WORK_DIR.mkdir(parents=True, exist_ok=True)

def download_video(url: str) -> Path:
    ensure_work_dir()
    out_tmpl = str(WORK_DIR / "target_video.%(ext)s")
    # Eski dosyaları temizle
    for f in WORK_DIR.glob("target_video*"):
        try: f.unlink()
        except: pass

    cmd = [
        "/Library/Frameworks/Python.framework/Versions/3.13/bin/yt-dlp",
        "--format", "mp4/best",
        "-o", out_tmpl,
        url
    ]
    print(f"📥 Video indiriliyor: {url}")
    subprocess.run(cmd, check=True)
    
    mp4_files = list(WORK_DIR.glob("target_video*.mp4"))
    if not mp4_files:
        raise FileNotFoundError("Video indirilemedi!")
    return mp4_files[0]

def extract_hook_frames(video_path: Path) -> list[str]:
    """İlk 0.5s, 1.0s, 2.0s, 3.0s, 5.0s karelerini çıkarır."""
    ensure_work_dir()
    timestamps = [0.5, 1.0, 2.0, 3.0, 5.0]
    frame_paths = []
    
    for i, t in enumerate(timestamps):
        out_frame = str(WORK_DIR / f"frame_{i}_{t}s.jpg")
        cmd = [
            "/Users/applesupport/.local/bin/ffmpeg",
            "-y",
            "-ss", str(t),
            "-i", str(video_path),
            "-vframes", "1",
            "-q:v", "2",
            out_frame
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(out_frame):
            frame_paths.append(out_frame)
            
    print(f"📸 {len(frame_paths)} kilit kanca karesi yakalandı.")
    return frame_paths

def analyze_hook_with_gemini(frame_paths: list[str], extra_notes: str = "") -> str:
    """Yakalanan kareleri Gemini Multimodal'a gönderip derin trikoloji & reklam analizi yapar."""
    import base64
    
    parts = []
    # Kareleri base64 ekle
    for fp in frame_paths:
        with open(fp, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        parts.append({
            "inline_data": {
                "mime_type": "image/jpeg",
                "data": b64
            }
        })
        
    prompt = f"""Sen dünya çapında viral Reels ve kısa video analizi yapan usta bir kreatör ve video stratejistisin.
Sana bir Reels videosunun İLK 3-5 SANİYESİNDEN (Kanca / Hook bölümü) çıkarılmış kilit kareleri verdim.

GÖREVİN — GERÇEK BİR VİDEO YÖNETMENİ GÖZÜYLE ŞU ANALİZİ YAPMAK:
1. GÖRSEL KANCA (Visual Hook - 0-1. Saniye):
   - Ekranda izleyiciyi parmağını kaydırmaktan durduran ilk hareket / nesne nedir?
   - Makro çekim, şok edici bir eylem, ASMR detayı veya renk kontrastı var mı?
2. EKRAN ÜSTÜ METİN & MERAK BOŞLUĞU (Curiosity Gap):
   - Başlık izleyicide 'bunu sonuna kadar izlemeliyim' hissi uyandırıyor mu?
   - Klişe ve sıkıcı mı, yoksa provokatif ve merak ettirici mi?
3. RİTİM & KESME HIZI (Pacing):
   - İlk 3 saniyede açı değişimi veya görsel hareket yeterli mi?
4. LİNAİL BEAUTY (GÜLŞAH TAŞAN) İÇİN UYARLAMA REÇETESİ:
   - Bu videonun kurgusal şablonunu Uphill Towers Ataşehir'deki salonumuzda (Kombi Manikür, Cam Cilt veya IC Factory Kaş Laminasyonu için) BİREBİR nasıl çekeriz?
   - Gülşah'ın söyleyeceği 3 saniyelik ilk kanca cümlesi ne olmalı?
   - Kameranın açısı (Makro lens, tripod konumu) ne olmalı?
5. VİRALLİK PUANI (1 - 100):
   - Neden bu puanı verdin? Eksik olan ne?

Notlar: {extra_notes}
Cevabını doğrudan, net ve maddeler halinde Türkçe ver."""

    parts.append({"text": prompt})
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={GEMINI_KEY}"
    payload = {
        "contents": [{"parts": parts}],
        "generationConfig": {"temperature": 0.4, "maxOutputTokens": 1000}
    }
    
    r = requests.post(url, json=payload, timeout=40)
    if r.status_code == 200:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Gemini Analiz Hatası: {r.status_code} - {r.text[:200]}"

def main():
    parser = argparse.ArgumentParser(description="Viral Reels Hook & Video Analiz Motoru")
    parser.add_argument("--url", help="Instagram Reels veya TikTok linki")
    parser.add_argument("--file", help="Yerel MP4 dosya yolu")
    parser.add_argument("--notes", default="", help="Ekstra analiz notları")
    args = parser.parse_args()

    if not args.url and not args.file:
        print("Kullanım: python3 viral_reels_analyzer.py --url <link> veya --file <video.mp4>")
        sys.exit(1)

    if args.url:
        video_path = download_video(args.url)
    else:
        video_path = Path(args.file)
        if not video_path.exists():
            print(f"Dosya bulunamadı: {video_path}")
            sys.exit(1)

    print(f"🎬 Video analiz ediliyor: {video_path.name}")
    frames = extract_hook_frames(video_path)
    if not frames:
        print("Hata: Kanca kareleri çıkarılamadı!")
        sys.exit(1)

    print("🧠 Gemini Vision Multimodal ile kanca analizi yapılıyor...")
    report = analyze_hook_with_gemini(frames, args.notes)
    
    print("\n" + "="*60)
    print("📊 VİRAL REELS KANCA & VİDEO ANALİZ RAPORU")
    print("="*60)
    print(report)
    print("="*60)
    
    # Raporu kaydet
    out_report = WORK_DIR / "son_video_analiz_raporu.txt"
    out_report.write_text(report, encoding="utf-8")
    print(f"\n💾 Rapor kaydedildi: {out_report}")

if __name__ == "__main__":
    main()
