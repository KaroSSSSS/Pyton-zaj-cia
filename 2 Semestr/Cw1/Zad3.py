import time
aplikacje = []
class Smartphone:
    def __init__(self,marka,model,system,pamiec,ram,aplikacje):
        self.marka = marka
        self.model = model
        self.system = system
        self.pamiec = pamiec
        self.ram = ram
        self.aplikacje = aplikacje
    def zadzwon(self):
        print("Halo! Będzie dzwonione!!!")
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Tu zakład pogrzebowy Wesoła Wdówka!")
    def zagraj_w_gre(self):
        print("Halo halo, gramy w gierki! Patrz liste gierek!")
        print(aplikacje)
    def test(self):
        print("Testujemy telefonik! HALO HALO :")
        print("Sysytem " , self.system)
        print("Pamięć ram ",self.ram)
        print("Pamięć wewnętrzna ",self.pamiec)
        print("Marka ",self.marka)
        print("Model ",self.model)

telefon1 = Smartphone("Xiaomi","Redmi note 5", "MIUI 11","64GB","4GB",aplikacje.append("Snake"))
telefon1.zadzwon()
telefon1.zagraj_w_gre()
telefon1.test()
telefon2 = Smartphone("Samsung","Galaxy S3 2018","Android 7.0","32GB","2GB",'"Snake","Tetris","Diamond Rush"')
telefon2.zadzwon()
telefon2.zagraj_w_gre()
telefon2.test()