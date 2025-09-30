#harga satuan
buku_tulis = 5000
pensil = 4500

#total harga buku tulis dan pensil
total_buku_tulis = buku_tulis*3
total_pensil = pensil*2
total_harga = total_buku_tulis + total_pensil
print("total harga belanjaan Halim: ", total_harga)

# pajak
pajak = total_harga*0.1
print("pajak", pajak)

total_bayar = total_harga+pajak
print(f"Halim harus membayar ke kasir setelah diberi diskon sebesar {pajak} adalah: {total_bayar}")