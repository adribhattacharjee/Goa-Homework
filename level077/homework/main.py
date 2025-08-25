# 1.შექმენი ცარიელი ლისტი სადაც იქნება ციფრები შემდეგ მომხმარებელს შეეკითხე რამდენი რიცხვის წაშლა უნდა შემდეგ შეეკითხე რა რიცხვების წაშl
# list = [3,34,5,645,65,778,4,46,4464,645,64,64,67,6,57567,45,34,46,654]
# print(list)

# num = int(input("how many numbers do you want to delete"))

# for i in range(num):
#     num1 = int(input("please enter a numbers that you want to delete"))
#     list.remove(num1)
# print(list)
# 2. შექმენი ცარიელი ლისტი სადაც იქნება ციფრები შემდეგ მომხმარებელს შეეკითხე რამდენი რიცხვის წაშლა უნდა შემდეგ შეეკითხე რომელი რიცხვენის წაშლა უნდა ინდექსით
# list1 = [22,32,54,45,23,12,21,88,76,90,99,55,3,4,8,3,2,11,8,9,0,3]
# print(list1)

# num0 = int(input("please enter how many numbers do you want to delete"))
# num2 = int(input("please enter anumbers that you want to delete"))

# for i in range(num0):
#     num2 = int(input("please enter anumbers that you want to delete"))
#     list1.pop(num2)

# print(list1)
# 3.შექმენი ცარიელი ლისტი შემდეგ მომხმარებელს დაამატებინე ციფრები შემდეგ შექმენი კიდევ 4 ლისტი 1 ლისტსი დაამარებ ლუც რიცხვებს 2 ში დაამატებ კენტ რიცხვებს მე-3ში დაამატებ უარყოფით რიცხვება მე4 ში დაამატებ დადებით რიცხვებს
# list0 = []
# list2 = []
# list3 = []
# list4 = []
# list5 = []
# num3 = int(input("please enter how many numbers do you want to add to the list0: "))

# for i in range(num3):
#     num4 = int(input("please enter a numbers that you want to add in the list0: "))
#     list0.append(num4)
    
# for i in list0:
#     if i % 2 == 0:
#         list2.append(i)
#     elif i % 2 != 0:
#         list3.append(i)
#     if i > 0:
#         list4.append(i)
#     elif i < 0:
#         list5.append(i)
# print(list0)
# print(list2)
# print(list3)
# print(list4)
# print(list5)
# 4.შექმენი ლისტი შემდეგ აირჩიე ერთ-ერთი ელემენტი ლისტიდან და დაითველე მისი რაოდენობა მერე გაიგე ლისტის ზომა შემდეგ შემოატრიალე ეს ლისტი თითოეული შედეგი გამოიტანე
list6 = [23,32,43,54,45,23,33,32,22]

print(list6.count(23))
print(len(list6))
list6.reverse()
print(list6)        