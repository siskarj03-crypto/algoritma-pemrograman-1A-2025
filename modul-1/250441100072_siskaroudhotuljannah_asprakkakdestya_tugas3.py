print("="*50)
print("nama: siska roudhotul jannah")
print("nim: 250441100072")
print("="*50)

total = 0
for i in range(1, 15):        
    for j in range(i+1, 15):  
        for k in range(j+1, 15):  
            total += 1

print("Total kombinasi:", total)