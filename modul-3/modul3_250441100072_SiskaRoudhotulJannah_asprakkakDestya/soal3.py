vocal = "aiueo"
kata = 0
jumlah_vokal = 0
huruf = input("masukkan kata: ")
jumlah_kata = 1

for i in huruf:
    if i in vocal:
        print(i, "adalah huruf vokal")
        jumlah_vokal += 1
    elif i != " ":
        print(i, "adalah huruf konsonan")
        kata += 1
    else:
        jumlah_kata += 1

print("jumlah huruf vokal:", jumlah_vokal)
print("jumlah huruf konsonan:", kata)
print("jumlah kata:", jumlah_kata)