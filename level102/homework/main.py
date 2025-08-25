# 1) შექმენი ფუნქცია(factorial), რომელიც დაბეჭდავს გადაცემული რიცხვის ფაქტორიალს.

# რიცხვის ფაქტორიალი არის, ერთიდან იმ რიცხვამდე ყველა რიცხვის ნამრავლი.
# მაგალითად, მომხმარებელმა თუ შემოიყვანა 5, მისი ფაქტორიალია 1 * 2 * 3 * 4 * 5 = 120
# def multiply():
#     num = int(input("please enter a number"))
#     num1 = 1
#     for i in range(1,num + 1):
#         num1 *= i
#     print(num1)
# multiply()
# 2) შექმენი ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს და დაბეჭდავს True-ს თუ ის მარტივია, სხვა შემთხვევაში დაბეჭდავს False-ს.
# def parametr(x):
#     if x % 
# მარტივია რიცხვი, რომელიც იყოფა მხოლოდ 1-ზე და საკუთარ თავზე. ნებისმიერი სხვა რიცხვი რთულია.

# 3) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა რიცხვს.
# def from_one_to_number():
#     num = int(input("please enter a number"))
#     for i in range(1,num):
#         print(i)
# from_one_to_number()
# 4) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს, და დაბეჭდავს რიგით მე-5 ლუწ რიცხვს შემოტანილი რიცხვის შემდეგ.
# def num():
#     num = int(input("please enter a number"))
#     if num % 2 == 0:
#         print(num + 10)
#     else:
#         print(num + 9)
# num()
    
# 5) შექმენი ფუნქცია, რომელიც მიიღებს string-ს, შემდეგ კი შექმნის ახალ string-ს, სადაც თითოეული სიმბოლო იქნება გამეორებული ორჯერ და დაბეჭდავს მიღებულ string-ს
def text_multiply(x):
    text1 = ""
    for i in x:
        text1 += i * 2
    print(text1)
text_multiply("Hello")
text_multiply("my name is adri")
# მაგალითად: "Hello" -> "HHeelllloo"