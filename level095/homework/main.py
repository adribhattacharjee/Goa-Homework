film = ["The pirats of caribian sea","sonic 2","sonic 3"]

print(film)

film.append("stich")

film.remove("sonic 2")

print(film)

for i in film:
    print(i)


list = [1,2,3,4,5,6,7,8,9,10]

for i in list:

     if i % 2 == 0:
         print(i)

list.pop(9)

print(list)

print(list[4])



list = ["red", "green", "blue", "yellow", "purple"]

list.append("blue")

list.remove("yellow")   

print(list[:2:])

print(list[-3::])




list = []

for i in range(5):
    num = int(input("please enter a number"))
    list.append(num)

for i in list:
    print(i)


for i in list:
    if i > 10:
        print(i)
list.pop(2)


num1 = [1,2,3,4,5,6,7,8,9,10]

for i in num1:

    if i % 2 != 0:
        print(i)

print(num1[-3::])

num1.pop(0)

num1.append(12)