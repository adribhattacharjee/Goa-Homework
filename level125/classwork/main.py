# codewars 1
def greet(name):
    name1 = f"Hello, {name} how are you doing today?"
    return name1
# codewars 2
def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    
    for i in arr:
        if i > 0:
            count += 1
        else:
            sum += i
    if len(arr) == 0:
        return []
    return [count,sum]
# codewars 3
def boolean_to_string(b):
    return f"{b}"
# codewars 4
def no_space(x):
    result = ""
    
    for i in x:
        if i != " ":
            result += i
    return result
# codewars 5
def grow(arr):
    num = 1
    for i in arr:
        num *= i
    return num
# codewars classwork 6
def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == "T":
            rna += "U"
        else:
            rna += i
    return rna
# codewars 7
def make_upper_case(s):
    return s.upper()
# codewars 8
def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
# codewars 9
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "rock")or (p1 == "paper" and  p2 == "scissors") or (p1 == "rock" and p2 == "paper"):
        return "Player 2 won!"
    else:
        return "Player 1 won!"