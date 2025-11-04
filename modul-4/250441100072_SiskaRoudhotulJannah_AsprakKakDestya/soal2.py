total_gaji = 0
total_lembur = 0
bonus_shift = 0

for i in range(1, 7):
    print(f"hari ke {i}")

    while True:
             try:
                  jam_lembur = int(input("Masukkan jumlah jam lembur hari ini: "))
                  if jam_lembur < 0:
                      print("Jam lembur tidak boleh negatif. Coba lagi.")
                      continue
                  break
             except ValueError:
                 print("Input tidak valid! Masukkan angka.")

    while True:
         shift_malam = input("apakah shift malam? (y/n):")
         if shift_malam not in ("y", "n"):
              print("input tidak valid! masukkan 'y' atau 'n' ")
         else:
              break

    gaji_harian = 100000

    if 1 >= jam_lembur <= 3:
         gaji_harian += jam_lembur * 25000
         total_lembur += jam_lembur
    elif jam_lembur == 4:
         gaji_harian += 100000
         total_lembur += jam_lembur
    elif jam_lembur == 6:
         gaji_harian += 200000
         total_lembur += jam_lembur
    elif jam_lembur == 8:
         gaji_harian += 300000
         total_lembur += jam_lembur
    elif jam_lembur > 8:
         print("lembur melebihi batas. tidak dihitung")

    if shift_malam == "y": 
         gaji_harian += 50000
         bonus_shift += 50000
    
    total_gaji += gaji_harian
    print(f"gaji hari ke {i} : Rp{gaji_harian}")

print("\n=== Hasil mingguan pak Wowo ===")
print(f"total jam lembur :{total_lembur} jam")
print(f"total bonus shift malam : Rp{bonus_shift}")
print(f"total gaji seminggu : Rp{total_gaji}")