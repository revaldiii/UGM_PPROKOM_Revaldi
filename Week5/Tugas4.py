# Program untuk menghitung rata-rata dari banyak data yang ditentukan oleh user

# Meminta user untuk memasukkan jumlah data
jumlah_data = int(input("Masukkan jumlah data: "))

# Inisialisasi variabel untuk menyimpan total
total = 0

# Loop untuk meminta user memasukkan setiap nilai data
for i in range(1, jumlah_data + 1):
    nilai = float(input(f"Masukkan nilai data ke-{i}: "))
    total += nilai  # Menambahkan nilai ke total

# Menghitung rata-rata
rata_rata = total / jumlah_data

# Menampilkan hasil rata-rata
print(f"Rata-rata dari {jumlah_data} data yang dimasukkan adalah: {rata_rata:.2f}")
