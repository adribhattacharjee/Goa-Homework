# # 2)შექმენი ფუნქცია, რომელიც აბრუნებს სამუშაო დღეს შეყვანილი ნომრის მომხმარებელეი ჩაწერე ამ რიცხვს მიხედვით:
# # 1 print "Sunday"
# # 2 print "Monday"
# # 3 print "Tuesday"
# # 4 print "Wednesday"
# # 5 print "Thursday"
# # 6 print "Friday"
# # 7 print "Saturday"
# # Otherwise returns "Wrong, please enter a number between 1 and 7"

# text = int(input("pls enter a number"))

# if text == 1:
#     print("monday")
# elif text == 2:
#     print("tuesday")
# elif text == 3:
#     print("wensdey")
# elif text == 4:
#     print("thursday")
# elif text == 5:
#     print("friday")
# elif text == 6:
#     print("suterday")
# elif text == 7:
#     print("sunday")
# else:
#     print("wrong enter a number 1 to 7")

# # 3)შენი მიზანი დაითვალო ამ ლისტში True-ს რაოდენობა და გამოიტანო შედგი
# # ლისტი = [True,  True,  True,  False,
# #   True,  True,  True,  True ,
# #   True,  False, True,  False,
# #   True,  False, False, True ,
# #   True,  True,  True,  True ,
# #   False, False, True,  True]

# list = [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]

# list.count(True)

# print(list.count(True))

# # 4)დაწერეთ პროგრამა, რომელიც იპოვის ყველა რიცხვის ჯამს 1-დან რიცხვამდე. რიცხვი ყოველთვის იქნება 0-ზე მეტი მთელი რიცხვი. თქვენი საჭირო პროდუქტის საჭიროება, რაც არის ნაჩვენები, მათ შორის არის ეს მაგალითი, თუ როგორ მივაღწიოთ ამ შედეგს და ის არ არის ნაწილი,
# # მაგალითი: 
# # 2 -> 3 (1 + 2)
# # 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# num = int(input("Enter a number: "))

# number = 0

# for i in range(num + 1):
#     number += i
# print(number)
# # 5)შექმენით ფუნქცია, რომელიც პასუხობს კითხვას "თამაშობ ბანჯოზე?".
# # თუ თქვენი სახელი იწყება ასო "R"-ით ან პატარა "r"-ით, 
# # მაშინ დაწეროს
# # name + " plays banjo" 
# # თუ სახელი არ იცყება "r" 
# # მაშინ დაწეროს 
# # name + " does not play banjo"
# name =input("please enter your name")

# if name[0] == "R" or name[0] == "r":
#     print(name + "plays banjo")
# else:
#     print(name + " does not play banjo")
# # 7)შექმენი ლისტი სადაც იქნება ციფრები და დააბრუნეთ ამ რიცხვთა ჯამი.
# # მაგალითი: 
# # Input: [1, 5.2, 4, 0, -1]
# # Output: 9.2

# list = [1,33,43,44]
# num = 0

# for i in list:
#     num += i
# print(num)
# 8)მომხმარებელს შეეკითხე სიტყვა შემდეგ შეეკითხე რამდენჯერ უნდა რომ გაიმეორეს ეს სიტყვა. მაგალითი:
# "I"     -> "IIIIII"
# "Hello" -> "HelloHelloHelloHelloHello"

word = input("please enter a word: ")
word1 = int(input("please enter how many times do you want to reply the word"))

print(word*word1)