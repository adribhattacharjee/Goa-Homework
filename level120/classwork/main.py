# codewars1
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
# codewars 2
def repeat_str(repeat, string):
    str = ""
    for i in range(repeat):
        str += string
    return str
#  codewars 3
def solution(string):
    return string[::-1]
#  codewars 4
def sum_array(a):
    if a == []:
        return 0
    sum1 = 0
    for i in range(len(a)):
        sum1 += a[i]
    return sum1
# codewars 5
def digitize(n):
    str_n = str(n)
    list = []
    for i in range(len(str_n)-1,-1,-1):
        list.append(int(str_n[i]))
    return list
# codewars 6
def find_smallest_int(arr):
    small = arr[0]
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
    return small
#  codewars 7
def summation(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
#  codewars 8
def abbrev_name(name):
    first,second = name.split()
    return first[0].upper() + "." + second[0].upper() 
#  codewars 9
def simple_multiplication(number) :
    if number %2 == 0:
        return number * 8
    else:
        return number * 9