awal = int(input("Masukan saldo awal\t: "))
sisa = awal  # Bila tidak ada pengeluaran

while True:
    pengeluaran = int(input("Masukan pengeluaran hari ini (-1 untuk keluar): "))

    if pengeluaran == -1:  # Untuk berhenti
        print("Sisa saldo =", sisa)  # Sisa bila di berhentikan
        break

    # Cek jika pengeluaran lebih besar dari sisa saldo
    while pengeluaran > sisa:
        print("Saldo tidak cukup")
        print("Sisa saldo", sisa)
        pengeluaran = int(input("Masukan pengeluaran yang valid (-1 untuk keluar): "))
        if pengeluaran == -1:  # Untuk berhenti jika pengguna memutuskan
            print("Sisa saldo =", sisa)  # Sisa bila di berhentikan
            break
        if pengeluaran <= sisa:
            break  # Keluar dari loop saat pengeluaran valid

    if pengeluaran == -1:  # Cek lagi setelah keluar dari loop jika saldo cukup
        break

    sisa -= pengeluaran

    # Tampilkan sisa saldo setelah pengeluaran
    print("Sisa saldo setelah pengeluaran:", sisa)
    
    # Jika saldo habis, program berhenti
    if sisa == 0:
        print("Saldo habis.")
        break
