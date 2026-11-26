# Program Tabel Perkalian Interaktif
print("=== PROGRAM TABEL PERKALIAN ===")
n = int(input("Ingin menampilkan tabel perkalian sampai angka berapa? "))

print(f"\nTABEL PERKALIAN 1 SAMPAI {n}")
print("-" * 25)

for i in range(1, n + 1):  # Loop Baris
    print(f"Perkalian {i}:")
    for j in range(1, 11):     # Loop Kolom (1 sampai 10)
        hasil = i * j
        print(f"  {i} x {j} = {hasil}")
    print("-" * 15)
