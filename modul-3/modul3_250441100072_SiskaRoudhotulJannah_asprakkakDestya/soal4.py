stop = False
while stop == False:
    nama = input("Masukkan Nama Pembeli : ")
    print("----- Masukkan Daftar Barang Anda -----")

    input_barang = True
    daftar_barang = ""
    total_harga = 0

    while input_barang == True:
        barang = input("Masukkan Nama Barang : ")
        harga = int(input("Masukkan Harga Barang : "))
        jumlah = int(input("Masukkan Jumlah Barang : "))

        subtotal = harga * jumlah
        daftar_barang += f"- {barang} x{jumlah} : Rp{subtotal}\n"
        total_harga += subtotal

        stop_input = input("Apakah ada barang lain yang dibeli? (iya/tidak): ")
        print("")
        if stop_input == "tidak":
            break

    print("========================================")
    print("Nama Pembeli :", nama)
    print("Daftar Barang :")
    print(daftar_barang, harga, "")
    print("Total Harga : Rp", total_harga)
    print("========================================")

    end_program = input("Apakah ada pembeli berikutnya? (ya/tidak): ")
    if end_program == "tidak":
        stop = True
        print("Terima kasih telah berbelanja di IndoMei.")
