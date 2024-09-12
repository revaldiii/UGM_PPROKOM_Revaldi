# variabel dideklarasikan
var_nilai = 0
var_i = 1

# Perulangan FOR
for var_nilai in range(0, 10):
    print("Perulangan pertama Ke ", var_nilai)
    
    # Perulangan nested WHILE 
    while(var_i < 3):
        print(" Perulangan ke ", var_nilai, ", ", var_i)
        var_i += 1
    
    # reset (var_i)
    var_i = 1

# Di luar perulangan FOR
print("var_nilai = ", int(var_nilai) + 1, " = 10. Bernilai False")
