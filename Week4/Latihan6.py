import random

def main():
    # Memberikan pilihan
    pilihan = ["batu", "gunting", "kertas"]

    # Menampilkan output berupa isntruksi
    print("EEYYOO! main permainan Batu, Gunting, Kertas, yukk!.")
    print("Pilihannya ada batu, gunting, atau kertas.")

    # Pilihan pemain
    pemain = input("Masukkan pilihanmu : ").strip().lower()

    # Validasi input pemain
    if pemain not in pilihan:
        print("Pilihan yang kamu masukkan tidak valid brow!. Pilih antara batu, gunting, atau kertas.")
        return  # Menghentikan program jika input tidak valid

    # Pilihan acak dari komputer
    komputer = random.choice(pilihan)
    print(f"Komputer memilih: {komputer}")

    # Menentukan hasil permainan
    if pemain == komputer:
        hasil = "Seri!"
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        hasil = "Widiiihh! Selamat kamu menang!"
    else:
        hasil = "Yahhh! Komputer menang!"

    # Menampilkan hasil 
    print(hasil)

if __name__ == "__main__":
    main()
