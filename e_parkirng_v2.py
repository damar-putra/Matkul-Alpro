import datetime
import os
import math

FILE_AKUN = "akun_petugas.txt"
FILE_HISTORY = "history.txt"

# Registrasi
def registrasi():
    print("\n=== Registrasi Petugas Parkir ===")
    nama_lengkap = input("Masukkan nama lengkap: ")
    nim = input("Masukkan NIM: ")

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
    else:
        with open(FILE_AKUN, "a") as file:
            file.write(f"{username},{password},{nama_lengkap}\n")
        print("\nRegistrasi berhasil!")
        print(f"Username: {username}")
        print(f"Password: {password}")

# login
def login():
    print("\n=== Login Petugas Parkir ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if os.path.exists(FILE_AKUN):
        with open(FILE_AKUN, "r") as file:
            for baris in file:
                data = baris.strip().split(",")
                if data[0] == username and data[1] == password:
                    print("/nLogin berhasil!")
                    return data[2]

    else:
        print("Akun tidak ditemukan. Silakan registrasi terlebih dahulu.")
        registrasi()
        return None

# waktu_parkir
def waktu_parkir():
    while True:
        waktu = input("Apakah anda ingin mencatat waktu secara manual? (ya/tidak): ").lower()
        if waktu == "ya":
            durasi = int(input("Masukkan durasi parkir (dalam jam): "))
            waktu_keluar_manual = datetime.datetime.now()
            waktu_masuk_manual = datetime.datetime.now() - datetime.timedelta(hours=durasi)
            print(f"Waktu masuk: {waktu_masuk_manual.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Waktu keluar: {waktu_keluar_manual.strftime('%Y-%m-%d %H:%M:%S')}")
            return durasi
        
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
            return durasi
            
        else:
            print(">> Jawaban tidak valid, ketik 'ya' atau 'tidak'")


# Transaksi Parkir
def transaksi(nama_petugas):
    while True:
        print("\n" + "=" *40)
        print("=== Transaksi Parkir ===")
        print("=" *40)
        plat_nomor = input("Masukkan plat nomor kendaraan: ")
        jenis_kendaraan = int(input("Masukkan jenis kendaraan (1=motor, 2=mobil): "))

        if jenis_kendaraan != 1 and jenis_kendaraan != 2:
            print(">> Error Jenis Kendaraan tidak Valid! ")
            continue

        durasi_parkir = waktu_parkir()
        if jenis_kendaraan == 1:
            tarif_2jam, tarif_lanjut = 3000, 1000
            nama_kendaraan = "Motor"
        else:
            tarif_2jam, tarif_lanjut = 6000, 2000
            nama_kendaraan = "Mobil"

        total_biaya = tarif_2jam
        if durasi_parkir > 2:
            total_biaya = tarif_2jam + ((durasi_parkir - 2) * tarif_lanjut)

        print(f"\nDurasi Parkir : {durasi_parkir} jam")
        print(f"Total Biaya   : Rp {total_biaya:,.0f}")

        # Simpan ke history
        waktu_sekarang = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(FILE_HISTORY, "a") as file:
            file.write(f"{waktu_sekarang} | {nama_petugas} | {plat_nomor} | {nama_kendaraan} | {durasi_parkir} jam | Rp {total_biaya:,.0f}\n")
        
        print("\n[INFO] Transaksi berhasil disimpan ke history!")
        
        lagi = input("\nAda kendaraan lain? (ya/tidak): ").lower()
        if lagi != "ya":
            break


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
        print("\nTekan Enter untuk kembali ke Menu!")


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
            registrasi()
        elif menu == "2":
            nama_petugas = login()
            if nama_petugas:
                transaksi()
        elif menu == "3":
            lihat_history()
        elif menu == "4":
            print("/n>> Keluar dari Program")
            break
        else:
            print("/n>> Pilihan tidak Valid! Pilih opsi 1-4")

if __name__ == "__main__":
    main()