# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:19:24 2023

@author: hatice
"""



def ortalama_hesapla(satir):
    satir = satir[:-1]  #her satirin bir bilgiye denk gelmesini istediğimiz için boşlukları çıkarmamız gerekir ve bu ifade de boşlukları çıkarır. 
    liste = satir.split(":")  #ogrenci soyadinin sonunda yer alan :'dan sonraki bilgileri alacak. Yani listenin elemanlarini :'nin öncesi ve sonrasi olarak ayirdik.
    ogrenciAdi = liste[0]  #:'nin oncesi elemanlar listenin 0. elemanlari olarak sayildi
    notlar = liste[1].split(",") #:'nin sonrasi elemanlar listenin 1. elemanlari olarak sayildi. , ile notları sayıların aralarindaki , den ayirdik.
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1+not2+not3)/3
    
    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=85 and ortalama<=89:
        harf = "BA"
    elif ortalama>=80 and ortalama<=84:
        harf = "BB"
    elif ortalama>=75 and ortalama<=79:
        harf = "CB"
    elif ortalama>=70 and ortalama<=74:
        harf = "CC"
    elif ortalama>=65 and ortalama<=69:
        harf = "DC"
    elif ortalama>=60 and ortalama<=64:
        harf = "DD"
    elif ortalama>=50 and ortalama<=56:
        harf = "FD"
    else:
        harf = "FF"
        
    return ogrenciAdi + ": " +harf+ "\n"
    
    
    
def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(ortalama_hesapla(satir))
    
     
def not_gir():
    ad = input("ogrencinin adi: ")
    soyad = input("ogrencinin soyadi: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")
    
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+""+soyad+ ":" +not1+","+not2+","+not3+"\n")
    
def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(ortalama_hesapla(i))
               
        with open("sonuclar.txt","w",encoding="utf-8") as file:   #hesaplanan ortalamanin kaydedilip kaydedilen dosyayi birdahaki sefere kullanmak istediğimizde dosyanin icerisinin temiz olmasini istedigimiz icin dosyayi w ile actik.
            for i in liste:
                file.write(i)
                

while True:
    islem = input(' 1- Notlari Oku\n 2- Not Gir\n 3- Notlari kaydet\n 4- Cikis\n')

    if islem == '1':
        notlari_oku()
        
    elif islem == '2':
        not_gir()
    
    elif islem == '3':
        notlari_kaydet()
        
    else:
        break





























