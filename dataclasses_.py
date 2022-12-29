# class Student:
#     def __init__(self, name1, address1, age1):
#         self.name = name1
#         self.address = address1
#         self.age = age1
#
#     def get_details(self):
#         return self.name,self.address, self.age
#
#     def set_details(self, new_name, new_address):
#         self.name = new_name
#         self.address = new_address
#
#
# s = Student("Koustubh", "Pune",20)
# print(s.get_details())
# print(s.set_details("Koustubh","Bidar"))
# print(s.get_details())


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    address: str
    age: int


s1 = Student(name="Chetan", address="Pune", age="15")
print(type(s1.age))
print(s1)