# # 2) for ციკლის გამოყენებით დაბეჭდე რიცხვები 1-დან 10-მდე
for i  in range(1,10):
    print(i)
# # 3) მომხარებელს შემოატანინე სახელი და რიცხვი. გამოიყენე for ციკლი და რა რიცხვიც გადმოგეცა, იმდენჯერ დაბეჭდე მომხარებლის სახელი
name = input("enter your name: ")
number = int(input("enter a number: "))
for i in range(number):
    print(name)
# 4) მომხარებელს შემოატანინე რიცხვი და დაბეჭდე 1-დან გადმოცემულ რიცხვამდე ყველა რიცხვი
number = int(input("enter a number: "))
for i in range(1,number):
    print(i)
# 5) შეე2ცადე დაბეჭდო 1-დან 10-მდე ყველა ლუწი რიცხვი
for i in range(2,10,):
    print(i)