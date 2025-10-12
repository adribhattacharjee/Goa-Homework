# codewars 1
def minimum(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min

def maximum(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
# codewars 2
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
# codewars 3
def points(games):
    points = 0 
    for score in games:
        if int(score[0]) > int(score[2]):
            points += 3
        elif int(score[0]) == int(score[2]):
            points += 1
    return points