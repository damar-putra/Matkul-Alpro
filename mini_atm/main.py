from modul import cek_saldo, setor_tunai, tarik_tunai

def main():
    saldo_awal = 500000
    saldo_saat_ini = saldo_awal
    
    while True:
        print("\n=== MENU ATM MINI ===")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            cek_saldo(saldo_saat_ini)
        elif pilihan == "2":
            try:
                nominal = float(input("Masukkan nominal setor: Rp "))
                saldo_saat_ini = setor_tunai(saldo_saat_ini, nominal)
            except ValueError:
                print(">> Error: Input harus berupa angka.")
        elif pilihan == "3":
            try:
                nominal = float(input("Masukkan nominal tarik: Rp "))
                saldo_saat_ini = tarik_tunai(saldo_saat_ini, nominal)
            except ValueError:
                print(">> Error: Input harus berupa angka.")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan ATM Mini.")
            break
        else:
            print(">> Pilihan tidak valid.")


main()