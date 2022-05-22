import random
import sqlite3, os

dosya = 'musteri_bilgileri.sqlite'
dosya_mevcut = os.path.exists(dosya)
vt = sqlite3.connect(dosya)
im = vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS musteriler(Adi, Soyadi, Harcama_miktari)""")


gunSonuRaporu = []
gunlukToplamKazanc = 0
musteriKazanci = 0
kacinciMusteri = 1
saat = 10
dakika = 0
gunSonuAlindiMi = 0
#--------------------------------------------
class Musteri_Bilgi:                         
   def __init__(self,harcama_miktari): 
     self.isim = input("Adınızı Giriniz: ")                           
     self.soyad = input("Soyadınızı Giriniz: ")
     self.harcama_miktari = harcama_miktari
     
    
#--------------------------------------------
def gunSonufonk(toplamKazanc):
    print("\nGün Sonu Raporu Alınıyor...\n")
    print("\nGünlük Toplam Kazanç: {} ₺\n".format(toplamKazanc))
    for i in gunSonuRaporu:
        print(i,"\n")
    print("----Çıkış Yapılıyor...----")
#--------------------------------------------
def fotokopi_fonk(katsayi):
    try:
        adet = int(input("Kac adet istiyor: "))
        if adet >= 0:
            return adet * katsayi           
        else:
            print("Adet 0'dan büyük olmalıdır!")
            return fotokopi_fonk(katsayi)
            
    except:
        print("Lütfen sadece sayı giriniz! ")
        return fotokopi_fonk(katsayi)       
#-------------------------------------------
def pc_islem(katsayi):
    try:
        sure = int(input("Kac saat kullanmak istiyor: "))
        if sure >= 0:
            return sure * katsayi
        else:
            print("Saat 0'dan büyük olmalıdır!")
            return pc_islem(katsayi)
    except:
        print("Lütfen sadece sayı giriniz! ")
        return pc_islem(katsayi)        
#-------------------------------------------
def pc_ozellikleri():
    pcOzellik = {"Pc1": {"Ekran Kartı": "GTX 1060 Ti",
                       "İşlemci"    : "intel i9 9th",
                       "Ram"        : "8GB"},
                "Pc2" : {"Ekran Kartı": "GTX 3090",
                       "İşlemci"    : "intel i9 9th",
                       "Ram"        : "32GB"},
                "Pc3": {"Ekran Kartı": "GTX 1060 Ti",
                       "İşlemci"    : "intel i9 9th",
                       "Ram"        : "8GB"}
                 }
    try:
        pc = input("Özelliklerini görmek istediğiniz pc seçiniz (Pc1/Pc2/Pc3): ")
        print(pcOzellik[pc])
    except:
        print("----\nSadece mevcut pclerden seçiniz!----\n")
        return pc_ozellikleri()
#------------------------------------------
def oyun_al():
    oyunlar = {"GTA-V": {"Boyut": "60GB",
                         "Fiyat"    : "50₺"},
                       
                "Fallout 4" :{"Boyut": "35GB",
                              "Fiyat"    : "40₺"},
                "Forza Horizon": {"Boyut": "75GB",
                                     "Fiyat"    : "100₺"},
                 }
    for anahtar, değer in oyunlar.items():
        print("{} = {}".format(anahtar, değer))
    oyunadi = input("\nOyun Adı Giriniz: ")
    if oyunadi == "GTA-V":
        return 50
    elif oyunadi == "Fallout 4":
        return 40
    elif oyunadi == "Forza Horizon":
        return 100
    else:
        print("\nLütfen listeden bir oyun seçiniz\n")
        return oyun_al()
#------------------------------------------
print("""
İnternet Cafe sistemine Hoşgeldiniz.
Dükkan Açılıyor...
Saat: 10:00
""")

while True:
    if kacinciMusteri == 1:
        print("-----Musteri geldi-----.\n")
    if gunSonuAlindiMi == 0:
        print("""Menü:
1-Çıktı veya fotokopi almak istiyor. (1.5₺)
2-Sadece basit bilgisayar işlemleri yapmak istiyor. (Saatlik 2₺)
3-Bilgisayar oyunu oynamak istiyor. -Oyuncu Bilgisayarı- (Saatlik 5₺)
4- Pclerin özelliklerini görmek istiyor.
5- Oyun satın almak istiyor.
6- Bu ayın kazanan müşterisini gör.
""")
    elif gunSonuAlindiMi == 1:
        print("""Menü:
1-Çıktı veya fotokopi almak istiyor. (1.5₺) (Kapalı)
2-Sadece basit bilgisayar işlemleri yapmak istiyor. (Saatlik 2₺) (Kapalı)
3-Bilgisayar oyunu oynamak istiyor. -Oyuncu Bilgisayarı- (Saatlik 5₺) (Kapalı)
4- Pclerin özelliklerini görmek istiyor(Kapalı).
5- Oyun satın almak istiyor.(Kapalı)
6- Bu ayın kazanan müşterisini gör.(Kapalı)
7- Gün Sonu Raporu Al (Açık)
""")

    if gunSonuAlindiMi == 0:       
        try:
            islem = int(input("Lütfen menüden bir işlem seçiniz: "))
            if(islem <=0 or islem > 6):
                print("\n---Lütfen sadece menüden bir işlem seçiniz!---\n")
                continue
        except:
            print("\n---Sadece sayı giriniz!---\n")
            continue
    else:
        try:
            islem = int(input("Lütfen menüden bir işlem seçiniz: "))
            if(islem != 7):
                print("\n---Sadece günsonu raporu alabilirsiniz!---\n")
                continue
        except:
            print("\n---Sadece sayı giriniz!---\n")
            continue
        
    
    if islem == 1: #Fotokopi veya çıktı
        musteriKazanci = fotokopi_fonk(1.5)
        mb = Musteri_Bilgi(musteriKazanci)
        im.execute("INSERT INTO musteriler VALUES (?, ?, ?)", (mb.isim, mb.soyad, mb.harcama_miktari))
        vt.commit()
        gunlukToplamKazanc += musteriKazanci
        
            
    elif islem == 2: #Basit bilgisayar işlemleri
        musteriKazanci = pc_islem(2)
        mb = Musteri_Bilgi(musteriKazanci)
        im.execute("INSERT INTO musteriler VALUES (?, ?, ?)", (mb.isim, mb.soyad, mb.harcama_miktari))
        vt.commit()
        gunlukToplamKazanc += musteriKazanci
        
            
    elif islem == 3: # Bilgisayar Oyunu
        musteriKazanci = pc_islem(5)
        mb = Musteri_Bilgi(musteriKazanci)
        im.execute("INSERT INTO musteriler VALUES (?, ?, ?)", (mb.isim, mb.soyad, mb.harcama_miktari))
        vt.commit()
        gunlukToplamKazanc += musteriKazanci
        
    elif islem == 4:
        pc_ozellikleri()
    
    elif islem == 5:
        musteriKazanci = oyun_al()
        mb = Musteri_Bilgi(musteriKazanci)
        im.execute("INSERT INTO musteriler VALUES (?, ?, ?)", (mb.isim, mb.soyad, mb.harcama_miktari))
        vt.commit()
        gunlukToplamKazanc += musteriKazanci
    
    elif islem == 6:
        im.execute("""SELECT * FROM musteriler ORDER BY Harcama_miktari DESC""")
        veriler = im.fetchone()
        print(veriler)
        
    elif(islem == 7 and gunSonuAlindiMi == 1): #Gün Sonu Raporu
        gunSonufonk(gunlukToplamKazanc)
        break
    
    musteridenGelenKazanc = "{}. Müşteriden Gelen Kazanç: {} ₺ , İşlem Saati ---> {}:{}".format(kacinciMusteri, musteriKazanci,saat,dakika)
    gunSonuRaporu.append(musteridenGelenKazanc)
    
    cikis = input("Dükkânı kapatıp çıkmak istiyor musun? (y/n):  ")
    if cikis == 'y':
        print("\n----Gün Sonu Raporunu almanız gerekiyor! -----\n")
        gunSonuAlindiMi = 1
        continue
        
        
    else:
        yeniMusteriGelmeSuresi = random.randint(15, 30)
        dakika += yeniMusteriGelmeSuresi
        if(dakika >= 60):
            dakika = dakika % 60
            saat += 1
        kacinciMusteri = kacinciMusteri + 1
        print("\n-----{} dakika geçti ve Yeni Müşteri geldi. Saat şu an {}:{}-----\n".format(yeniMusteriGelmeSuresi,saat,dakika))
       


