'''
Menampilkan Nilai Huruf Dari Bilangan Bulat 0 - 100
'''
jwb="y"
while jwb=="y" or jwb=="Y":
    n=1
    while int(n) > 0 and  int(n) <= 100:
        print("========================")
        print("         Cek Nilai     ")
        print("========================")
        n=input("Masukkan Nilai = ")
        if int(n) > 0 and  int(n) <= 100:
            if int(n) >= 91:
                sts="A"
            elif int(n) >=81:
                sts= "B"
            elif int(n) >=71:
                sts= "C"
            else:
                sts="D"
            print(sts)
            jwb=input("Masukkan Nilai Lagi ? y/t = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=print("Masukkan Angka 1 - 100 saja !!!")
            break