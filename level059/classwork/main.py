# 1) მომხარებელს შემოატანინე ნებისმიერი სიტყვა, დაბეჭდე მისი თითოეული სომბოლო და გვერდით მიუწერე რიგით რომელი ნომერია ეს.
word = input("enter a word: ")
index = 1
for i in word:
    print(i+" - "+str(index))
    index = index + 1
# 2) მომხარებელს შემოატნინე რიცხვი და 1-დან შემოტანილი რიცხვის ჩათვლით დაბეჭდე ყველა რიცხვი კვადრატშ
number = int(input("enter a number"))

for i in range(1,number+1):
    print(i*i)