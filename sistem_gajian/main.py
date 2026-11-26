from modul import hitung_gaji_pokok, hitung_lembur, hitung_potongan_bpjs, cetak_slip_gaji

def main():
    print("=== SISTEM PENGGAJIAN HRD ===")
    nama_input = input("Masukkan Nama Karyawan : ")
    jabatan_input = input("Masukkan Jabatan (Manager/Staff/Teknisi) : ")
    
    try:
        jam_lembur_input = float(input("Masukkan Jam Lembur : "))
    except ValueError:
        print(">> Error: Jam lembur harus berupa angka. Dianggap 0.")
        jam_lembur_input = 0

    # Proses Pipeline
    gaji_pokok = hitung_gaji_pokok(jabatan_input)
    
    if gaji_pokok == 0:
        print(">> Error: Jabatan tidak dikenali. Silakan cek kembali.")
    else:
        upah_lembur = hitung_lembur(jam_lembur_input)
        potongan = hitung_potongan_bpjs(gaji_pokok)
        
        cetak_slip_gaji(nama_input, jabatan_input, gaji_pokok, upah_lembur, potongan)

main()