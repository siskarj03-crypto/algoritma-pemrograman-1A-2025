print("menghitung volume dan luas sebuah balok")

# masukkan nilai panjang, lebar, tinggi
panjang = float(input("Masukkan nilai panjang "))
lebar = float(input("Masukkan nilai lebar "))
tinggi  = float(input("masukkan nilai tinggi "))

print(type(panjang))
# menghitung volume dan luas
luas = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
volume = panjang*lebar*tinggi

print(f"Luas balok adalah {luas} cm²")
print(f"Volume balok adalah {volume} cm³")
