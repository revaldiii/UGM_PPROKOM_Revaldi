# variabel dideklarasikan
var_nilai = 0
var_i = 1

# Perulangan WHILE
while (var_nilai < 10):
    print("Perulangan pertama Ke ", var_nilai)
    
    # Perulangan nested WHILE 
    while (var_i < 3):
        print(" Perulangan ke ", var_nilai, ", ", var_i)
        var_i += 1  # Menambah nilai var_i setiap kali perulangan
    
    # Diluar perulangan var_i
    var_i = 1  # Mengembalikan var_i ke 1 untuk perulangan selanjutnya
    var_nilai += 1  # Menambah nilai var_nilai setiap kali perulangan pertama selesai

# Diluar perulangan var_nilai
print("var_nilai = ", int(var_nilai), " = 10. Bernilai False")
