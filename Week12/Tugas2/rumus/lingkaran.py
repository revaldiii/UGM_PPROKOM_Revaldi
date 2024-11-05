import tampilan.menu as menu

def lingkaran():
    print("Menghitung Luas Lingkaran")
    r = float(input("Masukkan Jari-Jari: "))
    luas = 3.14 * (r ** 2)
    print("Luas Lingkaran adalah", luas)
    print()
    back = input("Coba lagi [Y/N]? ").upper()
    if back == "Y":
        menu.menu()
    else:
        exit()