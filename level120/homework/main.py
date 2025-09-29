# codewars 1
def lovefunc( flower1, flower2 ):
    return flower1 %2 != flower2 %2
# codewars 2
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
# codewars 3
def smash(words):
    return " ".join(words)
# codewars 4
def bmi(weight, height):
    bmi1 = weight / height ** 2
    if bmi1 <= 18.5: 
        return "Underweight"
    elif bmi1 <= 25.0:
        return "Normal"
    elif bmi1 <= 30.0:
        return "Overweight"
    elif bmi1 > 30:
        return "Obese"