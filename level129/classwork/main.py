# codewars 
def sum_even_numbers(seq): 
    result = 0
    for i in seq:
        if i % 2 == 0:
            result += i
    return result
