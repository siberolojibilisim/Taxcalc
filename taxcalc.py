print("Vergi Hesaplayiciya Hosgeldiniz")
global deger
def kdvhesapla():
    while True:         
        deger = int(input("Urunun Fiyatini Giriniz : "))
        if deger == 0 :         
                print("Girdiginiz miktar gecersiz")
        else:            
            vergimiktari = int(input("Vergi Miktarini Giriniz : % "))
            Vergi=deger*vergimiktari/100
            print("Vergi Miktari " + str(Vergi))
            print("Vergi haric miktar " + str(deger-Vergi))
            break 
kdvhesapla()            