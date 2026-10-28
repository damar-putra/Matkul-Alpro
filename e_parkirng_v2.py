import datetime
import os
import math

FILE_AKUN = "akun_petugas.txt"
FILE_HISTORY = "history.txt"

# Registrasi
def registrasi():
    print("\n=== Registrasi Petugas Parkir ===")
    nama_lengkap = input("Masukkan nama lengkap: ")
    nim = input("Masukkan NIM: ").replace(".", "")

    username = nama_lengkap.lower().replace(" ", "")
    password = "parkir" + nim[-3:]

    user_sudah_ada = False
    if os.path.exists(FILE_AKUN):
        with open(FILE_AKUN, "r") as file:
            for baris in file:
                akun = baris.strip().split(",")
                if akun[0] == username:
                    user_sudah_ada = True
                    break

    if user_sudah_ada:
        print("Username sudah digunakan. Silakan coba lagi.")
        return False
    else:
        with open(FILE_AKUN, "a") as file:
            file.write(f"{username},{password},{nama_lengkap},{nim}\n")
        print("\nRegistrasi berhasil!")
        print(f"Username: {username}")
        print(f"Password: {password}")
        return True

# login
def login():
    print("\n=== Login Petugas Parkir ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    username_ditemukan = False

    if os.path.exists(FILE_AKUN):
        with open(FILE_AKUN, "r") as file:
            for baris in file:
                data = baris.strip().split(",")
                if data[0] == username:
                    username_ditemukan = True
                    if data[1] == password:
                        print("\nLogin berhasil!")
                        return data[2], data[3]
                    else:
                        print(">> Error: Password Salah!")
                        return None
                

    if not username_ditemukan:
        print("\n>> Akun tidak ditemukan. Anda akan di alihkan ke laman login!")
        input("Tekan Enter untuk melanjutkan!...")

        berhasil_regis = registrasi()

        if berhasil_regis:
            print("\n[INFO] Silahkan login menggunakan akun baru!")
            return login()  
        else:
            return None

# waktu_parkir
def waktu_parkir():
    while True:
        waktu = input("Apakah anda ingin mencatat waktu secara manual? (ya/tidak): ").lower()
        if waktu == "ya":
            durasi = int(input("Masukkan durasi parkir (dalam jam): "))
            waktu_keluar = datetime.datetime.now()
            waktu_masuk = datetime.datetime.now() - datetime.timedelta(hours=durasi)
            print(f"Waktu masuk: {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Waktu keluar: {waktu_keluar.strftime('%Y-%m-%d %H:%M:%S')}")
            return durasi, waktu_masuk, waktu_keluar
        
        elif waktu == "tidak":
            waktu_masuk = datetime.datetime.now()
            print(f"Waktu masuk: {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}")

            input("Tekan Enter untuk mencatat waktu keluar...")
            waktu_keluar = datetime.datetime.now()
            print(f"Waktu keluar: {waktu_keluar.strftime('%Y-%m-%d %H:%M:%S')}")

            selisih_detik = (waktu_keluar - waktu_masuk).total_seconds()
            durasi = math.ceil(selisih_detik / 3600) 
            if durasi == 0:
                durasi = 1
            return durasi, waktu_masuk, waktu_keluar
            
        else:
            print(">> Jawaban tidak valid, ketik 'ya' atau 'tidak'")


# Transaksi Parkir
def transaksi(nama_petugas, nim):
    while True:
        print("\n" + "=" *40)
        print("=== Transaksi Parkir ===")
        print("=" *40)
        plat_nomor = input("Masukkan plat nomor kendaraan: ")
        jenis_kendaraan = int(input("Masukkan jenis kendaraan (1=motor, 2=mobil): "))

        if jenis_kendaraan != 1 and jenis_kendaraan != 2:
            print(">> Error Jenis Kendaraan tidak Valid! ")
            continue

        durasi, waktu_masuk, waktu_keluar = waktu_parkir()
        if jenis_kendaraan == 1:
            tarif_2jam, tarif_lanjut = 3000, 1000
            nama_kendaraan = "Motor"
        else:
            tarif_2jam, tarif_lanjut = 6000, 2000
            nama_kendaraan = "Mobil"

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
                while True:
                    print(f"Total Tagihan: Rp {total_tagihan:,.0f}")
                    uang_bayar = float(input("Masukkan jumlah uang yang dibayarkan: "))
                    kekurangan = total_tagihan - uang_bayar
                    if uang_bayar < total_tagihan:
                        print(f"Transaksi Gagal: Uang anda kurang sebesar Rp {kekurangan:,.0f}.")
                    else:
                        kembalian = uang_bayar - total_tagihan
                        print("\n[INFO] Transaksi berhasil!")

                        struk_parkir(nama_petugas, nim, waktu_masuk, waktu_keluar, plat_nomor, jenis_kendaraan, durasi, status_member, biaya_parkir, denda, diskon, total_tagihan, uang_bayar, kembalian)
                        break

        # Simpan ke history
        waktu_sekarang = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(FILE_HISTORY, "a") as file:
            file.write(f"{waktu_sekarang} | {nama_petugas} | {plat_nomor} | {nama_kendaraan} | {durasi} jam | Rp {total_tagihan:,.0f}\n")
        
        print("\n[INFO] Transaksi berhasil disimpan ke history!")
        
        lagi = input("\nAda kendaraan lain? (ya/tidak): ").lower()
        if lagi != "ya":
            break

# struk
def struk_parkir(nama_petugas, nim, waktu_masuk, waktu_keluar, plat_nomor, jenis_kendaraan, durasi, status_member, biaya_parkir, denda, diskon, total_tagihan, uang_bayar, kembalian):
    saat_ini = waktu_keluar
    print("\n" + "=" *40)
    print("         STRUK PARKIR         ") 
    print(f"date: {saat_ini.strftime('%Y-%m-%d %H:%M:%S')}")    
    print("=" *40)
    print(f"Nama Lengkap: {nama_petugas}")
    print(f"NIM: {nim}")
    print(f"Plat Nomor: {plat_nomor}")
    print(f"Jenis Kendaraan: {'Motor' if jenis_kendaraan == 1 else 'Mobil'}")
    print(f"Durasi Parkir: {durasi} jam")
    print(f"Waktu masuk: {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Waktu keluar: {waktu_keluar.strftime('%Y-%m-%d %H:%M:%S')}")
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

def lihat_history():
    print("\n" + "=" *40)
    print("     RIWAYAT TRANSAKSI E-PARKING     ")
    print("=" *40)

    if os.path.exists(FILE_HISTORY):
        with open (FILE_HISTORY, "r") as file:
            isi = file.read()
            if isi == "":
                print("[INFO] Belum Ada Transaksi")
            else:
                print(isi)
    else:
        print("[INFO] File history belum dibuat.")

    input("\nTekan Enter untuk kembali ke Menu!")


def main():
    while True:
        print("\n" + "=" *40)
        print("     SISTEM E-PARKING POLINES       ")
        print("=" *40)
        print("1. Registrasi akun petugas")
        print("2. Login")
        print("3. History")
        print("4. Keluar Program")
        print("=" *40)

        menu = input("Pilih Menu (1-4): ")

        if menu == "1":
            berhasil = registrasi()
            if berhasil:
                hasil_login = login()
                if hasil_login:
                    nama_petugas, nim = hasil_login
                    transaksi(nama_petugas, nim)
        elif menu == "2":
            hasil_login = login()
            if hasil_login:
                nama_petugas, nim = hasil_login
                transaksi(nama_petugas, nim)
        elif menu == "3":
            lihat_history()
        elif menu == "4":
            print("\n>> Keluar dari Program")
            break
        else:
            print("\n>> Pilihan tidak Valid! Pilih opsi 1-4")

if __name__ == "__main__":
    main()