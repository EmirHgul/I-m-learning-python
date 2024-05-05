#BU KODLARDA HATA ALIYORUM  
#BTK AKADEMİ https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877
#Kütüphanede tekrar denedim ve bu sefe çalıştı bağlantıdan kaynaklı olabilir kodlarda hata yok :D

from githubUserInfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)      #2saniyede yüklensin.
                                            
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
                                                
        time.sleep(1)     #1 saniye uyuttuk
                                            
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[13]").send_keys(self.password)
        
github = Github(username, password)
github.signIn()    
    
 




















