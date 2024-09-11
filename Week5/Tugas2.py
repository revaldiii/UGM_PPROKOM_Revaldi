awal = int(input("Masukan saldo awal\t: "))
sisa = awal  # Bila tidak ada pengeluaran

while True:
    pengeluaran = int(input("Masukan pengeluaran hari ini (-1 untuk keluar): "))

    if pengeluaran == -1:  # Untuk berhenti
        print("Sisa saldo =", sisa)  # Sisa bila di berhentikan
        break

    sisa -= pengeluaran

    if sisa < 0:
        print("Saldo tidak cukup")
        print("Sisa saldo", sisa + pengeluaran)  # Mengembalikan saldo ke nilai sebelum pengeluaran
        break
    
    # Tampilkan sisa saldo setelah pengeluaran
    print("Sisa saldo setelah pengeluaran:", sisa)
    
    # Jika saldo habis, program berhenti
    if sisa == 0:
        print("Saldo habis.)
        break
