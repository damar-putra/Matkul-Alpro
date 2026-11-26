# Program Perhitungan Luas & Keliling Persegi Panjang dengan Fungsi
def tampilkan_header():
    print("=== KALKULATOR GEOMETRI MODULAR ===")

def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

# Pemanggilan Fungsi Utama
tampilkan_header()
p = float(input("Masukkan Panjang (cm) : "))
l = float(input("Masukkan Lebar (cm)   : "))

hasil_luas = hitung_luas(p, l)
hasil_keliling = hitung_keliling(p, l)

print(f"\nLuas Persegi Panjang     : {hasil_luas:.2f} cm2")
print(f"Keliling Persegi Panjang : {hasil_keliling:.2f} cm")