class SuperCar:

    # CHECK IF CAR IS ON
    def __int__(self, state):
        self.state = False
        if self.state is not False:
            return True
        else:
            return False

















    def accelerate(self, gear, speedMeasure=50):

        if gear <= 2:
            return gear * speedMeasure

        elif gear <= 4:
            return gear * speedMeasure
        # print("Entering Beast mode")

        elif gear <= 9:
            return gear * speedMeasure
        print("Beast mode activated,drive carefully")

    # def autoSpeed(self):
    #     command = float(input("Enter what speed you will like to travel in: "))
    #
    #     if self.state >= 250:
    #         print("\nSorry, your command exceed the safety state:", command)
    #
    #     else:
    #         print("Okay Oluwaseun,sit back and enjoy the ride")
    #
    # def chargeup(self):
    #     command = float(input("Enter the amount you want "))
    #
    #     if self.state >= 101:
    #         print("\n Charging limit exceed;", command)
    #     else:
    #         print("Charging")

    #


# s = SuperCar()
# s.accelerate(gear=9)



# s.chargeup()

