# 1)   მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი შეამოწმეთ ეს რიცხვი არის თუ არა სამის ჯერადი
num = int(input("ener num:"))
if num % 3 == 0:
  print(num)
#  2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი შეამოწმეთ ეს რიცხვი არის თუ არა ხუთის ჯერადი
num = int(input("please enter a number"))

if num % 5 == 0:
  print(num)
#  3)  მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ ეს რიცხვი უარყოფითია თუ დადებითი
num = int(input("please enter a number"))

if num > 0:
  print("num is positive")

else:
  print("num is negative")
#  4)  დაბეჭდეთ ნულიდან 50 მდე მხოლოდ ლუწი რიცხვები 
for i in range(0,50,2):
  print(i)
#  5) დაბეჭდეთ ნულიდან 30 მდე მხოლოდ კენტი რიცხვები
for i in range(1,30,2):
  print(i)
#  6)  დაბეჭდეთ ნულიდან 70 მდე რიცხვები ლუწ რიცხვებს გვერძე მიუწერეთ რომ ლუწია ხოლო კენტებს მიუწერეთ რომ კენტია
for z in range(70):
  
  if z % 2 == 0:
    print("number is even",z)
  
  elif z % 2 != 0:
    print("number is odd",z)
#  7) დაბეჭდეთ 0 დან 100 მდე მხოლოდ ხუთის ჯერადი რიცხვები
for i in range(0,100,5):
  print(i)
#  8) დაბეჭდეთ 0 დან 50 მდე მხოლოდ სამის ჯერადი რიცხვები
for i in range(0,50,3):
  print(i)
#  9) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი
num = int(input("please enter a number"))

for i in range(num):
  print(i)
#  10) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვები
num = int(input("please enter a number"))

for i in range(0,num,2):
  print(i)
#  11) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ კენტი რიცხვები
for i in range(1,num,2):
  print(i)
#  12)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი
num = int(input("please enter a number"))

for z in range(num):
  
  if z % 2 == 0:
    print("number is even",z)
  
  elif z % 2 != 0:
    print("number is odd",z)
#  13) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები
num = int(input("please enter a number"))

for i in range(0,num,5):
  print(i)