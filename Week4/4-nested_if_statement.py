jenis_kelamin = str(input("Jenis kelamin = "))

if jenis_kelamin.lower() in ['pria', "laki laki", "cowok"]:
    umur = int(input("Umur = "))
    if (umur >= 25):
        print (str(jenis_kelamin), " boleh menikah")
    else:
        print (str(jenis_kelamin), " boleh menikah")
elif jenis_kelamin.lower() in ['wanita', "perempuan", "cewek"] :
    umur = int(input("Umur = "))
    if (umur >= 20):
        print (str(jenis_kelamin), " boleh menikah")
    else:
        print (str(jenis_kelamin), " tidak boleh menikah")
else:
    print ("Jenis kelamin anda tidak terdaftar") 