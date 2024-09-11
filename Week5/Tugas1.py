def pola_angka():
    angka_awal = 1
    angka_akhir = 10
    
    # Loop untuk mencetak angka dari 1 ke 10
    while angka_awal <= 5:
        print(angka_awal, angka_akhir, end=" ")
        angka_awal += 1
        angka_akhir -= 1
    
    # Mulai ulang nilai awal dan akhir
    angka_akhir = 5
    
    # Loop untuk mencetak angka dari 6 ke 1
    while angka_awal <= 10:
        print(angka_awal, angka_akhir, end=" ")
        angka_awal += 1
        angka_akhir -= 1

pola_angka()
print()
