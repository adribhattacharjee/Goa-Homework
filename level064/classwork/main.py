# 1) კომენტარებით ახსენი შემდეგი კოდი:

password = "1234"

user_input = input("Please enter your password: ")
tries = 1
while user_input != password:
    print("Password is incorrect!")
    user_input = input("Please enter your password: ")
    tries += 1
    
print("Password is correct!")
print("It took you " + str(tries) +  " tries")
# с начала мы создали переменную в которой мы хроним пороль, потом мы запрашиваем пороль у клиента. потом tries нам нужно чтобы когда клиент захочет узнать сколько попыток ему 