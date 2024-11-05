import tampilan.menu as menu

def segitiga():
    print("Menghitung Luas Segitiga")
    a = float(input("Masukkan Alas: "))
    t = float(input("Masukkan Tinggi: "))
    luas = (a * t) / 2
    print("Luas Segitiga adalah", luas)
    print()
    back = input("Coba lagi [Y/N]? ").upper()
    if back == "Y":
        menu.menu()
    else:
        exit()