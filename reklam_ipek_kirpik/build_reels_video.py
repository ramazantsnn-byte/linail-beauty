import subprocess
import os

out_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"
ffmpeg = "/Users/applesupport/.local/bin/ffmpeg"

img1 = os.path.join(assets_dir, "lash_perfect.jpg")
img2 = os.path.join(assets_dir, "ipek_kirpik_centered.jpg")
audio_src = os.path.join(assets_dir, "salon-experience.mp4")
out_video = os.path.join(out_dir, "linail_kahve_ipek_kirpik_reels.mp4")

# Let's write simple drawtext without colons in text or fontfile issues
filter_complex = """
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=text='LİNAİL BEAUTY':fontcolor=0xD4AF37:fontsize=38:x=(w-text_w)/2:y=280:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='Gözlerinizin kendi doğal ışıltısını':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=350:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='ortaya çıkaran tüy kadar hafif zarafet':fontcolor=white:fontsize=44:x=(w-text_w)/2:y=420:box=1:boxcolor=black@0.6:boxborderw=12,
fade=t=in:st=0:d=0.6,fade=t=out:st=4.4:d=0.6[v1];

[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=text='KAHVE İPEK KİRPİK':fontcolor=0xD4AF37:fontsize=38:x=(w-text_w)/2:y=280:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='Kendi kirpiğinizle kusursuz bütünleşen':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=350:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='gözde ağırlık hissettirmeyen doku':fontcolor=white:fontsize=44:x=(w-text_w)/2:y=420:box=1:boxcolor=black@0.6:boxborderw=12,
fade=t=in:st=0:d=0.6,fade=t=out:st=4.4:d=0.6[v2];

[2:v]trim=start=4:end=9,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
drawtext=text='LİNAİL BEAUTY • ATAŞEHİR':fontcolor=0xD4AF37:fontsize=38:x=(w-text_w)/2:y=280:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='Uphill Towers B Blok Daire 14':fontcolor=white:fontsize=46:x=(w-text_w)/2:y=350:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='Sakin VIP Stüdyo ve Özel Seanslar':fontcolor=0xFFF0BE:fontsize=40:x=(w-text_w)/2:y=420:box=1:boxcolor=black@0.6:boxborderw=12,
drawtext=text='WhatsApp 0531 869 67 64':fontcolor=0xD4AF37:fontsize=44:x=(w-text_w)/2:y=1550:box=1:boxcolor=black@0.7:boxborderw=16,
fade=t=in:st=0:d=0.6,fade=t=out:st=4.4:d=0.6[v3];

[v1][v2][v3]concat=n=3:v=1:a=0[vout];
[2:a]atrim=start=4:end=19,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1,afade=t=out:st=14:d=1[aout]
"""

cmd = [
    ffmpeg, "-y",
    "-loop", "1", "-t", "5", "-i", img1,
    "-loop", "1", "-t", "5", "-i", img2,
    "-i", audio_src,
    "-filter_complex", filter_complex.strip(),
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "22",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-t", "15",
    out_video
]

print("Running FFmpeg...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"SUCCESS: Created {out_video}")
else:
    print("FFmpeg Error:", res.stderr[-500:])
