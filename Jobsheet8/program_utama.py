# File Utama: 6_3_program_utama.py
import modul_akademik as akd

print("=== SISTEM PENILAIAN MODULAR POLINES ===")
nama = input("Nama Mahasiswa : ")
tgs = float(input("Nilai Tugas    : "))
uts = float(input("Nilai UTS      : "))
uas = float(input("Nilai UAS      : "))

na = akd.hitung_nilai_akhir(tgs, uts, uas)
grade = akd.konversi_grade(na)

print("-" * 35)
print(f"Mahasiswa   : {nama}")
print(f"Nilai Akhir : {na:.2f}")
print(f"Predikat    : {grade}")
