import subprocess
import os

out_dir = "/Users/applesupport/Desktop/linail beauty/reklam_ipek_kirpik"
assets_dir = "/Users/applesupport/Desktop/linail beauty/assets"
ffmpeg = "/Users/applesupport/.local/bin/ffmpeg"

s1 = os.path.join(out_dir, "slide_1.png")
s2 = os.path.join(out_dir, "slide_2.png")
s3 = os.path.join(out_dir, "slide_3.png")
s4 = os.path.join(out_dir, "slide_4.png")
audio_src = os.path.join(assets_dir, "salon-experience.mp4")
out_video = os.path.join(out_dir, "linail_kahve_ipek_kirpik_reels.mp4")

# Each slide displays for 4 seconds with 0.5s xfade transition
# Total 4 slides = ~14.5 seconds
filter_complex = """
[0:v]scale=1080:1350,pad=1080:1920:0:(1920-1350)/2:color=0x18091E,format=yuv420p[v0];
[1:v]scale=1080:1350,pad=1080:1920:0:(1920-1350)/2:color=0x18091E,format=yuv420p[v1];
[2:v]scale=1080:1350,pad=1080:1920:0:(1920-1350)/2:color=0x18091E,format=yuv420p[v2];
[3:v]scale=1080:1350,pad=1080:1920:0:(1920-1350)/2:color=0x18091E,format=yuv420p[v3];
[v0][v1]xfade=transition=fade:duration=0.6:offset=3.5[xf1];
[xf1][v2]xfade=transition=fade:duration=0.6:offset=6.9[xf2];
[xf2][v3]xfade=transition=fade:duration=0.6:offset=10.3[vout];
[4:a]atrim=start=5:end=19.5,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1,afade=t=out:st=13:d=1.5[aout]
"""

cmd = [
    ffmpeg, "-y",
    "-loop", "1", "-t", "4.1", "-i", s1,
    "-loop", "1", "-t", "4.1", "-i", s2,
    "-loop", "1", "-t", "4.1", "-i", s3,
    "-loop", "1", "-t", "4.2", "-i", s4,
    "-i", audio_src,
    "-filter_complex", filter_complex.strip(),
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "20",
    "-c:a", "aac",
    "-b:a", "192k",
    "-pix_fmt", "yuv420p",
    "-t", "14.5",
    out_video
]

print("Rendering Reels video...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"SUCCESS: Created {out_video}")
else:
    print("FFmpeg Error:", res.stderr[-500:])
