# Inisialisasi Set dengan data NIM duplikat
nim_hadir = {"201", "202", "201", "203", "202"}

# Menambah data baru
nim_hadir.add("204")

# Menampilkan hasil (Set otomatis membuang duplikat)
print("Daftar NIM Unik yang Hadir:", nim_hadir)

# Operasi Irisan (Intersection)
admin_lab = {"Andi", "Budi"}
dosen = {"Budi", "Cici"}
keduanya = admin_lab.intersection(dosen)
print("Orang yang bertugas sebagai Admin sekaligus Dosen:", keduanya)
