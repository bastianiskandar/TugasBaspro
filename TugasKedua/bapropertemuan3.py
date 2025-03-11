nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")

gaji = 0
bonus = 0

if status == "Pegawai Tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
elif status == "Honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000

gaji_total = gaji + bonus

print("\n===== INFORMASI GAJI KARYAWAN =====")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Status: {status}")
print(f"Golongan: {golongan}")
print(f"Gaji Pokok: Rp {gaji:,}".replace(",", "."))
print(f"Bonus: Rp {bonus:,}".replace(",", "."))
print(f"Gaji Total: Rp {gaji_total:,}".replace(",", "."))
print("==================================")