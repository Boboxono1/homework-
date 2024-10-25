class Avto:
    def __init__(self, model, rang, karobka, narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.kilometr = 0

    def model(self):
        return self.model

    def rang(self):
        return self.rang

    def karobka(self):
        return self.karobka

    def narh(self):
        return self.narh
    def set_narh(self, yangi_narh):
        self.narh = yangi_narh

    def update_km(self):
        self.kilometr += 1000

    def get_info(self):
        return f"{self.model} mashina ,rangi :{self.rang},karobaka :{self.karobka},narhi:{self.narh} dollar ,kilometr:{self.kilometr}"


Avto1 = Avto('Malibu', 'qora', 'avtomat', 30000)
print(Avto1.get_info())
Avto1.set_narh(25000)
Avto1.update_km()
Avto1.update_km()
print(Avto1.get_info())


class Avto_salon:
    def __init__(self, solon_nomi, manzil, sotuivdagi_avtomabillar):
        self.solon_nomi = solon_nomi
        self.mazil = manzil
        self.sotuvdagi_avtomabilar = sotuivdagi_avtomabillar


class Talaba:
    def __init__(self, ism, familya, t_yil):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.bosqich = 1

    def get_info(self):
        return f"{self.familya} {self.ism},{self.bosqich}-bosqich talabasi"

    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        self.bosqich += 1
