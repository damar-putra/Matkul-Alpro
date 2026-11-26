daftar_hadir = []

while True:
    print("\n=== MENU MANAJEMEN PRESENSI ===")
    print("1. Tambah Hadir")
    print("2. Hapus Presensi")
    print("3. Lihat & Urutkan")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == "1":
        nama_input = input("Masukkan nama mahasiswa: ")

        nama = " ".join(nama_input.split()).title() 
        
        if not nama: 
            print("[ERROR] Nama tidak boleh kosong.")
        elif nama in daftar_hadir: 
            print(f"[ERROR] {nama} sudah ada di dalam daftar hadir.")
        else:
            daftar_hadir.append(nama)
            print(f"[INFO] {nama} berhasil ditambahkan.")
            
    elif pilihan == "2":
        nama_input = input("Masukkan nama yang ingin dihapus: ")
        nama = " ".join(nama_input.split()).title()
        
        if nama in daftar_hadir:
            daftar_hadir.remove(nama)
            print(f"[INFO] {nama} berhasil dihapus.")
        else:
            print(f"[ERROR] {nama} tidak ditemukan dalam daftar hadir.")
            
    elif pilihan == "3":
        if len(daftar_hadir) == 0:
            print("[INFO] Daftar hadir masih kosong.")
        else:
            daftar_urut = sorted(daftar_hadir)
            print("\n--- DAFTAR HADIR (ALFABETIS) ---")
            for i, nama in enumerate(daftar_urut, 1):
                print(f"{i}. {nama}")
                
    elif pilihan == "4":
        print("[INFO] Keluar dari program presensi.")
        break
    else:
        print("[ERROR] Pilihan tidak valid. Silakan coba lagi.")