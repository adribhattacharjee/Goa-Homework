words = ["ember", "whisper", "orbit", "velvet", "cascade"]
words1 = []
for i in words:
    words1.append(len(i))
print(words1)

word = "I am your new neighbor"
word1 = []
count = 0

for i in word: 
    if i != " ": # თუ space-ზე არ ვდგავართ თვლას მოუმატოს
        count += 1
    elif i == " ": # თუ space-ზე ვდგავართ დათვლილი შედეგი ჩაამატოს ლისტში
        word1.append(count)
        # თვლა გაანულოს რომ შემდეგი სიტყვის სიგრძე დავთვალოთ 
        count = 0
 # რადგან ბოლო სიტყვის შემდეგ space-ი არ არის ამიტომ ბოლო
 # სიტყვის სიგრძეს აღარ ჩაამატებს
 # და ვამატებთ if-ის დახმარებით. True გვჭირდება რადგან ყველა        # ვარიანტში უნდა გაეშვას შიგნით მოცემული კოდი, ყველა     # ვარიანტში ჩაემატოს ბოლო სიტყვის სიგრძე 
if True:
    word1.append(count)
print(word1)