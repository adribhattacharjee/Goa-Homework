# 1) მომხარებელს შემოატანიე 1 რიცხვი და while ციკლის გამოყენებით დაბეჭდე 0-დან შემოტანილი რიცხვის ჩათვლით ყველა რიცხვი
# number1 = int(input("enter a number: "))
# number2 = 0
# while number2 <= number1:
#     print(number2) 
#     number2+=1
# 2) მომხარებელს შემოატანინე ასაკი და თუ ის ნაკლებია 18-ზე დაბეჭდე "Discount 20%", სხვა შემთხვევაში თუ ის მეტია 75-ზე დაბეჭდე "Discount 10%". სხვა შემთხვევაში დაბეჭდე "No Discount"
# age = int(input("enter your age"))

# if age < 18:
#     print("discount 20%")
# elif age > 75:
#     print("discount 10%")
# else:
#     print("no discount")
# 3) მომხარებელშ შემოატანინე პაროლი. for ციკლით დაითვალე მისი სიგრძე და თუ ის ნაკლებია 6-ზე დაბეჭდე "Password is to sort", სხვა შემთხვევაში დაბეჭდე "Password is good"
password = input("enter a password: ")
number = 0
for i in password:
    number += 1
if number < 6:
    print("password is to sort")
else:
    print("password is good")