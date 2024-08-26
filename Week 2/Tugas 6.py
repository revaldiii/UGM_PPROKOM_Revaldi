# Tugas Pratikum Pemograman Komputer
# by Revaldi Rifwianda
# NIM : 24/534074/SV/23973
# Senin, 19 Agustus 2024

print( " ~~~ Mengkonversi Jumlah Detik ~~~ \n")

# User diminta untuk menginputkan jumlah detik
N = int(input("Masukkan lamanya waktu dalam detik:"))

# Buatlah variable A yang berisi (60 * 60 * 24)
A = (60 * 60 * 24)

# Bagi nilai N dengan A, simpan di variabel hari
hari = (N // A)

# Kalikan nilai A dengan hari, simpan di variabel B
B = (A * hari)

# Kurangi nilai N dengan B, simpan di variabel C
C = (N - B)

# Bagi nilai C dengan (60 * 60), simpan di variabel jam
jam = (C // (60 * 60))

# Kalikan nilai jam dengan (60 * 60), simpan di variabel D
D = (jam * (60 * 60))

# Kurangi nilai C dengan D, simpan di variabel E
E = (C - D)

# Bagi nilai E dengan 60, simpan di variabel menit
menit = (E // 60)

# Modulus nilai N dengan 60, simpan di variabel detik
detik = (N % 60)

# print variabel dengan format "hari + jam + menit + detik"
print("\n" + str(N) + " detik sama dengan: " + str(hari) + " hari " + str(jam) + " jam " + str(menit) + " menit " + str(detik) + " detik", end=".")
