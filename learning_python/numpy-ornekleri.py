import numpy as np

# (10, 15, 30, 45, 60) değerlerine sahip numpy dizisi oluşturma

result = np.array([10, 15, 30, 45, 60])

# 5-15 sayıları arasında numpy dizisi oluşturma

result = np.arange(5,15)

# 50 ile 100 arası beşer beşer artan dizi

result = np.arange(50,100,5)

# 10 elemanlı sıfırlardan oluşan bir dizi oluşturma

result = np.zeros(10)

# 10 elemanlı birlerden oluşan bir dizi oluşturma

result = np.ones(10)

# 0-100 arası eşit aralıklı 5 sayı üretme

result = np.linspace(0,100,5)

# 10-30 arası rastgele 5 sayı üretme

result = np.random.randint(10,30,5)

# -1 ile 1 arası 10 adet sayı üretme

result = np.linspace(-1,1,10)

# 10 ile 20 arası sayılar içeren dizinin ilk 3 elemanı

numbers = np.arange(10,20)
result = numbers [:3]

# dizinin elemanlarını tersten yazdırma

result = numbers [::-1]

# 3x5 boyutlarında 10-50 arası rastgele matris oluşturma

result = np.random.randint(10,50,15).reshape(3,5)

# üretilen matrisin satır ve sütun sayıları toplamı

matris = np.random.randint(10,50,15).reshape(3,5)
rowTotal = matris.sum(axis = 1)
colTotal = matris.sum(axis = 0)
print(rowTotal)
print(colTotal)

# üretilen matrisin en büyük, en küçük ve ortalama değerlerini bulma
matris = np.random.randint(10,50,15).reshape(3,5)
result.matris.max()
result.matris.min()
result.matris.mean()








print(result)
