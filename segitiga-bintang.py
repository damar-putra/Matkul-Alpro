print("=" *40)
print("=== PROGRAM SEGITIGA BINTANG ===")
print("=" *40)

while True:
    print("\nPilih jenis segitiga bintang:")
    print("1. Segitiga Bintang Siku-Siku")
    print("2. Segitiga Bintang Sama Kaki")
    pilihan = int(input("Masukkan pilihan (1/2): "))

    jumlah_baris = int(input("Masukkan jumlah baris: "))
    print("\nHasil Segitiga Bintang:\n")

    if pilihan == 1:
        for i in range(1, jumlah_baris + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif pilihan == 2:
        for i in range(1, jumlah_baris + 1):
            for spasi in range(jumlah_baris - i):
                print(" ", end="")
            
            for bintang in range(2 * i - 1):
                print("*", end="")

            print()  

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

    lagi = input("\nApakah ingin membuat segitiga bintang lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        print("\nTerima kasih telah menggunakan program ini!")
        break