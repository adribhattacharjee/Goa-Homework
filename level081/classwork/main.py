# 1)შექმენი ფუნქცია რომელსაც ექნება 2 პარამეტრი. პირველი პარამეტრი იქნება ენა (geo, eng, rus), მეორე პარამეტრი იქნება მომხმარებლის სახელი. შენი მიზანია რომ შეამოცმო რა ენა აირჩია მომხმარებელმა და მაგ ენაზე მიესალემო თუ ჩამოთვლილი სამი ენიდან არცერთი არ არის უთხერი რომ ეს ენა არ გვაქ
def number(leng,name):
    if leng == "geo":
        print("გამარჯობა " + name)
    elif leng =="eng":
        print("helo " + name)
    elif leng == "rus":
        print("привет " + name)
    else:
        print("we dont have this lenguage")
name = input("please enter your name: ")
lenguage = input("please enter a lenguage: ")
number(lenguage,name)
# 2)შენინ მიზანია შექმნა კანკულატორი  პირველი პარამეტრი იქნება ოპერატორი(+,-,*,/) შემდენი ორი პარამეტრი იქნება ციფრები ოპერატორიც და ციფრებიც უნდა შემოიტანოს მომხმარებელმა
def number1(operator,num1,num2):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1/num2)
op = input("enter operator")
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
number1(op,num1,num2)