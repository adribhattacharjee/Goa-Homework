# # 1) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი
# numbers1 = [521,6,7,8,9,10]
# maxnum = numbers1[0]
# for i in range(len(numbers1)):
#     if numbers1[i] > maxnum:
#         maxnum = numbers1[i]
# print(maxnum)
# # 2) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი
# numbers = [10,5,4,7,8,2]
# for i in numbers:
#      i += numbers
#      print(i)
# # 3) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი
# numbers2 = [76,95,87,65,45,98,23,21,32]
# minnum = numbers2[0]
# for i in range(len(numbers2)):
#     if numbers2 < minnum:
#         minnum = numbers2[i]
# print(minnum)
# # 4) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).
# numbers3 = [-4,-5,9,9,-3,-8,8,7,5,-7,-6,-8,-5]
# numbers4 = []
# numbers5 = []
# for i in range(len(numbers3)):
#     if numbers3[i] > 0:
#         numbers4.append(numbers3[i])
#     else:
#         numbers5.append(numbers3[i])
# # 5) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)
# numbers6 = [5,4,3,2,1,10,9,8,7,6,5,4,3,2,1,10]
# for i in range(len(numbers6)-1,-1,-1):
#     print(numbers6[i])
# # 6) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
# chars = [1,3,54,1,3,4,2,6,2,6,4]

# nums = []
# for i in range(len(chars)):
#     if chars[i] not in nums: 
#         nums.append(chars[i])

# print(nums)
# # 7) შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის
# name ="adri"
# for i in range(len(name)-1,-1,-1):
#     name1 = name[i]
#     print(name1)
# # 8) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი
# num = int(input("enter a number"))
# if num % 2 == 0:
#     for i in range(2,num,2):
#         print(i)
# else:
#     for i in range(1,num,2):
#         print(i)
# 9) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის
num2 = int(input("please enter a year"))
num3 = num2//100
print(num3)
# 1) მომხმარებელს შეეკითხეთ list სიგრძე შემდეგ მომხმარებელს დაამათებინეთ ციფრები(int) list შემდეგ შექმენით კიდევ 2 list 
# შემდეგ შექმენი ფუნქცია რომელც დაყოფს ლისტში მოცემულ რიცხვებს კენტებად და ლუწებად. კენტი ციფრები უნდა დაამატოს 2 list ლუწი რიცხვები უნდა დაამატოს 3 list
length = int(input("Please enter a list lenght: "))

numbers = []

for i in range(length):
    num = int(input("Please enter a number: "))
    numbers.append(num)

print(numbers)