import subprocess
import os

out_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"
ffmpeg = "/Users/applesupport/.local/bin/ffmpeg"

img_cateye = os.path.join(assets_dir, "cat_eye_silk_lashes.jpg")
img_macro = os.path.join(assets_dir, "luxury_silk_lash_macro.jpg")
video_studio = os.path.join(assets_dir, "vip_oda_deneyimi.mp4")
video_logo = os.path.join(assets_dir, "linail-logo-animation.mp4")

ov1 = os.path.join(out_dir, "overlay_scene1.png")
ov2 = os.path.join(out_dir, "overlay_scene2.png")
ov3 = os.path.join(out_dir, "overlay_scene3.png")
ov4 = os.path.join(out_dir, "overlay_scene4.png")

voiceover = os.path.join(out_dir, "ipek_kirpik_seslendirme.mp3")
bg_music = os.path.join(assets_dir, "salon-experience.mp4")

out_video = os.path.join(out_dir, "03_REKLAM_REELS_CATEYE_VS_WISPY.mp4")

filter_complex = """
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[bg1];
[bg1][1:v]overlay=0:0:format=auto,fade=t=in:st=0:d=0.5,fade=t=out:st=5.0:d=0.5[s1];

[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[bg2];
[bg2][3:v]overlay=0:0:format=auto,fade=t=in:st=0:d=0.5,fade=t=out:st=6.0:d=0.5[s2];

[4:v]trim=start=2:end=6.5,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[bg3];
[bg3][5:v]overlay=0:0:format=auto,fade=t=in:st=0:d=0.5,fade=t=out:st=4.0:d=0.5[s3];

[6:v]trim=start=0:end=4.0,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[bg4];
[bg4][7:v]overlay=0:0:format=auto,fade=t=in:st=0:d=0.5,fade=t=out:st=3.5:d=0.5[s4];

[s1][s2][s3][s4]concat=n=4:v=1:a=0[vout];

[8:a]volume=1.0[voice];
[9:a]atrim=start=0:end=20.5,asetpts=PTS-STARTPTS,volume=0.18,afade=t=in:st=0:d=1,afade=t=out:st=19.5:d=1[bgm];
[voice][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]
"""

cmd = [
    ffmpeg, "-y",
    "-loop", "1", "-t", "5.5", "-i", img_cateye,     # 0
    "-loop", "1", "-t", "5.5", "-i", ov1,            # 1
    "-loop", "1", "-t", "6.5", "-i", img_macro,      # 2
    "-loop", "1", "-t", "6.5", "-i", ov2,            # 3
    "-i", video_studio,                              # 4
    "-loop", "1", "-t", "4.5", "-i", ov3,            # 5
    "-i", video_logo,                                # 6
    "-loop", "1", "-t", "4.0", "-i", ov4,            # 7
    "-i", voiceover,                                 # 8
    "-i", bg_music,                                  # 9
    "-filter_complex", filter_complex.strip(),
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "20",
    "-r", "30",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-t", "20.5",
    out_video
]

print("Rendering master Meta Reels video...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    size = os.path.getsize(out_video)
    print(f"SUCCESS: Rendered {out_video} ({size} bytes, {size/1024/1024:.2f} MB)")
else:
    print("FFmpeg Error:\n", res.stderr[-1000:])
