# names = ["nikolozi", "gio", "lika", "adnria"]
# names1 = []
# for name in names:
#     if len(name) > 4:
#         names1.append(name)
# print(names1)

nums = [12,42,65,90,33,89,11]
str1 = []
for num in nums:
    str1.append(str(num))
for string in str1:
    if int(str1[0]) + int(str1[1]) > 5:
        print(int(string))