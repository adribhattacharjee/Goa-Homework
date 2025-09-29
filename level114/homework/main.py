# Homework level 114
# მოცემულია მანქანების ლისტი cars = ["BMW", "Lexus", "Pagani", "Nissan", "Lamborghini", "Toyota"] 
# slicing-ის გამოყენებით:
# ახალ ცვლადში შეინახე სიის მხოლოდ კენტი ინდექსის მქონე ელემენტები (step-ი რომ ვისწავლეთ ეგ დაგჭირდება)
# ახალ ცვლადში შეინახე სია უკუღმა
# ახალ ცვლადში შეინახე მესამე ელემენტიდან მეხუთემდე ელემენტები
# ახალ ცვლადში შეინახე მხოლოდ შუა 2 მანქანა ანუ (pagani და nissan)

cars = ["BMW", "Lexus", "Pagani", "Nissan", "Lamborghini", "Toyota"]
cars1 = cars[1::2]
cars2 = cars[::-1]
cars3 = cars[2:5]
cars4 = cars[2:4]
print (cars1)
print (cars2)
print (cars3)
print (cars4)