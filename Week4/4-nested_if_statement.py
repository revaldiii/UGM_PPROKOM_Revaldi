jenis_kelamin = str(input("Jenis kelamin = "))
umur = int(input("Umur = "))

if jenis_kelamin.lower() == 'pria':
    if (umur >= 25):
        print ("Pria boleh menikah")
    else:
        print ("Pria tidak boleh menikah")
elif jenis_kelamin.lower() == 'wanita':
    if (umur >= 20):
        print ("Wanita boleh menikah")
    else:
        print ("Wanita tidak boleh menikah")
else:
    print ("Jenis kelamin anda tidak terdaftar") 
