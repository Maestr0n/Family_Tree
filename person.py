class Person:
    __gender = None
    __name = None
    __surname = None
    __father_name = None
    __mom_name = None
    __wife = None
    __city = None

    def __init__(self, gender, name, surname, father_name, mom_name, city, wife_name):
        self.set_gender(gender)
        self.set_name(name)
        self.set_surname(surname)
        self.set_father(father_name)
        self.set_mom_name(mom_name)
        self.set_wife(wife_name)
        self.set_city(city)

    def __str__(self):
        return f'{self.__name}\n{self.__surname}\n{self.__gender}\n{self.__father_name}\n' \
               f'{self.__mom_name}\n{self.__wife}\n{self.__city}'

    def __repr__(self):
        return f'Gender: {self.__gender}\n' \
               f'Name: {self.__name}\n' \
               f'Surname: {self.__surname}\n' \
               f'Father: {self.__father_name}\n' \
               f'Mom: {self.__mom_name}\n' \
               f'Wife: {self.__wife}\n' \
               f'City: {self.__city}'

    def set_gender(self, gender):
        self.__gender = gender

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_father(self, father):
        self.__father_name = father

    def set_mom_name(self, mom):
        self.__mom_name = mom

    def set_wife(self, wife):
        self.__wife = wife

    def set_city(self, city):
        self.__city = city

    def get_gender(self):
        return self.__gender

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_father(self):
        return self.__father_name

    def get_mom_name(self):
        return self.__mom_name

    def get_wife(self):
        return self.__wife

    def get_city(self):
        return self.__city
