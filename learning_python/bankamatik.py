# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:25:11 2023

@author: hatice
"""



#BANKAMATİK UYGULAMASI


hesapHatice = {
    "ad" : "Hatice AYVA",
    "hesapNo" : "123456",
    "bakiye" : 3000,
    "ekHesap" : 2000
    }


hesapEmirhan = {
    "ad" : "Emirhan GÜL",
    "hesapNo" : "123456",
    "bakiye" : 3000,
    "ekHesap" : 5000
    }


def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')
    
    
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
        
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanilsin mi (e/h)")
            
            if ekHesapKullanimi == "e":
               
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"] 
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar 
                
                print("paranizi alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap["hesapNo"] } nolu hesabinizda {hesap["bakiye"]} bulunmaktadir.')
                
        else:
            print("uzgunuz bakiye yetersiz")
            bakiyeSorgula(hesap)
            
            
def bakiyeSorgula(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabinizda {hesap["bakiye"]} TL bulunmaktadir. Ek hesap limitiniz ise {hesap["ekHesap"]} TL bulunmaktadir.')
            
                
paraCek(hesapEmirhan, 3000) 
bakiyeSorgula(hesapEmirhan)

print("*******************")

paraCek(hesapEmirhan, 3000)
bakiyeSorgula(hesapEmirhan)

































