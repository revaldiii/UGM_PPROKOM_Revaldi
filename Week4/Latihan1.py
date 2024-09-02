lulus = "Selamat Anda Berhak Mendapatkan Sim Anda"
gagal = "Maaf, Anda tidak berhak mendapatkan sim anda\nSilahkan Coba lagi Bulan atau tahun Depan"
dini = "Maaf, Anda belum berhak mengikuti ujian SIM. Terima kasih"

umur = int(input("Masukan Umur Anda = "))

if(umur>17) :
    nilai = int(input("Masukan Nilai Tes Anda = "))
    if(nilai<60) :
        print()
        print(gagal)
    else :
        print()
        print(lulus)
else :
    print()
    print(dini)
