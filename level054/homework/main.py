# 1) დაწერე პროგრამა, რომელიც მომხარებელს შემოატანინებს ორ რიცხვს, როგორც string-ს. შეუცვლის მათ მონაცემთა ტიპს integer-ად და დაპრინტავს მათ ჯამს
age = input("пожалуйста введите число")
print(type(age))
age = int(age)
print(type(age))
age = float(age)
print(type(age))
# 2) დაწერე პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და შეამოწმებს არის თუ არა ის უარყოფითი(0-ზე ნაკლები). თუ კი დაბეჭდე True, სხვა შემთხვევაში დაბეჭდე False
# 2)

number = int(input("Please enter a number: "))

print(number < 0)

# 3)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)

# 4)

number = int(input("Please enter a number: "))

print(number > 100)
# 3) დაწერე პროგრამა, რომელიც მომხარებელს შემოატანინებს ორ ირცხვს. დაბეჭდე მიღებული რიცხებიდან მაქსიმუმი

# 4) დაწერე პროგრამა, რომელიც მომხარებელს შემოატნინიებს რიცხვს და შეამოწმებს არის თუ არა ეს რიცხვი 100-ზე მეტი. თუ კი დაბეჭდე True, სხვა შემთხვევაში დაბეჭდე False