
def list_slicer(list1, integer):
    sliced_list = list1[integer:]
    result_list = []
    for i in sliced_list:
        if i % 2 != 0:
            result_list.append("Odd")
        else:
            result_list.append("Even") 
    return result_list


test = [12,543,57,3,5,57,8]

print(list_slicer(test, 4)) 