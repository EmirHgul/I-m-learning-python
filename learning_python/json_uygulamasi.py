# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 18:52:54 2023

@author: hatice
"""
 


import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email      
        
class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False   #daha once giris yapmis mi yapmamis mi onu burada soyleriz
        self.currentUser = {}     #kullanici login olmussa bilgileri buraya aktarilacak ve sonrasinda bilgileri buradan alinacak 
        
        #asagidaki islem ile kullanici bilgilerini json dosyasi uzerinden uygulamaya aktarmak istiyoruz:
        self.loadUsers()
        
    def loadUsers(self):
        if os.path.exists("user.json"):         #"user.json" isimli dosya var mı diye kontrol ettik.
            with open("users.json","r",encoding="utf-8") as file:       #eger vaar ise bu dosya okuma formatında acılsın.
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user["username"], password=user["password"], email=user["email"])
                    self.users.append(newUser)
            print(self.users)
                    
    
    #register kayit bolumu 
    def register(self, user: User):    #disaridan gelecek olan user bilgisini burada tanimladik.
        self.users.append(user)        #kaydedilen kisiyi users listesini ekleme yapacagiz.
        self.savetoFile()              #kayitlari dosyaya kaydedecegiz.
        print("Kullanıcı oluşturuldu.")
        
        
    def login(self,username,password):
        if self.isLoggedIn:
            print("zaten login oldunuz")
        else:
            for user in self.users:
                if user.username == username and user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("login yapıldı.")
                    break
                
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Çıkış yapıldı")
            
    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print("giriş yapılmadi")
            
    
    def savetoFile(self):
        list = []
        
        for user in self.users:
            list.append(json.dumps(user.__dict__))      #hata almamak icin user verisini  dict,sozluk, donusturme islemi yaptık  
        
        with open('users.json','w') as file:
            json.dump(list, file)                     #yukarıda olusturup sozluge cevirdigimiz users listesi dosyaya kaydadilecek. 
    
repository = UserRepository()
    
    
while True:
    print("Menü".center(50,'*'))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n  Seçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
      
            user = User(username=username, password=password, email=email)   #user bilgisi olusturduk.
            repository.register(user)       #user bilgisini dosya islemleri icin repository'e aktardik. 
        
            
        
        elif secim == "2":
            if repository.isLoggedIn:
                print("zaten login oldunuz")
            else:
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)
         
        elif secim == "3":
            repository.logout()
            
            
        elif secim == "4":
            repository.identity()
        
        else:
            print("yanlış seçim")
        



































