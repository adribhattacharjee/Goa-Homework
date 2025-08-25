# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 2 to 20
for i in range(2, 21):
    if i % 2 == 0:
        print(i)

# 3. Use a while loop to print numbers from 5 down to 1
sum = 5

while sum >= 1:
    print(sum)
    sum -= 1
# 4. Calculate the sum of numbers from 1 to 100
sum1 = 0
for i in range(1, 101):
    sum1 += i
print("Sum:", sum1)

# 5. Print numbers starting from 1, but stop if the number is 7
for i in range(1, 100):
    if i == 7:
        break
    print(i)

# 6. Print numbers from 1 to 10, skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 7. Ask the user to enter numbers and print them until they enter 0
num = int(input("please enter a number"))

while True:
    num = int(input("please enter a number"))
    if num == 0:
        break
# 8. Keep summing the numbers entered by the user until they enter 0
num1 = int(input("please enter a number"))

num2 = 0

while True:
    num1 = int(input("please enter a number"))
    if num1 != 0:
        num2 += num1
    break
print(num2)
# 9. Print all numbers from 1 to 50 that are not divisible by 3
for i in range(1, 51):
    if i % 3 != 0:
        print(i)

# 10. User enters numbers. When they enter 0, print the smallest number entered
