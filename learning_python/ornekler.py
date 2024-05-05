""" 0rnek1

ogrenciler = {}

number = input("ogrenci no: ")
name = input ("ogrenci ad: ")
surname = input ("ogrenci soyadÄ± : ")
phone = input ("ogrenci tel : ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "tel" : phone
    }

print(ogrenciler)

"""




""" 0rnek2 3'ÃN KATLARI

sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)
"""




"""Ornek3 SAYILAR LÄ°STESÄ°NDEKÄ° ELEMANLARIN TOPLAMI

sayilar = [1,3,5,7,9,12,19,21]
toplam = 0
for sayi in sayilar:
    toplam += sayi 
print('toplam:',toplam)

"""




"""Ornek4 TEK SAYILARIN KARESÄ°

sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar:
    if (sayi%2==1):   #tek sayÄ±larÄ± seÃ§er
        print(sayi**2)
        
"""




""" Ornek5 KARAKTER SAYISI 5'DEN KÃÃÃK OLAN ÅEHÄ°RLER

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
for sehir in sehirler:
    if (len(sehir) <=5):
        print(sehir)
        
"""




""" Ornek6 TOPLAM ÃRÃN FÄ°YATI
urunler = [
    {"name":"samsung S6","price": "3000"},
    {"name":"samsung S7","price": "4000"},
    {"name":"samsung S8","price": "5000"},
    {"name":"samsung S9","price": "6000"},
    {"name":"samsung S10", "price": "7000"}
    ]

toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])  #urunler listesindeki priceÄ± verir
    toplam += fiyat
print("toplam Ã¼rÃ¼n fiyatÄ±:" ,toplam)

"""




""" Ornek7 FÄ°YATI EN FAZLA 5000 OLAN ÃRÃNLER
urunler = [
    {"name":"samsung S6","price": "3000"},
    {"name":"samsung S7","price": "4000"},
    {"name":"samsung S8","price": "5000"},
    {"name":"samsung S9","price": "6000"},
    {"name":"samsung S10", "price": "7000"}
    ]

toplam = 0
for urun in urunler:
    if (int(urun["price"]) <= 5000):  #urunler listesindeki priceÄ± verir
        print("fiyatÄ± en fazla 5000 olan Ã¼rÃ¼nler:",urun["name"])

"""





"""Ornek8 sayilari yazdirdik

sayilar = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
"""




"""Ornek9  baslangic ve bitis değeri kullanicidan istenilen sayilar arasindaki tek sayilari yazdirdik.
baslangic = int(input("baslangic: "))
bitis = int(input("bitis: "))

i = baslangic
while i < bitis:
    i += 1
    if (i%2 == 1):
        print(i)
"""




"""Ornek10 sayilari azalan şekilde yazdirma
i = 100

while i > 0:
    print(i)
    i -= 1
"""




"""Ornek11 kullanicidan aldiğimiz sayilari siraladik

numbers = []

i = 0
while i<5:
    sayi = int(input("sayi: "))
    numbers.append(sayi)
    i += 1   
numbers.sort()
print(numbers)
"""





"""Ornek12

urunler = []

adet = int(input("Kac urun eklemek istiyorsunuz: "))
i = 0

while(i<adet):
    name = input("urun ismi: ")
    price = input("urun fiyati: ")
    urunler.append({
        "name": name,
        "price": price
    })
    i+=1
    
for  urun in urunler: 
    print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]}')
    
"""







"""Ornek13  fonksiyon kullanarak gönderilen bir kelimeyi belirtilen kez ekranda yazdırma 

def yazdir(kelime, adet):
    print(kelime * adet)
    
yazdir("merhaba\n", 10)

"""





"""Ornek14 Kendine verilen parametreleri listeye çeviren fonksiyon
def listeyeCevir(*params):
    liste = []
    
    for param in params:
        liste.append(param)
    
    return liste
result: list()
result = listeyeCevir(10,20,30,"Merhaba")

print(result)

"""






"""Ornek15 asal sayilari yazdirabilen bir fonksiyon

def asalSayiBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2):
            if sayi > 1:
                for i in range(2, sayi):
                    if (sayi % i == 0):
                        break
                else:
                    print(sayi)

sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

asalSayiBul(sayi1, sayi2)

"""





''' Ornek 16 # LISTE ELEMANLARI ICINDEKI SAYISAL DEGERLERI BULUNUZ

liste = ["1","2","5a","10z","bac","10","50"]

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue   #continue ile hatali olan yani int turunden olmayan degerleri gorup atlayarak yazdirmaya devam etti.
        
'''






''' Ornek17 # q'ya basildigi zaman donguden cikan bir kod blogu

while True:
    sayi = input('sayi: ')
    if sayi == 'q':
        break

    try:
        result = float(sayi)
        print('girdiginiz sayi: ', result)
    except ValueError:
        print('gecersiz sayi')
        continue

'''




''' Ornek 18
# Girilen parola icin turkce karakter hatasi verme
# parola iki kez girilir

parola = input('parola')


def checkPassword(parola):

    turkce_karakterler = 'ğĞÜüİŞşÖöÇçı'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola turkce kaakter iceremez')
        else:
            pass
    
    print('gecerli parola')

parola = input('parola')
       
try:
    checkPassword(parola)
except TypeError as err:
    print(err)
   
'''    





''' Ornek19
# SAYILARIN FAKTORIYELINI YAZDIRDIK

def faktoriyel(x):
     x = int(x)
     
     if x < 0:
         raise ValueError('Negatif deger')

     result = 1

     for i in range(1, x+1):
        result *= i
        
     return result
 
for x in [5,10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)
    
'''











