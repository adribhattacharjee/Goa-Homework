
def multiply_two():
    num1 = int(input("please enter a number"))
    num2 = int(input("please enter a number"))

    print(num1 * num2)

# multiply_two()
# multiply_two()
# multiply_two()

# def from1_to_number():
#     num3 = int(input("please enter a number"))

#     for i in range(1,num3):
#         print(i)

# from1_to_number()

def number_to_number(x):
    for i in range(0,x + 1,2):
        print(i)

number_to_number(10)

def func(names):
    
    for i in names:
        for x in i:
            print(x)
func(["Adri","Nika","Irakli"])