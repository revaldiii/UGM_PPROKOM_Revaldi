# import module matematika math
import math

# Input koefisien dari pengguna
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("Masukkan c: "))

# hitung diskriminan d
d = (b ** 2) - (4 * a * c)

# cek nilai diskriminan
if d < 0:
    print("Persamaan tidak memiliki solusi real.")
elif d == 0:
    x = -b / (2 * a)
    print("Persamaan memiliki satu solusi ganda:", x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Solusinya adalah {0} dan {1}".format(x1, x2))
