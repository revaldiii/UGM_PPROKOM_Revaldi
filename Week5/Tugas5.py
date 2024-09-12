# Deklarasi variabel
var_nilai = 0
var_i = 1

# Perulangan FOR pertama
for var_nilai in range(0, 10):
    print("Perulangan pertama ke-", var_nilai)
    
    # Perulangan FOR kedua (bersarang)
    for var_i in range(1, 3):
        print(" Perulangan ke-", var_nilai, ",", var_i)
    
    # Kembali set var_i menjadi 1 setelah perulangan var_i selesai
    var_i = 1

# Di luar perulangan var_nilai
print("var_nilai =", int(var_nilai) + 1, "= 10. Bernilai False")
