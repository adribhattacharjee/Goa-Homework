# codewars (basic math operations)
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
    
# codewars lost without a map
def maps(a):
    doubled = []
    for i in a:
        doubled.append(i * 2)
    return doubled