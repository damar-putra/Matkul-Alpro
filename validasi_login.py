print("=" *40)
print("=== PROGRAM VALIDASI LOGIN ===")
print("=" *40)

PIN_BENAR = "1234"
percobaan = 1
login_berhasil = False

while percobaan <= 3:
    print(f"\nPercobaan ke-{percobaan}")
    pin = input("Masukkan PIN: ")
    if pin == PIN_BENAR:
        print("\n[INFO] Login berhasil!")
        login_berhasil = True
        break
    else:
        sisa_percobaan = 3 - percobaan
        if sisa_percobaan > 0:
            print(f"Error: PIN salah! Sisa percobaan: {sisa_percobaan}")
        else:
            print("\n>> Error: Anda telah mencoba login sebanyak 3 kali. Akses ditolak.")
    percobaan += 1

if not login_berhasil:
    print("\nAkses ditolak. Silakan hubungi administrator.")