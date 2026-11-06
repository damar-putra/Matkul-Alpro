print("=" *40)
print("=== PROGRAM HITUNG FAKTORIAL ===")
print("=" *40)

while True:
    angka = int(input("Masukkan angka positif: "))

    if angka < 0:
        print("Error: Angka harus positif!")
        continue
    else:
        faktorial = 1
        temp = angka
        while temp > 0:
            faktorial *= temp
            temp -= 1
        print(f"Faktorial dari {angka} adalah {faktorial}")

    lagi = input("\nApakah ingin menghitung faktorial lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        print("\nTerima kasih telah menggunakan program ini!")
        break