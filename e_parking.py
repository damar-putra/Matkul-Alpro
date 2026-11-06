import datetime

print("=" *40)
print("         E-PARKING SYSTEM         ")
print("=" *40)

#REGISTRASI & INISIALISASI AKUN PETUGAS
nama_lengkap_mhs = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ").replace(".", "")
username_terdaftar = nama_lengkap_mhs.lower().replace(" ", "")
password_terdaftar = "parkir" + nim[-3:]

print("\n[INFO] Akun berhasil dibuat!")
print(f"Username: {username_terdaftar}")
print(f"Password: {password_terdaftar}")

#AUTENTIKASI LOGIN 
print("\n" + "=" *40)
print("         LOGIN E-PARKING         ")
print("=" *40)

percobaan = 1
login_berhasil = False

while percobaan <= 3:
    print(f"\nPercobaan ke-{percobaan}")
    username = input("Masukkan Username: ")
    if username_terdaftar != username:
        print("Error: username petugas tidak terdaftar!")
    else:
        password = input("Masukkan Password: ")
        if password_terdaftar != password:
            print("Error: Password salah! Akses ditolak.")
        else:
            print("\n[INFO] Login berhasil!")
            print(f"Selamat bertugas, {nama_lengkap_mhs}!")
            login_berhasil = True
            break

    percobaan += 1

if not login_berhasil:
    print("\n>> Error: Anda telah mencoba login sebanyak 3 kali. Akun anda diblokir.")
else:

#TRANSAKSI & PERHITUNGAN TARIF PARKIR
    while True:
        print("\n" + "=" *40)
        print("         DATA KENDARAAN PARKIR           ")
        print("=" *40)

        plat_nomor = input("Plat Nomor: ")
        jenis = int(input("Jenis Kendaraan (1=motor, 2=mobil): "))

        if jenis != 1 and jenis != 2:
            print("Error: Jenis kendaraan tidak valid!")
            continue
        
        durasi = int(input("Durasi Parkir (dalam jam): "))

        if jenis == 1:  # motor
            tarif_2jam = 3000
            tarif_lanjut = 1000
        else:
            tarif_2jam = 6000
            tarif_lanjut = 2000

        biaya_parkir = tarif_2jam
        if durasi <= 0:
            print("Error: Durasi parkir tidak valid!")
            continue
        else:
            if durasi > 2:
                biaya_parkir = tarif_2jam + ((durasi - 2) * tarif_lanjut)

            if durasi > 12:
                denda = 20000
            else:
                denda = 0

            subtotal = biaya_parkir + denda
            
            status_member = input("Apakah Anda member? (ya/tidak): ").lower()
            if status_member == "ya":
                diskon = 0.30 * subtotal
            else:
                diskon = 0

            total_tagihan = subtotal - diskon
            print("\n" + "=" *40)
            print("         RINCIAN TAGIHAN PARKIR         ") 
            print("=" *40)

            konfirmasi = input("apakah data sudah benar? (ya/tidak): ").lower()
            if konfirmasi == "tidak":
                print("\n[INFO] Data di batalkan.")
                opsi = input("Ketik 'ulang' untuk mengulang input data, atau 'keluar' untuk keluar: ").lower()
                if opsi == "ulang":
                    continue
                else:
                    print("\n>> Program dihentikan oleh petugas!")
                    break
            else:
                saat_ini = datetime.datetime.now()
                while True:
                    print(f"Total Tagihan: Rp {total_tagihan:,.0f}")
                    uang_bayar = float(input("Masukkan jumlah uang yang dibayarkan: "))
                    kekurangan = total_tagihan - uang_bayar
                    if uang_bayar < total_tagihan:
                        print(f"Transaksi Gagal: Uang anda kurang sebesar Rp {kekurangan:,.0f}.")
                    else:
                        kembalian = uang_bayar - total_tagihan
                        print("\n[INFO] Transaksi berhasil!")
                                
                        
                        print("\n" + "=" *40)
                        print("         STRUK PARKIR         ") 
                        print(f"date: {saat_ini.strftime('%Y-%m-%d %H:%M:%S')}")    
                        print("=" *40)
                        print(f"Nama Lengkap: {nama_lengkap_mhs}")
                        print(f"NIM: {nim}")
                        print(f"Plat Nomor: {plat_nomor}")
                        print(f"Jenis Kendaraan: {'Motor' if jenis == 1 else 'Mobil'}")
                        print(f"Durasi Parkir: {durasi} jam")
                        print(f"Status Member: {'Ya' if status_member == 'ya' else 'Tidak'}")
                        print(f"Biaya Parkir: Rp {biaya_parkir:,.0f}")
                        print(f"Denda: Rp {denda:,.0f}")
                        print(f"Diskon: Rp {diskon:,.0f}")
                        print("=" *40)
                        print(f"Total Tagihan: Rp {total_tagihan:,.0f}")
                        print(f"Uang Bayar: Rp {uang_bayar:,.0f}")
                        print(f"Kembalian: Rp {kembalian:,.0f}")
                        print("=" *40)
                        print("Terima kasih telah menggunakan E-Parking System!")
                        print("Semoga hari Anda menyenangkan!")
                        print("=" *40)
                        break
                transaksi_lagi = input("\nApakah Anda ingin melakukan transaksi parkir lagi? (ya/tidak): ").lower()
                if transaksi_lagi != "ya":
                    print("\n[INFO] Terima kasih telah menggunakan E-Parking System!")
                    break
                    