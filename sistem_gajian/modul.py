def hitung_gaji_pokok(jabatan):
    jabatan = jabatan.lower()
    if jabatan == "manager":
        return 10000000
    elif jabatan == "staff":
        return 5000000
    elif jabatan == "teknisi":
        return 4000000
    else:
        return 0

def hitung_lembur(jam_lembur, tarif_per_jam=25000):
    return jam_lembur * tarif_per_jam

def hitung_potongan_bpjs(gaji_pokok):
    return gaji_pokok * 0.02

def cetak_slip_gaji(nama, jabatan, gaji_pokok, upah_lembur, potongan_bpjs):
    gaji_bersih = (gaji_pokok + upah_lembur) - potongan_bpjs
    
    print("\n" + "=" * 35)
    print("       SLIP GAJI KARYAWAN       ")
    print("=" * 35)
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan.capitalize()}")
    print("-" * 35)
    print(f"Gaji Pokok    : Rp {gaji_pokok:,.2f}")
    print(f"Upah Lembur   : Rp {upah_lembur:,.2f}")
    print(f"Potongan BPJS : Rp {potongan_bpjs:,.2f}")
    print("-" * 35)
    print(f"GAJI BERSIH   : Rp {gaji_bersih:,.2f}")
    print("=" * 35)