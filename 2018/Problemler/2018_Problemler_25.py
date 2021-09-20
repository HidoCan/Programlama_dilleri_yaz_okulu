# Baska Bir Kod - Python Soru / Cevap

def girdi_al():
    isim = input(u"İsim Giriniz:")

    return isim.upper()


def isim_donustur(ad):
    dondur = str()
    sehirler = {"A": "Antalya", "B": "Bilecik", "Cankırı": "", "Ç": "Çanakkale", "D": "Diyarbakır", "E": "Erzurum",
                "F": "Fetiye",
                "G": "Giresun", "Ğ": "Gümüşhane", "H": "Hatay", "I": "Iğdır", "İ": "İzmir", "L": "Lüleburgaz",
                "K": "Kütahya", "M": "Mersin", "N": "Niğde", "O": "Osmaniye", "Ö": "Ordu", "P": "Pamukkale",
                "R": "Rize",
                "S": "Samsun", "Ş": "Şırnak", "T": "Tokat", "U": "Uşak", "Ü": "Uşak", "V": "Van",
                "Y": "Yozgat", "Z": "Zonguldak"}

    for i in ad:
        if ("A" <= i and i <= "Ğ"):
            dondur += sehirler[i] + " "

    return dondur


ad = list(girdi_al())
print(isim_donustur(ad))