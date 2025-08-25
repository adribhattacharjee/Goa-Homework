# # 1) შექმენით ფუნქცია რომელიც მომხმარებელს მიესალმება
# def hello():
#     print("hi")
# hello()
# # 2) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება სახელს შემდეგ კი მას მიესალმება
# def hi():
#     word = input("what is your name: ")
#     print(word,"hi")
# hi()
# 3) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ დაუმატებთ ერთმანეთს 
def door():
    number = int(input("please enter a number: "))
    number1 = int(input("please enter a number: "))
    print(number1 + number)
door()
# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გამოაკლებს ერთმანეთს 
def school():
    number2 = int(input("please enter a number: "))
    number3 = int(input("please enter a number: "))
    print(number2 - number3)
school()
# 5) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაამრავლებს ერთმანეთზე
def multiplacation():
    number4 = int(input("please enter a number: "))
    number5 = int(input("please enter a number: "))
    print(number4 * number5)
multiplacation()
# 6) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაყოფს ერთმანეთზე 
def number1():
    number12 = int(input("please enter a number: "))
    number34 = int(input("please enter a number: "))
    print(number12/number34)
number1()
# 7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი
def number3():
     number45 = int(input("please enter a number: "))
     if number45 % 2 == 0:
         print("number is even")
     else:
         print("number is odd")
number3()
# 8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი
def number4():
    number46 = int(input("please enter a number: "))
    if number46 < 0:
        print(" the number is negative")
    else:
        print("the number is positive")
number4()
# 9) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს თუ მისი ასაკი მეტია 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის
def number5():
    number4 = int(input("please enter a your age: "))
    if number4 > 18:
        print("you are old")
    elif number4 < 18:
        print("you are young")
number5()
# 10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს
def number6():
    number47 = int(input("please enter a your age: "))
    for i in range(number47):
        print(i)
number6()
# 11) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა ლუწ რიცხვს
def number7():
    number48 = int(input("please enter a your age: "))
    for i in range(number48):
        if i % 2 == 0:
            print(i)
number7()
# 12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს
def number8():
    number48 = int(input("please enter a your age: "))
    for i in range(number48):
        if i % 2 != 0:
            print(i)
number8()
# 13) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია შემდეგ კი დაბეჭდავს ამ სიაში არსებული რიცხვების ჯამს
def number9():
    list = [3,4,2,4,5,6,7,8,9,10,11,12,13,14,15]
    num = 0
    for i in list:
        num += i
    print(num)
number9()