# Daftar nilai ujian
nilai = [78, 85, 90, 65, 88, 72, 95, 80]

# 1. Urutkan dari terkecil ke terbesar
nilai.sort()

# 2. Perhitungan menggunakan built-in functions
jumlah_mahasiswa = len(nilai)
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / jumlah_mahasiswa

# 3. Menampilkan hasil
print("Daftar Nilai Terurut :", nilai)
print("Jumlah Mahasiswa     :", jumlah_mahasiswa)
print("Nilai Tertinggi      :", nilai_tertinggi)
print("Nilai Terendah       :", nilai_terendah)
print(f"Rata-rata Kelas      : {rata_rata:.2f}")