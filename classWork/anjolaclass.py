# gen = [num for num in range(1,11**100)]
#
# lst= (num for num in range(1,11**100))
#
# print(sys.getsizeof(gen))

# print(sys.getsizeof(lst))

# set = {1,1,1,3,4,6,7,5,4,5}
#
# print(set)

# dict_comp = {k:v for k,v in zip(range(5),range(5))}
# print(dict_comp)

# lst = [i in (range(61, 95), lst.append(i))]
# print(lst)

# add = lambda x,y:x + y
# sub = lambda x,y:x - y
# print(add.__name__)
# print(sub.__name__)
#
# LAMBDA

# def add(a,b):
#     return a + b
#
# def sub(a,b):
#     return  a - b
#
# def mul(a,b):
#     return a * b
#
# def div(a,b):
#     return a / b

#
# def operate (x,y, func):
#     return func(x, y)
#
# val_sub = operate(1,4,lambda x,y:y -x)
# val_add = operate(53,4,lambda x,y:y +x)
# val_mul = operate(6,26,lambda x,y:y *x)
# val_div = operate(5,24,lambda x,y:y /x)
#
#
#
# # val_add = operate(7,27,add)
# # val_mul = operate(7,27,mul)
# # val_div = operate(7,27,div)
#
# print(val_add)
# print(val_sub)
# print(val_mul)
# print(val_div)

# def multiple (x, func):
#     return func(x)
#
# val_double = multiple(4, lambda x:x*x)
#
# val_triple = multiple(5,lambda x:x*x*x)
#
# print(val_double)
# print(val_triple)

# abs

# print(abs(566-1000))
#
# print(any([1,3,4,5,2,5,6,0]))


# def isOdd(x):
#     return x % 2 == 1
#
# filter_obj = list(filter(isOdd, range(1,10)))
# print(filter_obj)
#
# from functools import reduce
# fruits = ["Apple","pineapple","Orange","Watermelon","Banana"]
# shortest = reduce(lambda x ,y: x if len (x) < len(y) else y, fruits)
# print(shortest)
# # print(min(fruits, key=len))
# print(sorted(fruits, key=lambda x :x[-1]))
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Denomiator can not be zero")
#     return a / b
#
#
# num = int(input("Enter the numerator: "))
# den = int(input("Enter the denominator: "))
# while True:
#     try:
#         print(divide(num, den))
#         break
#     except ValueError:
#            print("Wrong value")
#            num = int(input("Enter the numerator: "))
#            den = int(input("Enter the denominator: "))


# class Player:
#       name = 'Yakubu'
#
#       def say_my_name():
#             print("Yakubu")
# player1 = Player()
# player2 = Player()
#
# print(player1)
# player1.name  = 'Ronaldo'
# print(player2)
#
# print(player1.name)
# print(player2.name)

# class Player:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age


# INHERITANCE


# class Animal():
#     def __init__(self, name):
#         self.name = name
#         print("ANIMAL CREATED")
#
#     def eat(self):
#         print("I AM EATING")
#
#     def who_am_i(self):
#         print("i am a Animal")
#
#
# class Dog(Animal):
#     def __init__(self, name, type_):
#
#         super().__init__(name)
#         print("Dog created")
#
#         self.type = type_
#
#     def who_am_i(self):
#         print("I am a dog")
#
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__(self)
#         print("cat created")
#
#     def who_am_i(self):
#         print("I am a cat")
#
#
# felix = Dog("felix","bull")
# niko = Cat()







class Sport(object):
    goat = 'LEBRON FUCKING JAMES'

    def __init__(self, jersey):
        self.jersey = jersey


class Ballgame(object):

    def __init__(self, goat, jersey):
        super().__init__(goat)
        self.jersey = jersey

    def football(self):
        pass







