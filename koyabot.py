import requests
import time
import sys

# ==================== DATA PENGGUNA ====================
# TEMPELKAN TOKEN BARU ANDA DI SINI (Wajib ambil baru lewat F12)
TOKEN = "MASUKKAN_TOKEN_BARU_ANDA_DISINI"
CHANNEL_ID = "1541010333894836315"
# =======================================================

url = f"https://discord.com{CHANNEL_ID}/messages"
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

pesan_list = ["p", "up", "r"]

print("=== SCRIPT SPAM DISCORD DI CLOUD GITHUB AKTIF ===")
print("Anda bebas MENUTUP browser ini dan mematikan laptop sekarang!")
print("Untuk BERHENTI: Klik area Terminal bawah lalu tekan CTRL + C.`\n")

try:
    while True:
        for pesan in pesan_list:
            data = {"content": pesan}
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                print(f"Berhasil terkirim ke Discord: {pesan}")
            elif response.status_code == 429:
                print("Terkena pembatasan kecepatan Discord. Menunggu 5 detik...")
                time.sleep(5)
            elif response.status_code == 401:
                print("Gagal! Token Anda salah atau sudah kedaluwarsa. Silakan ambil token baru.")
                sys.exit()
            else:
                print(f"Gagal mengirim. Code: {response.status_code}")
                
            time.sleep(1) # Jeda waktu 1 detik
except KeyboardInterrupt:
    print("\nScript dihentikan oleh pengguna.")
    sys.exit()
