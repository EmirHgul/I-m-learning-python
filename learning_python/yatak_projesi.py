# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 13:25:30 2023

@author: hatice
"""


#Yatak turlerini bir liste icerisinde barindiralim.

yatak_turu = ["Yaylı yatak", "Köpük yatak", "Hibrit yatak", "Lateks yatak"]
destek = ["Orta","Yüksek"]
hava_gecirgenligi = ["Düşük","Orta","Yüksek"]
hareket_aktarimi = ["Düşük","Orta","Yüksek"]
maliyet = ["Düşük","Orta","Yüksek","Çok yüksek"]
dogallik = ["Düşük","Orta/Düşük","Orta","Yüksek"]


def yas():
    yas = input("Lütfen yaşınızı giriniz: ")
    yas = int(yas)   #kullanicinin girdigi degeri int'a cevirdik
    
    if yas >= 0 and yas <= 17:
        return maliyet[0]
    elif yas >= 18 and yas <= 35:
        return maliyet[1] 
    elif yas >= 36 and yas <= 55:
        return maliyet[2]
    else:
        return maliyet[3]

yas_maliyet = yas()
print(yas_maliyet)        

    







































