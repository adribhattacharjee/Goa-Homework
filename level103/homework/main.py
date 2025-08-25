# 1) შექმენი ფუნქცია, რომელიც პარამეტრეად მიიღებს რიცხვს და დააბრუნებს მისი ციფრების ჯამს
# задача:
# создать функцию которая принимает string число(тоесть, число в кавычках) и возвращает сумму его цифр

# def func(str_num):
#     sum = 0

#     for i in str_num:
#         sum += int(i)
    
#     return sum

# print(func("123"))
# 2) შექმენი ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს და დაბეჭდავს მას შემობრუნებულს.
# მაგალითად: 12345 -> 54321
# def reversed_number(number):
#     reversed_number = str(number)[::-1]

#     print(int(reversed_number))

# reversed_number(12345) 

# 3) შექმენი ფუნქცია, რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა რიცხვის კვადრატის ჯამს.
# def cubes():
#     num1 = 0
#     cube = int(input("please enter a number"))
#     for i in range(1,cube):
#         num1 += i*i
#         print(num1)
# cubes()

# 4) შექმენი ფუნქცია, რომელიც პარამეტრად მიიღებს 2 რიცხვს. ამ ფუნქციამ უნდა დააბრუნოს პირველი მიღებული რიცხვი მეორე მიღებული რიცხვის ხარისხში
def double_multiply(x,z):

    return  x**z

print(double_multiply(20,2))
# 5) შექმენი ფუნქცია, რომელიც მიიღებს 3 რიცხვს. გაიგებს მათ შორის მაქსიმალურს და მინიმალურს. შემდეგ კი დააბრუნებს მაქსიმალური და მინიმალური რიცხვის ნამრავლს. 
# def product_of_min_and_max(a, b, c):
#      minimum = min(a, b, c)
#      maximum = max(a, b, c)
#      return minimum , maximum

# result = product_of_min_and_max(3, 7, 5)
# print(result)