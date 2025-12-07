# input-ით შემოტანილი რიცხვი ნულია თუ არა — დაბეჭდე "ნულია" ან "არ არის ნული" ternary operator–ით.
# შეინახე ცვლადში ეს ყველაფერი და შემდეგ დაპრინტე. if-ში არ გამოიყენო პრინტი!!!
number = int(input("please enter the number: "))

result = "zero" if number == 0 else "not zero"

print(result)
# input-ით შემოტანილი სტრინგის სიგრძე თუ მეტია 9ზე დააბრუნე "Good Job" სხვა შემთხვევაში "Lazy"
# შეინახე ცვლადში ეს ყოველივე და დაპრინტე. if-ში არ გამოიყენო პრინტი!!!

number1 = input("enter a text: ")

result1 = "Good Job" if len(number1) > 9 else "Lazy"

print(result)

