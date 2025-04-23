import random
import string
# CopyrightDimas - Fungsi untuk membersihkan input (hapus spasi, tanda baca, ubah ke huruf besar)
def bersihkan_input(teks):
    return ''.join(filter(str.isalpha, teks.upper()))

# CopyrightDimas - Fungsi untuk generate key secara acak
def buat_key_random(panjang):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(panjang))

# CopyrightDimas - Fungsi konversi karakter ke angka 0-25
def huruf_ke_angka(huruf):
    return ord(huruf) - ord('A')

# CopyrightDimas - Fungsi konversi angka 0-25 ke karakter A-Z
def angka_ke_huruf(angka):
    return chr(angka + ord('A'))

# Mulai program
print("=== Program One-Time Pad (OTP) Cipher ===\n")
print("Keamanan Sistem Informasi dan Jaringan\n")

# Input plaintext dari user
plaintext = input("Masukkan plaintext (hanya huruf): ")
plaintext = bersihkan_input(plaintext)

# Pilih mode key: random atau manual
mode_key = input("Pilih jenis key (ketik 'random' atau 'manual'): ").strip().lower()

if mode_key == "random":
    key = buat_key_random(len(plaintext))
elif mode_key == "manual":
    key = input("Masukkan key manual (panjang harus sama dengan plaintext): ")
    key = bersihkan_input(key)
    if len(key) != len(plaintext):
        print("❌ Yahh.. Panjang key harus sama dengan panjang plaintext dong!")
        exit()
else:
    print("❌ Mode key tidak dikenali bos!")
    exit()

# Proses enkripsi
ciphertext = []
print("\n--- Proses Enkripsi ---")
for huruf_p, huruf_k in zip(plaintext, key):
    nilai_p = huruf_ke_angka(huruf_p)
    nilai_k = huruf_ke_angka(huruf_k)
    nilai_c = (nilai_p + nilai_k) % 26
    huruf_c = angka_ke_huruf(nilai_c)
    ciphertext.append(huruf_c)
    
    # Tampilkan detail proses
    print(f"{huruf_p}+{huruf_k} = ({nilai_p}+{nilai_k}) % 26 = {nilai_c} = {huruf_c}")

# Tampilkan hasil akhir
print("\n=== Hasil Akhir ===")
print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ''.join(ciphertext))