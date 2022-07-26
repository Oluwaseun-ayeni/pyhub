# #Checking type of datatypes
#
# a = 4000
#
# type(a)
#
# print(type(a))
#
# my_income = 200
#
# tax_rate = 0.4
#
# my_taxes = my_income * tax_rate
#
# print(my_taxes)

# String in detail
#

# good = 677/900
# print("The result was {r:1.2f}".format(r=good))
## float formatting follows "{value:width.precision f}"


# print('Python{}'.format(' rules!'))

##List
# lst = ['a','f','b','d','e','c']
# number = ['1','2','3','4','5','6','7','8','9']
# number.reverse()
# lst.reverse()
# print(lst)
# print(numbe


# prices_lookup = {'apple':3.00,'orange':4.98,'pineapple':['a','b','c']}
#
# print(prices_lookup['pineapple'][2].upper())

# tuples
# you can have string and interger in a tuple
# t = (1,2,3,4)
# my_list = [1,2,3]
# print(type(my_list))

# Sets
# myset = set()
# myset.add(1)
# myset.add(12)
# print(myset)

# my_list = (1,2,3,4,5,6,4,5,3,4,2,3,5,6,7,9,9,7)
# print(set(my_list))

# Booleans

# I/O (INPUT AND OUTPUT)
#
#
# lst = [ ]
# for i in range(1,10 ):
#  lst.append(i)
#  # lst.add(10)
#  print(lst)

# print(not(1==1))
#
# if True:
#     print('Its true')

# for loop
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list_sum = 0
# for num in mylist:
#     list_sum = list_sum + num
#
# print(list_sum)

# for num in mylist:
#     if num % 2 == 0:
#         print(num)
# else:
#  print(f'Odd Number: {num}')

# mylist = [(1,2,3),(4,5,6),(7,8,9)]
# for a,b,c in mylist:
#     print(a,b,c)

# x = 0
#
# while x < 5:
#     print(f'The current value of x is {x}')
#     x = x + 1

# mylist1 =[1,2,3]
# mylist2 =['a','b','c']
# for item in zip(mylist1,mylist2):
#     print(item)

# mystring = 'hello'
# mylist = []
# for letter in mystring:
#     mylist.append(letter)
#     print(mylist)

# celcius = [0,10,32,20,34.5]
# fahrenheit = [((9/5)*temp + 32) for temp in celcius]
# print(fahrenheit)

# print(list(range(0,11,2)))

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# def add_num(num1,num2):
#     return num1 + num2
# result = add_num(10,20)
# print(result)


# TUPLE UNPACKING

# stock_prices = [('APPL',100),('BTC',35000),('ETH',2600)]
# for product,amount in stock_prices:
#     print(amount+(1*amount))
#
# work_hours = [('Abby', 100), ('Emma', 200), ('Jose', 400)]
#
#
# def employee_check(work_hours):
#     current_max = 0
#     employee_of_month = ''
#     for employee, hour in work_hours:
#         if hour > current_max:
#             current_max = hour
#             employee_of_month = employee
#         else:
#             pass
#
#
#
#     return (employee_of_month, current_max)
# print(employee_check(work_hours))

# from random import shuffle
#
# example = [1,2,3,4,5,6,7]
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
# result = shuffle_list(example)
#
#
#
# mylist = [' ','O',' ']
#
#
#
# def player_guess():
#      guess= ''
#      while guess not in ['0','1','2']:
#          guess = input("Enter a number from 0,1 or 2")
#      return int (guess)
# #
# myindex = player_guess()
# print(myindex)
#
# def check_guess (mylist,guess):
#     if mylist[guess] == 'O':
#         print('Correct')
#     else:
#         print('Wrong guess')
#         print(mylist)
# #INITIAL LIST
# mylist = [' ', 'O',' ']
# #SHUFFLE LIST
# mixedup_list = shuffle_list(mylist)
# #USER GUESS
# guess =  player_guess()
# #CHECK GUESS
# check_guess(mixedup_list,guess)

# def myfunc(a,b):
#     return sum((a,b)) * 0.05
# print(myfunc(20,40))

# ARGS
# It allows you to pass in as many parameter as you want
# build tuples

# def myfunc(*args):
#     return sum(args) * 0.05
# print(myfunc(3,5,7,8,5))

# KWARGS
# build dict in func

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')
#
#
# print(myfunc(fruit='apple',vegge ='lettuce'))

# def myfunc(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['foods']))
#
#
# print(myfunc(30, 5, 67, 78, fruit='apple', vegg='lettuce', f='pizza'))

# def myfunc(x):
#     out = []
#
#     for num in range(len(x)):
#         if num % 2 == 0:
#             out.append(x[num].upper())
#         else:
#             out.append(x[num].lower())
#     return ''.join(out)


# def lesser_of_two_even(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#
#
# print(lesser_of_two_even(2, 3))

# def animal_crackers(text):
#     wordlist = text.split()
#     return wordlist [0][0] == wordlist [1][0]

# def makes_twenty(n1, n2):
#     return sum(n1+n2) == 20 or n1 == 20 or n2 == 20

# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'

# def master_yoda(text):
#     return ' '.join(text.split()[::-1])
# print(master_yoda('We are ready to go'))

# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
# print(almost_there(2))

# def has_33(nums):
#     for i in range(0, len(nums) - 1):
#
#         # nicer looking alternative in commented code
#         # if nums[i] == 3 and nums[i+1] == 3:
#
#         if nums[i:i + 2] == [3, 3]:
#             return True
#
#     return False
#
#
# print(has_33([1, 3, 1]))

# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 6
#     return result
# print(paper_doll('hello'))

# def blackjack(a, b, c):
#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
#         return sum((a, b, c)) - 10
#     else:
#         return 'BUST'

#
# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
#
#
# print(summer_69([4]))


# name = 'THIS IS A GLOBAL STRING'
#
#
# def greet():
#     name = 'Sammy'
#
#      print('Hello ' + name)
#
#     # def hello():
#     #     print('Hello  ' + name)


# def vol(rad):
#    return (4/3)*(3.14)*(rad**3)
#
# print(vol(2))

# get user to input int
#
# def user_choice():
#     choice = 'WRONG'
#     while not choice.isdigit():
#         choice = input("Enter any number from (0-10): ")
#
#     return int(choice)
#
# print(user_choice())
# position = [0, 1, 2], [3, 4, 5], [6, 7, 8]
# print(position)

# OOP
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def get_circumference(self):
#         return self.radius * Circle.pi * 2
#
#
# my_circle = Circle(30)
# my_circle.get_circumference()
#


# INHERITANCE

# class Animal():
#     def __init__(self):
#         print("ANIMAL CREATED")
#
#     def eat(self):
#         print("I AM EATING")
#
#     def who_am_i(self):
#         print("i am a Animal")
#
#
# my_animal = Animal()
# my_animal.eat()
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def who_am_i(self):
#         print("I am a dog")
#
#
# my_dog = Dog()
# my_dog.who_am_i()
#
# POLYMORPHISM
#
# class Dog():
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         return self.name + ' Woof'
#
#
#     def run(self):
#         return self.name +' i am running'
#
#
#
# class Cat():
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + ' Meow'
#
#     def run(self):
#         return self.name + ' I am running'
#
#
# felix = Dog("felix")
# niko = Cat("niko")
#
#
# for pet in [felix,niko]:
#     print(pet.run())
#
# import abc
#
# class A(abc.ABC):
#     @abc.abstractmethod
#     def must_be_implement(self):
#         return
#
# class B(A):
#     def must_be_implement(self):
#         return

#
# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print('aye ali ti ta')
#
#
# b = Book("Ali go to School", 'AliG', 200)

# Error exeption
# try:
#     f = open('testfile', 'r')
#     f.write("Write a test line")
# except:
#     print('All other Error')
# finally:
#     print('I always run')

# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print('WTF are you doing dude')


# try:
#     x = 5
#     y = 0
#
#     z = x/y
# except ZeroDivisionError:
#     print('You are out of your mind buddy')
#
# finally:
#     print('All done')


# def ask():
#     while True:
#
#         try:
#             squ = int(input('Enter a number: '))
#
#         except:
#             print('That is not a number')
#             continue
#
#
#         else:
#             print('Thank you, your number squared is: ' ,squ**2)
#             break
#
# ask()


# spam =['bro','sup','hommie','yoo','yoo']
# spam.insert(3,'broda')
#
# print(spam)

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# current_users = ['bigt','Dt','sully','jamie','atita']
# new_users =['Zt','Joe','Ray','Josh','jamie']
#
# for new_users in current_users:
#     if new_users == 'JAMIE':
#         print("You have to enter a new name ")
#
#     else:
#         print("Username is available")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")
<<<<<<< HEAD


# decorator

# def shout(text):
#     return text.upper()
#
#
# print(shout('Hello'))
#
# yell = shout
#
# yell('')
#
# author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()


# x, y = input("Enter full name: ").split()
# print("First name: ", x)
# print("Last name: ", y)
# print()

# DATETIME

# from datetime import datetime
#
# mydatetime = datetime(2021,10,3,14,20)
# print(mydatetime)

# today = datetime.date.today()
# print(today.ctime())

# mystring = 'hello'
#
# mylist = []
# for letter in mystring:
#     mylist.append(letter)
#
# print(mylist)


# data = [1,2,3 ]
#
# def incr(x):
#     return  x+1
# print(list(map(incr,data)))

#
# print("result guy".capitalize())

# f = None
# for i in range(5):
#     with open("app.log","w") as f:
#         if i > 2:
#             break
# print(f.closed)


# y =[2,5J,6]
# y.sort()
# print(y)


# v  = ["dc" , "hg" ]
# print((list(map(lambda x: len(x),x)))

# x = "abcdef"
# i = "a"
# while i in x[:-1]:
#     print(1, end=" ")

#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'extraLongFactorials' function below.
# #
# # The function accepts INTEGER n as parameter.
# #
#
# def extraLongFactorials(n):
#     n = n * (n - 1) * (n - 2)
#
#     for num in range(0, 100):
#         if n <= 1 <= 100:
#
#
#
#     # Write your code here
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     extraLongFactorials(n)
#
# extraLongFactorials(30)

c = 2
for i in range(1,12):
    y = c*i
    print(y)












=======
>>>>>>> 590ac8ebbb1e151c32dba9047ffb32b28a6167a3

