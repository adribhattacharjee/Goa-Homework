# 1) შექმენი რიცხვების სია და დაბეჭდე მისის ელემენტების ჯამი
numbers = [12,34,23,65,34]
num = 0
for i in numbers:
    num += i
print(num)
# 2) მოიფიქრე თუ როგორ უნდა გადაუარო სიას for ციკლით და range() ფუნქციის გამოყენებით
names = ["Nika","adri","levan"]
for i in range(0,3):
    print(names[i])
# 3) შექმენი რიცხვების სია და დაბეჭდე მათი საშუალო არითმეტიკული
numbers1 = [23,45,12,98,45]
num1 = 0
for i in numbers1:
    num1 += i
print(num1/5)
# 4) შექმენი სახელების სია, შემდეგ გადაუარე მას for ციკლით და დაბეჭდე თითოეული სახელის პირველი ასო(გამოიყენე index-ინგი)
names1 = ["adri","nika","levan"]
for i in names1:
    print(i[0])