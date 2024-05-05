import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon     # ikon kullanmak için ekledik.


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
    
        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500)        # uygulamanın ilk açıldığındaki boyutunu belirler
        self.setWindowIcon(QIcon("imza.png"))    # uygulamamızın sol ust kosesine icon ekledik.
        self.setToolTip("my tooltip")            # mause uzun süre uygulamanın üzerinde işlem yapmadan kalmaya devam edince mause'ın yanında bu yazı cıkar.
        self.initUI()

    def initUI(self):
        # uygulama uzerinde label olusturma
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50, 30)     # "Adınız: " konumunu belirtir.
    
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50, 70)
    
        # sonucu terminal yerine uygulamaya yazdırmak icin bu kodu olusturduk ve asagıdaki click fonksiyonuna tanımladık.
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)
    
        # uygulama üzerinde text olustura
        # text: ıcıne metin yazılabilen kutu
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)    
        self.txt_name.resize(200,32)        # textbox'ların gemişligini belirler.
        
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150, 70)
        self.txt_surname.resize(200,32)
        
        # uygulama üzerine buton ekleme
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150, 110)
        self.btn_save.clicked.connect(self.clicked) 
        
    def clicked(self):
        self.lbl_result.setText("ad: "+ self.txt_name.text()+ "\nsoyad: "+ self.txt_surname.text())
        
def window():
    app = QApplication(sys.argv)    # uygulama olustururken kullanılan temel bir kod
    win = MyWindow()             # uygulama olustururken kullanılan temel bir kod
    win.show()
    sys.exit(app.exec_())   # bu kod ile carpıya bastığımızda uygulama durur.

window()

    
                
    
    
    
    

    
    
    
    











