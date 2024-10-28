class Shaxis:
    def __init__(self, ism, familya, passport, t_yil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.t_yil = t_yil

    def get_info(self):
        info = f"{self.ism} ,{self.familya},Passport:{self.passport},T_yil:{self.t_yil}"
        return info

    def get_age(self, jor_yil):
        return jor_yil - self.t_yil


class Foydalanuvchi(Shaxis):
    def __init__(self, ism, familya, passport, t_yil, email):
        super().__init__(ism, familya, passport, t_yil)
        self.email = email
        self.vatan = 'uzbekiston'

    def get_email(self):
        return self.email

    def get_vatan(self):
        return self.vatan

    def get_info1(self):
        return (f"{self.ism},{self.familya},\n"
                f"Passport : {self.passport},t_yil:{self.t_yil},Email:{self.email},Vatan:{self.vatan}")


class Admin(Foydalanuvchi):
    def __init__(self, ism, familya, passport, t_yil, email, kasbi):
        super().__init__(ism, familya, passport, t_yil, email)
        self.kasbi = kasbi

    def ban_user(self):
        return "Foydalanuvchi bloklandi"


admin1 = Admin('Ali', 'Valiyev', 'AB1234567', 1985, 'ali@mail.com', 'Dasturchi')
print(admin1.ban_user())