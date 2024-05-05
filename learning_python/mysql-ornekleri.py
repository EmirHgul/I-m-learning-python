import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Hat11082002"   
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")



MYSQL E BAĞLANMADA HATA ALIYORUM. 
BU YÜZDEN OLUŞTURDUĞUM TABLOLAR MYSQL E GELMİYOR.
HATAYI SOR ÖYLE DEVAM ET.
VİDEO 22.9 DA KALDIM



print(mydb)



