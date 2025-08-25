# 2) მომხარებელს შემოატანინე რიცხვი, თუ ის ლუწია დაბეჭდე "Number is Even", სხვა შემთხვევაში "Number is Odd"
number = int(input("enter a number: "))

if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
# 3) მომხარებელს შემოატანინე მისი სახელი და თუ ის არის "John"-ი, დაბეჭდე "Hello Admin", სხვა შემთხვევაში "Hello user"
name = input("enter a name: ")
name2 = "john"
if name == name2:
    print("hello Admin")
else:
    print("Hello user")
# 4) კომენატებით ახსენი თუ რა არის if/else და რაში გამოიყენება ის
# if/else ето функция которая нам помогает выйбрать одно между многими условиями и выполнить его.