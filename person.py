class Person:

    def __init__(self, gender, name, first_name, father_name, mom_name, city, wife_name=None):
        self.gender = gender
        self.name = name
        self.first_name = first_name
        self.father_mane = father_name
        self.mom_name = mom_name
        self.wife = wife_name
        self.city = city

    def grt_info(self):
        return f' Gender: {self.gender}\n' \
               f' Name: {self.name}\n' \
               f' First_name: {self.first_name}\n' \
               f' Father: {self.father_mane}\n' \
               f' Mom: {self.mom_name}\n' \
               f'Wife: {self.wife}\n' \
               f'City: {self.city}'
