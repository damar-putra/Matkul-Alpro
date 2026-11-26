def cek_saldo(saldo):
    print(f"Saldo Anda saat ini: Rp {saldo:,.2f}")

def setor_tunai(saldo, nominal):
    if nominal <= 0:
        print(">> Error: Nominal setor harus lebih dari 0.")
        return saldo
    saldo_baru = saldo + nominal
    print(f"Setor tunai berhasil: Rp {nominal:,.2f}")
    return saldo_baru

def tarik_tunai(saldo, nominal):
    if nominal < 50000:
        print(">> Error: Minimal penarikan adalah Rp 50.000.")
        return saldo
    if nominal > saldo:
        print(">> Error: Saldo tidak mencukupi.")
        return saldo
    
    saldo_baru = saldo - nominal
    print(f"Tarik tunai berhasil: Rp {nominal:,.2f}")
    return saldo_baru