def num(X):

    if X % 2 == 0:
        return True
    else:
        return False
number = num(20)
print(number)

# 2) შექმენი ფუნქცია, რომელიც მიიღებს წინადადებას. ამ ფუნქციამ უნდა დააბრუნოს ხმოვანი ასოების რაოდენობა წინადადებაში. შემდეგ გამოიძახე ფუნქცია და ჩასვი ის print ფუნქციაში, რათა დაიბეჭდო დაბრუნებული პასუხი
def text(z):
    leter = 0
    for i in z:
        if i in "aeiou":
            leter += 1
    return leter
print(text("hello my name is adri"))





# 4) შექმენი ფუნქცია, რომელიც მიიღებს პარამეტრად რიცხვს და შეამოწმებს არის თუ არა ის დადებითი.
def num(z):
    if z > 0:
        return True
    else:
        return False
print(num(200))
# თუ ის დადებითია დააბრუნე True, სხვა შემთხვევაში False

def text():
    txt = "HELLO MY NAME IS ADRI".split()
    print(txt[])
text()