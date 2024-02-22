inputanrrr = input("Masukkan bulan: ")

try:
    bulan = int(inputanrrr)
    if bulan == 1:
     print (31)
    elif bulan == 2:
     print (29)
    elif bulan == 3:
        print (31)
    elif bulan == 4:
        print (30)
    elif bulan == 5:
        print (31)
    elif bulan == 6:
        print (30)
    elif bulan == 7:
        print (31)
    elif bulan == 8:
        print (31)
    elif bulan == 9:
        print (30)
    elif bulan == 10:
        print (31)
    elif bulan == 11:
        print (30)
    elif bulan == 12:
        print (31)
    else:
        print ("bulan yang anda masukkan harus antara bulan 1-12!")
except:
 print ("format salah yang anda masukkan salah!")

