# Homework level118
# 1. მოცემულია ორი სტრინგი str1 = "fireplace" str2 = "racingtruck"  შენი დავალებაა დააბრუნო "firetruck".
#  მინიშნება: დაასლაისე და დაუმატე ერთმანეთს

str3 = "fireplace"
str4 = "racingtruck"

print(str3[0:4]+str4[-5:])
# 2.მოცემულია ორი სტრინგი str1 = "ecapl" str2 = "nice" შენი დავალებაა დააბრუნო "niceplace": მინიშნება: str1 უნდა შეატრიალო და შემდეგ str2-ს დაუმატო str1
str1 = "ecapl"
str2 = "nice"

result = str2 + str1[::-1]
print(result) 
# 3.შექმენი ფუნქცია რომელსაც გადაეცემა ერთი არგუმენტი strSlicer() გადაცემული არგუმენტი უნდა დააბრუნოს 
# მესამე ასოდან ბოლომდე: 
def strSlicer(str1):
    return str1[2:]
print(strSlicer("elephant"))
word = "tiger"
print(strSlicer(word))
# 4.  შექმენი ფუნქცია სახელად stringUnite(str1, str2) მას გადაეცემა ორი არგუმენტი str1 და str2 შენი მიზანია
#  პირველი სტრინგის დასაწყისიდან მესამე ასოს ჩათვლით გაუკეთო slice-ი str1-ს ხოლო მეორე სტრინგს ანუ 
# str2-ს გაუკეთე slice 4 ასოდან ბოლოს ჩათვლით.
# და შემდეგ მიუმატე ერთმანეთს და დააბრუნე.

def string(str1, str2):
    part1 = str1[:3]
    part2 = str2[3:]
    return part1 + part2
print(string(str1,str2))