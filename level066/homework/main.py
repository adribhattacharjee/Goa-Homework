# 1) დაასრულე საკლასო დავალება:
# მომხარებელს შემოატანინე რიცხვი და თუ ის იყოფა 3-ზეც და 5-ზეც დაბეჭდე ეს რიცხვი გაყოფილი 5-ზე, სხვა შემთხვევაში დაბეჭდე ეს რიცხვი გამრავლებული 5-ზე
number = int(input("enter a number"))

if number % 3 == 0 and number % 5 == 0:
    print(number / 5)
else:
    print(number * 5)
# 2) მომხარებელს შემოატანინე რიცხვი. 1-დან შემოტანილი რიცხვის ჩათვლით შეამოწმე ყველა რიცხვი, თუ ის ლუწია დაბეჭდე "Number is Even", სხვა შემთხვევაში "Number is Odd"
number = int(input("enter a number"))

if number % 2 == 0:
    print("number is odd")
else:
    print("number is even")
# 3) მომხარებელს შემოატანინე ორი რიცხვი. შემდეგ შეამოწმე და ნაკლები რიცხვიდან დიდი რიცხვის ჩათვლით დაბეჭდე ყველა რიცხვი გამრავლებული 5-ზე
number1 = int(input("enter a number"))
number2 = int(input("enter a number"))
if number1 >  number2:
    for i in range(number2,number1+1):
        print(i*5)
# 4) ბევრი ივარჯიშე შედარების და ლოგიკურ ოპერატორებზე, გააკეთე რამოდენიმე მაგალითი.
