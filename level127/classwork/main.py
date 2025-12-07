# codewars 1
def monkey_count(n):
    result = []
    
    for i in range(1,n + 1):
        result.append(i)
    return result
# codewars 2
def divisible_by(numbers, divisor):
    list = []
    for  i in numbers:
        if i % divisor == 0:
            list.append(i)
    return list
# codewars 3
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
# codewars 4
def string_to_number(s):
    return int(s)
# codewars 5
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
# codewars 6
def past(h, m, s):
    return s * 1000 + m * 60000 + 60000 * h * 60
# codewars 6
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / fuel_left <= mpg
# codewars 6
# codewars 6