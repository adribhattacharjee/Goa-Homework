# # 1)შექმენი ლისტი შემდეგ დაამატე ბევრი სხვადასხვა რიცხვი ისე რომ რამოედენიმე მეორდებოდეს შემდეგ დაითვალე რამედენი არის 1 ელემენტი შედეგი გამოიტანე
# list = [2,3,3,3,5,5,66,66,8,7,88,9,90,34,2,3,5,1,2,2,2,3,3,3]
# print(list.count(3))
# # 2)შექმენი ლისტი შემდეგ გამოიტანე ეს ლისტი შემდეგ შეეკითხე მომხმარებელს რიცხვი რომლის დამატება უნდა შემდეგ მერანდენე უნდა იყოს(მომხმარებელმა ინდექსინგი არ იცის) საბოლოოდ გამოუტანე შედეგი
# list0 =[4,5,4,6,6,8,9,1,12,43,65,56,89,98,90,99,77,78,66,55,56,65,44,33,34,44,22,33,32,23,11,22,12,21,0,00]

# print(list0)

# num = int(input("please enter a number: "))
# num1 = int(input("please enter a place of a number: "))

# list0.insert(num1 -1,num)
# print(list0)
# BOSS LEVEL 3)შექმენი ცარიელი სია შემდეგ მომხმარებეს შეეკითხე რამდენი ელემენტის დამატება უნდა და დაამატებინე (append) შემდეგ შეეკითხე უნა თუ არა კიდევ მაამატოს რამე ელემენტი თუ პასუხი კი არის მშინ შეეკთხე მარმდენე ელემენტად უნდა დაამატოს და რა ელემენტი შემდეგ დაამატე(insert) ეს ელემენტი და შედეგი გამოუტანე თუ პასუხი იყო არა მაშინ გამოუტანე შედეგი
list1 = []

num = int(input("how many elements do you want to add into the list1"))
for i in range(num):
    num2 = int(input("do you want to add elements to the list1"))
    list1.append(num2)
num3 = input("do you want to add one more element to the list1")
if num3 == "yes":
    num4 = input("do you want to add elements to the list1")
    num5 = int(input("please enter a place of a number: "))
    list1.insert(num5,num4)
elif num3 == "no":
    print("ok")
print(list1)