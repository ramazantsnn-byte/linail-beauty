import subprocess
import os

out_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"
ffmpeg = "/Users/applesupport/.local/bin/ffmpeg"

voiceover = os.path.join(out_dir, "ipek_kirpik_seslendirme.mp3")
bg_music_src = os.path.join(assets_dir, "salon-experience.mp4")
out_video = os.path.join(out_dir, "03_REKLAM_REELS_CATEYE_VS_WISPY.mp4")

img_cateye = os.path.join(assets_dir, "cat_eye_silk_lashes.jpg")
img_macro = os.path.join(assets_dir, "luxury_silk_lash_macro.jpg")
video_studio = os.path.join(assets_dir, "vip_oda_deneyimi.mp4")
video_logo = os.path.join(assets_dir, "linail-logo-animation.mp4")

# Escaped filter complex with safe characters (no unescaped colons)
filter_complex = """
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='LİNAİL BEAUTY':fontcolor=0xD4AF37:fontsize=38:x=(w-text_w)/2:y=240:box=1:boxcolor=black@0.65:boxborderw=14,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Cat eye mı, Wispy mi?':fontcolor=0xFFF0BE:fontsize=54:x=(w-text_w)/2:y=310:box=1:boxcolor=black@0.75:boxborderw=16,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Arkadaşına Gönder 💜':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=395:box=1:boxcolor=black@0.65:boxborderw=12,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Ataşehir • Uphill Towers':fontcolor=0xD4AF37:fontsize=34:x=(w-text_w)/2:y=1620:box=1:boxcolor=black@0.7:boxborderw=12,
fade=t=in:st=0:d=0.5,fade=t=out:st=5.0:d=0.5[v1];

[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='KİŞİYE ÖZEL KİRPİK MİMARİSİ':fontcolor=0xD4AF37:fontsize=38:x=(w-text_w)/2:y=240:box=1:boxcolor=black@0.65:boxborderw=14,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Göz Kapağınıza Göre Milimetrik Tasarım':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=310:box=1:boxcolor=black@0.75:boxborderw=16,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='0.07 mm İpek Lif • Sıfır Ağırlık • Sıfır Yanma':fontcolor=0xFFF0BE:fontsize=36:x=(w-text_w)/2:y=395:box=1:boxcolor=black@0.65:boxborderw=12,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Brown Lashes • Naturel Moka Tonları':fontcolor=0xD4AF37:fontsize=34:x=(w-text_w)/2:y=1620:box=1:boxcolor=black@0.7:boxborderw=12,
fade=t=in:st=0:d=0.5,fade=t=out:st=6.0:d=0.5[v2];

[2:v]trim=start=2:end=6.5,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='SABAH RİMELE SON ✨':fontcolor=0xD4AF37:fontsize=40:x=(w-text_w)/2:y=240:box=1:boxcolor=black@0.65:boxborderw=14,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Dinlendirici VIP Süit Deneyimi':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=310:box=1:boxcolor=black@0.75:boxborderw=16,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='4-6 Hafta Kalıcı Kusursuz İfade':fontcolor=0xFFF0BE:fontsize=38:x=(w-text_w)/2:y=395:box=1:boxcolor=black@0.65:boxborderw=12,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Günde Sınırlı Sayıda Misafir':fontcolor=0xD4AF37:fontsize=34:x=(w-text_w)/2:y=1620:box=1:boxcolor=black@0.7:boxborderw=12,
fade=t=in:st=0:d=0.5,fade=t=out:st=4.0:d=0.5[v3];

[3:v]trim=start=0:end=4.0,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Göz Analizi İçin DM’den Yazın 🌸':fontcolor=0xFFF0BE:fontsize=48:x=(w-text_w)/2:y=260:box=1:boxcolor=black@0.8:boxborderw=18,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Modelinizi Birlikte Belirleyelim':fontcolor=white:fontsize=38:x=(w-text_w)/2:y=340:box=1:boxcolor=black@0.7:boxborderw=14,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='WhatsApp VIP - 0531 869 67 64':fontcolor=0xD4AF37:fontsize=44:x=(w-text_w)/2:y=1560:box=1:boxcolor=black@0.85:boxborderw=18,
drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial Bold.ttf':text='Barbaros Mah. Uphill Towers B Blok Daire 14':fontcolor=white:fontsize=32:x=(w-text_w)/2:y=1640:box=1:boxcolor=black@0.7:boxborderw=12,
fade=t=in:st=0:d=0.5,fade=t=out:st=3.5:d=0.5[v4];

[v1][v2][v3][v4]concat=n=4:v=1:a=0[vout];

[4:a]volume=1.0[voice];
[5:a]atrim=start=0:end=20.5,asetpts=PTS-STARTPTS,volume=0.18,afade=t=in:st=0:d=1,afade=t=out:st=19.5:d=1[bgm];
[voice][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]
"""

cmd = [
    ffmpeg, "-y",
    "-loop", "1", "-t", "5.5", "-i", img_cateye,
    "-loop", "1", "-t", "6.5", "-i", img_macro,
    "-i", video_studio,
    "-i", video_logo,
    "-i", voiceover,
    "-i", bg_music_src,
    "-filter_complex", filter_complex.strip(),
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "20",
    "-r", "30",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-t", "20.5",
    out_video
]

print("Rendering high-definition Reels Video...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"SUCCESS: Rendered {out_video} ({os.path.getsize(out_video)} bytes)")
else:
    print("FFmpeg Error:\n", res.stderr[-800:])
