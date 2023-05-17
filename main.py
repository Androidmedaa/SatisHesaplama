class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        if satici_cinsi in ['tv', 'bilgisayar', 'beyaz esya','giyim']:
            self.__satici_cinsi = satici_cinsi
        else:
            self.__satici_cinsi = 'diğer'
        self.__satis_tutari = 0

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_cinsi(self, satici_cinsi):
        if satici_cinsi in ['tv', 'bilgisayar', 'beyaz esya','giyim']:
            self.__satici_cinsi = satici_cinsi
        else:
            self.__satici_cinsi = 'diğer'

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari

    def get_satis_tutari(self):
        return self.__satis_tutari

    def magaza_satis_tutar(self):
        toplam_satis = 0
        for magaza in self.magazalar.values():
            toplam_satis += magaza.get_satis_tutari()
        return toplam_satis
satislar = {}
def main():
    while True:
        # Mağaza bilgilerini kullanıcıdan al
        magaza_adi = input("Mağaza adı: ")
        satici_adi = input("Satıcı adı: ")
        satici_cinsi = input("Satıcı cinsi (tv, bilgisayar, beyaz esya, diğer, giyim): ")
        satis_tutari = int(input("Satış tutarı: "))

        # Yeni bir Magaza nesnesi oluştur
        satis = Magaza(magaza_adi, satici_adi, satici_cinsi)
        satis.set_satis_tutari(satis_tutari)

        # Satışları satislar sözlüğüne ekle
        satislar[len(satislar) + 1] = satis

        # Yeni bir satış eklemek isteyip istemediğini kontrol et
        devam = input("Yeni satış eklemek için 'e', çıkmak için herhangi bir tuşa basın: ")
        if devam.lower() != 'e':
            break

    # Eklenen satışları ekrana yazdır
    for key, value in satislar.items():
        print(f"{key}. Mağaza adı: {value.get_magaza_adi()}, "
              f"Satıcı adı: {value.get_satici_adi()}, "
              f"Satıcı cinsi: {value.get_satici_cinsi()}, "
              f"Satış tutarı: {value.get_satis_tutari()}")

    # Toplam satışları mağaza adına göre hesapla ve ekrana yazdır
    magaza_adi = input("Toplam satışını öğrenmek istediğiniz mağaza adı: ")
    toplam_satis = 0
    for value in satislar.values():
        if value.get_magaza_adi() == magaza_adi:
            toplam_satis += value.get_satis_tutari()
    print(f"{magaza_adi} mağazasının toplam satış tutarı: {toplam_satis} TL")

    # Toplam satışları satıcı adına göre hesapla ve ekrana yazdır
    satici_adi = input("Toplam satışını öğrenmek istediğiniz satıcının adı: ")
    toplam_satis = 0
    for value in satislar.values():
        if value.get_satici_adi() == satici_adi:
            toplam_satis += value.get_satis_tutari()
    print(f"{satici_adi} adlı satıcının yaptığı toplam satış tutarı: {toplam_satis} TL")
main()