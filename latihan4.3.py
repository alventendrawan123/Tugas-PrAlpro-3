sisi1 = input("Masukkan sisi 1: ")
sisi2 = input("Masukkan sisi 2: ")
sisi3 = input("Masukkan sisi 3: ")

try:
    sisi1 and sisi2 and sisi3 == int(sisi1 and sisi2 and sisi3)
    if sisi1 == sisi2 == sisi3:
        print ("3 sisi sama")
    elif sisi1 == sisi2 != sisi3:
        print ("2 sisi sama")
    elif sisi2 == sisi3 != sisi1:
        print ("2 sisi sama")
    elif sisi1 == sisi3 != sisi2:
        print ("2 sisi sama")
    else:
        print ("tidak ada sisi yang sama")
except:
    print ("format yang anda masukkan salah!")