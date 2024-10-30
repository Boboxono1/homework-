class Shaxis:
    def __init__(self, ism, familya, yosh):
        self.__name = ism
        self.familya = familya
        self.__age = yosh

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


shaxis1 = Shaxis('Husanboy', 'Boboxonov', 19)
print(shaxis1.get_name())
print(shaxis1.familya)
print(shaxis1.get_age())


class Account:
    def __init__(self):
        self.__balance = 0  # Xususiy atribut

    def balance1(self):
        return self.__balance

    def qoshish(self, summa):
        if summa > 0:
            self.__balance += summa
        else:
            print("Mablag' manfiy bo'lmasligi kerak.")

    def yechish(self, summa):
        if 0 < summa <= self.__balance:
            self.__balance -= summa
        elif summa > self.__balance:
            print("Balans yetarli emas.")
        else:
            print("Mablag' manfiy bo'lmasligi kerak.")


pul = Account()
print(pul.qoshish(9))
print(pul.balance1())


class Employee:
    def __init__(self, ism, lavozim, mavoshi):
        self.ism = ism
        self.lavozim = lavozim
        self.__mavoshi = mavoshi

    def set_salariy(self):
        return self.__mavoshi

    
employee1 = Employee("Dilshod", "Dasturchi", 5000)
