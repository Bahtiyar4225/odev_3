class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        self.adı = adı
        self.departmanı = departmanı
        self.çalışma_yılı = çalışma_yılı
        self.maaşı = maaşı

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.adı)
            print("Departmanı:", personel.departmanı)
            print("Çalışma Yılı:", personel.çalışma_yılı)
            print("Maaşı:", personel.maaşı)
            print()

    def zam(self, personel, zam_oranı):
        for p in self.personel_listesi:
            if p == personel:
                p.maaşı *= (1 + zam_oranı / 100)
                break

    def personel_cikar(self, personel):
        self.personel_listesi.remove(personel)


if __name__ == "__main__":
    personel1 = Personel("Ali", "ika", 3, 5000)
    personel2 = Personel("Ayşe", "bilgisayar", 5, 6000)
    
    firma = Firma()
    firma.ekle(personel1)
    firma.ekle(personel2)
    
    print("Personelleri:")
    firma.personel_listele()
    
    print("Zamdan önce:")
    firma.personel_listele()
    print()
    
    print("Zamdan sonra:")
    firma.zam(personel1, 10)  
    firma.personel_listele()
    print()
    
    print("Cıkarma yapıldıktan sonra:")
    firma.personel_cikar(personel1)
    firma.personel_listele()
