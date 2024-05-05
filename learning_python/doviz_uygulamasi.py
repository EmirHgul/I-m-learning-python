# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:13:42 2023

@author: hatice
"""





import requests
import json

#BU KOD HATA VERIYOR BUNUN SEBEBININ API ADRESI OLDUGUNU DUSUNUYORUM.
api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("bozulan doviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsun?"))

result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz, miktar * result["rates"][alinan_doviz],alinan_doviz))


















