class DreamGirl:
    # Initializing the class with data fields
    def __init__(self, name):
        self.name = name
        self.age = 18

    def age_reading(self):
        if self.age >= 18:
            print(f"I am {self.age} year old!")
        else:
            print("You can't have girls under 18. Go back and change the age!")

    # Updating age by creating a method with conditions
    def update_age(self, new_age):
        if new_age >= self.age:
            self.age = new_age
        else:
            print("You can't roll back an age")

    # We can also do something more interesting, like incrementing the age
    def incrementing_age(self, increment_age):
        if increment_age <= 30:
            self.age = increment_age + self.age
        else:
            print("You can't increase her age any further")

    # Creating method which is called function if it is not inside class
    def hello(self):
        print(f"Hey you! I am {self.name.title()}")
        print(f"I am {self.age} year old and I am gonna make you feel ecstatic!")

    def dance(self):
        print(f"{self.name.title()} now dances and cover you with her perfume")

    def thrill(self):
        print(f"{self.name.title()} gets your heart racing in her skin-tight jeans")

    def dream(self):
        print(f"{self.name.title()} is your teenage dream tonight!")


britney = DreamGirl('britney')
britney.hello()
britney.dance()
britney.thrill()
britney.dream()