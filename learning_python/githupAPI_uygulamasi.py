import requests

#API BAGLANTİSİYLA İLGİLİ HATA ALİYORUM REQUEST MODULU GİTHUP API UYGULAMASI VIDEOSU

class Githup:
    def __init__(self):
        self.api_url = "https://api.githup.com"
        
    def getUser(self,username):
        response = requests.get(self.api_url+"/users/"+ username)
        return response.json()        

githup = Githup()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4 - Exit\nSeçim: ")

    if secim == "4":
        break
    elif secim == "1":
        username=input("username: ")
        result = githup.getUser(username)
        print(f'name: {result["name"]} public repos: {result["public_repos"]} follower: {result["followers"]} ')
    elif secim == "2":
        pass
    elif secim == "3":
        pass
    










