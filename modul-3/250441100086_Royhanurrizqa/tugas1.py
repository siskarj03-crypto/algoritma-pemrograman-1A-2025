n = int(input("Masukkan nilai n: "))
print("bilangan perima dari 1 - n adalah :")
for i in range(2, n + 1):
    prima = True
    for j in range(2, i):  
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")