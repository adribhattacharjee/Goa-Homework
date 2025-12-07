# codewars 1
def get_average(marks):
    avg_score = sum(marks) / len(marks) 
    return int(avg_score)
# codewars 2
def sum_mix(arr):
    result = 0
    for i in arr:
        result += int(i)
    return result
# codewars 3
def get_count(sentence):
    count = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            count += 1
    return count
# codewars 4
def high_and_low(numbers):
    arr = numbers.split(" ")
    arr1 = []
    for i in arr:
        arr1.append(int(i))
    return f"{max(arr1)} {min(arr1)}"
# codewars 5
def DNA_strand(dna):
    result = ""
    for i in dna:
        if i == "A":
            result += "T"
        elif i == "T":
            result += "A"
        elif i == "G":
            result += "C"
        elif i == "C":
            result += "G"
    return result
