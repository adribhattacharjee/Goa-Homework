# დაასრულე საკლასო დავალება:

# 1) მომხარებელს, for ციკლის დახმარებით შემოატანინე 5 რიცხვი და დაბეჭდე მათი საშუალო არითმეტიკული
number = 0
for i in range(5):
    number += int(input("enter a number"))
print(number/5)
# 1) შექმენი პროგრამა, რომელიც მომხარებელს შემოატანინებს ლუწ რიცხვს. თუ მომხარებელმა შემოიტანა კენტი რიცხვი დაუბეჭდე "The Number is Odd" და იქამდე შემოატანინე ახალი რიცხვი სანამ ის არ იქნება კენტი.

# 3) კომენტარებით ახსენი რას აკეთებ elif-ი

# გააკეთე 5 if/else-ებზე
if number > 20:
    print("number is good")

name = "adri"
if name > 3:
    print("name succed the terminal")
else:
    print("name is small")

name = "adri"
if name < 6:
    print("name is good")
elif name > 6:
    print("name is very good")
else:
    print("name is small")

