print("="*50)
print("nama: siska roudhotul jannah")
print("nim: 250441100072")
print("="*50)

panjang = int(input("masukkan panjang: "))
lebar = int(input("masukkan lebar: "))
tinggi = int(input("masukkan tinggi: "))

volume = (panjang * lebar * tinggi)
print("jadi panjangnya adalah: ", volume)

luas_permukaan = ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print("jadi luas permukaan adalah: ", luas_permukaan)