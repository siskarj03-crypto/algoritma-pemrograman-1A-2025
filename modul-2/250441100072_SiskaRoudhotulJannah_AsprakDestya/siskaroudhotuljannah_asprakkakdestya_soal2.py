tiket = 50000

umur = int(input("masukkan umur: "))
status = (input("apakah pelajar? (iya/tidak) ", ))
kartu_pelajar = (input("apakah membawa kartu pelajar? (iya/tidak) ", ))
hari = input("masukkan hari: ")

if umur < 12:
        diskon = 0.5
elif status == "iya" and kartu_pelajar == "iya":
     diskon = 0.3
elif hari == "selasa":
     diskon = 0.2
else:
    diskon = 0

promo = int(diskon * 100)
print("anda mendapatkan diskon", promo, "%")
harga = tiket * (1 - diskon)
print("harga tiket: ", harga)
