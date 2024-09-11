awal = int(input("Masukan jumlah saldo awal kamu\t: "))
sisa = awal  # Jika tidak memiliki pengeluaran

while True:
    pengeluaran = int(input("Jumlah pengeluaran hari ini (Ketik 0 jika ingin keluar): "))

    if pengeluaran == 0:  # Untuk berhenti
        print("Sisa saldo kamu =", sisa)  # Menampilkan sisa saldo jika di berhentikan
        break

    # Periksa apabila pengeluaran lebih besar dari sisa saldo
    while pengeluaran > sisa:
        print("Saldo kamu tidak cukup")
        print("Sisa saldo kamu", sisa)
        pengeluaran = int(input("Masukan pengeluaran yang valid dong(Ketik 0 jika ingin keluar): "))
        if pengeluaran == 0:  # Untuk berhenti jika pengguna memutuskan
            print("Sisa saldo kamu =", sisa)  # Sisa saldo jika di berhentikan
            break
        if pengeluaran <= sisa:
            break  # Keluar dari loop saat pengeluaran valid

    if pengeluaran == 0:  # Cek lagi setelah keluar dari loop jika saldo cukup
        break

    sisa -= pengeluaran

    # Menampilkan sisa saldo setelah pengeluaran
    print("Sisa saldo kamu setelah pengeluaran:", sisa)
    
    # Jika saldo habis, program berhenti
    if sisa == 0:
        print("Maaf, saldo kamu sudah habis.")
        break
