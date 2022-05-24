class Playground:
    # def __init__(self, first_name, last_name, age):
    def __init__(self,age):
        self._age = age
        # self._name = f"{first_name} {last_name}"

    @property
    def age(self):
        # print("i am getting name")
        return self._age

    @age.setter
    def age(self,age):

       if age < 0:
          raise ValueError("Age can not be negative")

       self._age = age

    @age.deleter

    def age(self):
        print("Deleting name")

        del self._age



    # @name.setter
    # def name(self, fullname):
    #     print("i am settinf name")
    #     self._name = fullname


p1 = Playground(70)
print(p1.age)
p1.age = 16
print(p1.age)
print()

del p1.age
print(p1.age)
