jumlah = int(input("masukkan jumlah baris lampu: "))

for baris in range(1, jumlah+1):
    jumlah_lampu = int(input("masukkan jumlah lampu: "))
    for lampu in range(1, jumlah_lampu+1):
        if lampu % 3 == 0:
            print(f"lampu ke {lampu} pada baris {baris} rusak")
        else:
            print(f"lampu ke {lampu} pada baris {baris} menyala")

if baris == jumlah:
    print("periksa sambungan daya utama\n")
else:
    print()
