import tampilan.menu as menu

def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = float(input("Masukkan Panjang: "))
    l = float(input("Masukkan Lebar: "))
    luas = p * l
    print("Luas Persegi Panjang adalah", luas)
    print()
    back = input("Coba lagi [Y/N]? ").upper()
    if back == "Y":
        menu.menu()
    else:
        exit()