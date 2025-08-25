# 1. დავალება
# შეიყვანე ორი რიცხვი და შეადარე ისინი:

# თუ პირველი რიცხვი მეტია მეორეზე და მათი ჯამი ლუწია, დაბეჭდე "პირველი რიცხვი დიდია და ჯამი ლუწია".

# თუ მეორე რიცხვი მეტია პირველზე ან მათი სხვაობა ნაკლებია 10-ზე, დაბეჭდე "მეორე რიცხვი დიდია ან სხვაობა მცირეა".

# სხვა შემთხვევაში დაბეჭდე "არავითარი პირობა არ შესრულდა".

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

if num1 > num2 and (num1 + num2) % 2 == 0:
    print("num1 is biger than num2 and the sum is even")

elif num2 > num1 or (num2 - num1) < 10:
    print("num2 is biger or the difference is less than ten")
else:
    print("No condition is met")

# 2. დავალება
# შეიყვანე ასაკი და ფული:

# თუ ასაკი მეტია 18-ზე და ფული 100-ზე მეტია, დაბეჭდე "შეგიძლია კლუბში შესვლა".

# თუ ასაკი ნაკლებია 18-ზე ან ფული ნაკლებია 100-ზე, დაბეჭდე "კლუბში შესვლა შეუძლებელია".

# სხვა შემთხვევაში დაბეჭდე "გადამოწმება საჭიროა".


age = int(input("Enter your age: "))
money = float(input("Enter the amount of money you have: "))

# Checking the conditions
if age > 18 and money > 100:
    print("You can enter the club")
elif age < 18 and money < 100:
    print("You cannot enter the club")
else:
    print("Further verification is needed")



# 4. დავალება
# განსაზღვრე რიცხვი:

# თუ რიცხვი იყოფა 3-ზე და 5-ზე, დაბეჭდე "რიცხვი იყოფა 3-ზეც და 5-ზეც".

# თუ იყოფა მხოლოდ 3-ზე, დაბეჭდე "რიცხვი იყოფა 3-ზე".

# თუ იყოფა მხოლოდ 5-ზე, დაბეჭდე "რიცხვი იყოფა 5-ზე".

# სხვა შემთხვევაში დაბეჭდე "რიცხვი არ იყოფა არცერთზე".


num = int(input("Enter a number: "))

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif num % 3 == 0:
    print("The number is divisible by 3")
elif num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by either")




# 5. დავალება
# შეიყვანე რიცხვი და გაამრავლე ის 2-ზე, შემდეგ დაამატე 10 და დაყავი 3-ზე ((n * 2 + 10) / 3):

# თუ საბოლოო შედეგი მეტია 20-ზე ან 30-ზე ნაკლებია, დაბეჭდე "შედეგი კარგიია".

# თუ ზუსტად 20-ს უდრის, დაბეჭდე "შედეგი ზუსტად 20-ია".

# სხვა შემთხვევაში დაბეჭდე "სხვანაირი შედეგი".



num = float(input("Enter a number: "))

# Perform the calculation
result = (num * 2 + 10 / 3)

# Check the result
if result == 20:
    print("The result is exactly 20")
elif result > 20 or result < 30:
    print("The result is good")
else:
    print("A different result")