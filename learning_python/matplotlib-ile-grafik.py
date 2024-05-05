import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


import cv2

""" Ornek1
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.axis([0,6,0,20])

plt.show()
"""




""" Ornek2 birden fazla grafigi ayni grafikte gosterme
x = np.linspace(0,2,100)

plt.plot(x,x, label="linear",color="red")
plt.plot(x, x**2, label="quadratic", color="yellow")
plt.plot(x, x**3, label="cubic", color="green")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.title("simple plot")


plt.show()
"""




""" Ornek3 birden fazla grafiği ayrı ayrı gösterme
x = np.linspace(0,2,100)

fig,axs=plt.subplots(3)

axs[0].plot(x, x, color="red")
axs[1].plot(x, x**2, color="green")
axs[2].plot(x, x**3, color="yellow")
plt.show()
"""
"""
maas = [random.randint(10000, 40000) for _ in range(15)]
fig, axs = plt.subplots(3, figsize=(6, 12), sharex=True)
plt.subplots_adjust(hspace=0.4)  # Sütunlar arası boşluğu ayarlar
x = range(15)
axs[0].plot(x, maas, color="red")
axs[0].set_title('Maaşın şimdiki hali')
axs[1].plot(x, [m ** 2 for m in maas], color="green")
axs[1].set_title('Maaş iki katına çıktığında')
axs[2].plot(x, [m ** 3 for m in maas], color="yellow")
axs[2].set_title('Maaş üç katına çıktığında')
plt.show()
"""






# Resmi yükleyin
img_path = "C:\\Users\\hatice\\Desktop\\projeler\\python\\deri_kanseri_final_projesi\\aktinic keratoses.png"


img = Image.open(img_path)

print("aktinic keratoses")
