# codewars 1
def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result
# codewars 2
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 90:
        return "B"
    elif score >= 70 and score <= 80:
        return "C"
    elif score >= 60 and score <= 70:
        return "D"
    elif score >= 0 and score <= 60:
        return "F"
# codewars 3
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
# codewars 4
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
# codewars 5
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
# codewars 6
def area_or_perimeter(l , w):
    if l == w:
        return l * w 
    else:
        return (l + w) * 2
# codewars 7
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False
# codewars 8
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)