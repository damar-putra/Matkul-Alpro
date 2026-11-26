# Program Penggunaan While dan Break/Continue
print("=== DEMO WHILE & CONTROL ===")

# Contoh 1: Counted Loop dengan While
hitung = 1
while hitung <= 5:
    print(f"Langkah ke-{hitung}")
    hitung += 1

# Contoh 2: Continue (Melewati angka 3)
print("\nPenggunaan Continue:")
for angka in range(1, 6):
    if angka == 3:
        continue  # Lewati angka 3
    print(f"Angka: {angka}")

# Contoh 3: Break (Berhenti total saat angka 4)
print("\nPenggunaan Break:")
for angka in range(1, 6):
    if angka == 4:
        break  # Berhenti total
    print(f"Angka: {angka}")
