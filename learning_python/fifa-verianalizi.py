import pandas as pd

df = pd.read_csv("kl.csv",encoding="iso-8859-1")

# ilk 10 kaydı getirme
result = df.head(10)

# toplam kaç kayıt var?
result = len(df.index)

# tüm oyuncuların toplam maaş ortalaması
result = df["Wage"].mean()   #bizim verisetimizde burada hata aldık çünkü maaşın tamamı sayısal olarak yazılmamış 100k şeklinde yazılmış

# en yüksek maaş 
result = df["Wage"].max()      # yine numeric karakter hatası verdi.

# en yüksek maaşı alan oyuncu 
result = df[df["Wage"]==df["Wage"].max()]["Name"]      #numeric hatası verir

# yaşı 20-25 arasında olan oyuncuların isimlerini ve oynadıkları takımı azalan şekilde getirme
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Nationality","Age"]].sort_values("Age",ascending=False)
              
# L.Messi isimli oyuncunun ırkı

result = df[df["Name"] == "L.Messi"]["Nationality"]



print(result)








