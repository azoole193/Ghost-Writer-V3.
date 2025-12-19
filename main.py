import os

def setup_system():
    print("🤖 Menyiapkan sistem Ghost-Writer V3...")
    # Mengecek apakah rahasia (Secrets) sudah terbaca oleh sistem
    client_data = os.environ.get('CLIENT_SECRETS_JSON')
    
    if client_data:
        print("✅ Kredensial (CLIENT_SECRETS_JSON) terdeteksi!")
        # Membuat file fisik sementara agar bisa dipakai library Google nanti
        with open('client_secrets.json', 'w') as f:
            f.write(client_data)
    else:
        print("❌ ERROR: Kredensial TIDAK ditemukan di Secrets!")

if __name__ == "__main__":
    setup_system()
    print("🚀 Status: Robot Siap Beraksi!")
