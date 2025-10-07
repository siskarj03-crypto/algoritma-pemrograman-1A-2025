lama_parkir = int(input("masukkan lama parkir: "))
status = (input("apakah anda VIP? (iya/tidak)"))	 
 						 
if status == "iya":				 
    biaya = 0 					 
else:						 
    if lama_parkir <= 2:			 
        biaya = 5000				 
    else:					 
        biaya = 5000 + (lama_parkir - 2) * 3000	 
 						 
if biaya > 20000:				 
        biaya = 20000				 
 						 
print(f"biaya parkir: Rp{biaya}")	 	 