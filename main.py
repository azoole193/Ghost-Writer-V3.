import os
import subprocess

def setup_system():
    print("🤖 Menyiapkan sistem Ghost-Writer V3...")
    client_data = os.environ.get('CLIENT_SECRETS_JSON')
    if client_data:
        with open('client_secrets.json', 'w') as f:
            f.write(client_data)
        print("✅ Kredensial Siap.")

def download_viral_content(platform_url):
    print(f"📥 Hunting konten viral di: {platform_url}")
    try:
        # Mengambil video dengan nama 'temp_video.mp4'
        subprocess.run(['yt-dlp', '-f', 'mp4', '-o', 'temp_video.mp4', platform_url], check=True)
        print("✅ Konten berhasil diamankan.")
    except Exception as e:
        print(f"❌ Gagal download: {e}")

def apply_anti_copyright():
    print("🎬 Menjalankan Protokol Anti-Copyright...")
    # Mirror + Zoom + Audio Pitching
    cmd = [
        'ffmpeg', '-i', 'temp_video.mp4',
        '-vf', 'hflip,scale=iw*1.02:-1,crop=iw/1.02:ih/1.02',
        '-af', 'asetrate=44100*1.05,atempo=1/1.05',
        '-c:v', 'libx264', '-preset', 'ultrafast', 'final_upload.mp4'
    ]
    subprocess.run(cmd)
    print("✅ Video dimodifikasi secara unik.")

def cleanup():
    print("🧹 Menjalankan Protokol Sapu Bersih...")
    # Menghapus file agar tidak memenuhi server/repo
    files_to_delete = ['temp_video.mp4', 'final_upload.mp4', 'client_secrets.json']
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️ Berhasil menghapus: {file}")
    print("✅ Server Bersih Kembali.")

if __name__ == "__main__":
    setup_system()
    
    # KAPTEN: Bisa ganti dengan link TikTok/IG/YT Shorts yang viral
    target_url = "https://www.youtube.com/shorts/p6-9kS_k7X0" 
    
    download_viral_content(target_url)
    
    if os.path.exists("temp_video.mp4"):
        apply_anti_copyright()
        
        # --- TAHAP UPLOAD AKAN DI SINI ---
        print("📤 [SIMULASI] Mengunggah final_upload.mp4 ke YouTube Shorts...")
        
        # Setelah semua beres, kita hapus jejak
        cleanup()
        print("🚀 MISI SELESAI!")
