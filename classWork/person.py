class Person:
    def __init__(self, dob, mob, yob, first_name, last_name):
        self.age = f"{dob},{mob},{yob}"
        self.name = f"{first_name},{last_name}"
        self.id = f"{self.age} , {self.name}"

    def name(self,name):

        pass
