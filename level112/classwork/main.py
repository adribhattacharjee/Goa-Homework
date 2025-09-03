def find_smallest_int(arr):
    small = arr[0]
    for i in arr:
        if i < small:
            small = i
    