# Daftar untuk menyimpan data siswa
siswa = []

# Input data untuk 5 siswa
for i in range(1, 6):
    # Input Nama Siswa
    nama = input("Masukkan nama siswa ke-{}: ".format(i))
    
    while True:
        try:
            # Input Nilai Siswa
            nilai = float(input("Masukkan nilai siswa ke-{}: ".format(i)))
            # Jika nilai valid, keluar dari loop
            break
        except ValueError:
            print("Nilai harus berupa angka. Silakan coba lagi.")
    
    # Tambahkan data siswa ke daftar
    siswa.append((nama, nilai))

# Menampilkan hasil kelulusan setelah semua input
print("\nHasil Kelulusan:")
for nama, nilai in siswa:
    if nilai >= 70:
        status = "dinyatakan LULUS "
    else:
        status = "dinyatakan Tidak Lulus"
    print("Siswa {} dengan nilai {:.2f} {}".format(nama, nilai, status))
