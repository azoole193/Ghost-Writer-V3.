import os
import subprocess

def setup_system():
    print("🤖 Menyiapkan sistem Ghost-Writer V3...")
    client_data = os.environ.get('CLIENT_SECRETS_JSON')
    if client_data:
        # Menulis file kredensial dari brankas rahasia
        with open('client_secrets.json', 'w') as f:
            f.write(client_data)
        print("✅ Kredensial Siap.")

def download_viral_content(platform_url):
    print(f"📥 Hunting konten viral di: {platform_url}")
    # yt-dlp secara otomatis mendeteksi platformnya
    try:
        subprocess.run([
            'yt-dlp', 
            '-f', 'mp4', 
            '--no-playlist',
            '-o', 'input_video.mp4', 
            platform_url
        ], check=True)
        print("✅ Konten berhasil diamankan!")
    except Exception as e:
        print(f"❌ Gagal mengambil konten: {e}")

def apply_anti_copyright():
    print("🎬 Menjalankan Protokol Anti-Copyright (FFmpeg)...")
    # Logika: Mirror + Zoom Ringan + Pitching Audio
    cmd = [
        'ffmpeg', '-i', 'input_video.mp4',
        '-vf', 'hflip,scale=iw*1.02:-1,crop=iw/1.02:ih/1.02',
        '-af', 'asetrate=44100*1.05,atempo=1/1.05',
        '-c:v', 'libx264', '-preset', 'ultrafast', 'hasil_akhir.mp4'
    ]
    subprocess.run(cmd)
    print("✅ Video telah dimodifikasi secara unik.")

if __name__ == "__main__":
    setup_system()
    
    # KAPTEN: Ganti link di bawah ini dengan link video viral apa saja!
    target_url = "https://www.youtube.com/shorts/p6-9kS_k7X0" 
    
    download_viral_content(target_url)
    
    if os.path.exists("input_video.mp4"):
        apply_anti_copyright()
        print("🚀 MISI SELESAI: Video siap untuk langkah Upload!")
