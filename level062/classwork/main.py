# გადახედე შემდეგ კოდს და კომენტარის სახით ახსენი თითოეული დეტალი
password = "goa123"

user_pass = input("Please enter a number: ")

while user_pass != password:
    print("Incorrect password! Try again")
    user_pass = input("Please enter a number: ")

print("Password is correct")

# с начала в етом коде в переменой password мы пишем пороль за тем мы запрашиваем у ползавателя чтобы он ввел пороль потом мы пишем цикл while и етот цикл будет запрашивать пороль пока ответ не будет true но если ответ будет false он будет выводить incorect password! try again но если true то он выведет password is correct и цыкл while остановится