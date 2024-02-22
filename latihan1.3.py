inputan = (input("Masukkan suhu tubuh anda: "))

try:
    suhu = int(inputan)
    if suhu >= 38:
        print ("Anda dinyatakan demam!")
    elif suhu < 38:
        print ("Anda dinyatakan tidak demam!")
    else:
        print ("Anda dinyatakan tidak demam!")

except:
    print ("Format yang anda masukkan salah!")
