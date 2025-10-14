pin = 25072
kesempatan = 3
while kesempatan > 0:
    user = int(input("masukkan pin anda: "))
    if user == pin:
        print("pin anda benar")
        break
    else:
         kesempatan -= 1
    print("pin anda salah")
    if kesempatan == 0:
        print("Akses ditolak, kartu diblokir")