# jumlah merah dan biru
merah = 8
biru = 6
total = biru + merah

# jumlah ambil
ambil = 3

# hitung faktorial total, ambil, sisa
faktorian_total = 1
for i in range(1, total+1):
    faktorian_total *= i
    
faktorian_ambil = 1
for i in range(1, ambil+1):
    faktorian_ambil *= i
    
faktorian_sisa = 1
for i in range(1, total-ambil+1):
    faktorian_sisa *= i

# rumus kombinasi C(n,r) = n! / (r!*(n-r)!)
jumlah_kombinasi = faktorian_total / (faktorian_ambil*faktorian_sisa)
print("jumlah kombinasi yang mungkin: ", jumlah_kombinasi)