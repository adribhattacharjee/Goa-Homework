# Строковое срезание — Объединение слов Дано: str1 = “backward” str2 =
# “forward” Вернуть новую строку, составленную из первых 3 букв str1 и
# последних 4 букв str2. Результат: “bacward” Использовать только
# срезы.
str1 = "backward"
str2 = "forward"
print (str1[0:3] + str2[3:])

# Функция — Объединение половинок двух слов Напишите функцию
# mix_halves(a, b), которая возвращает: вторую половину a + первую
# половину b. Пример: a = “planet”, b = “system” → “netsys”

def a_b(a,b):
    print(a[3:] + b[0:4])
print(a_b("planet","system"))

# Словарь — Преобразование в одно предложение Дано: info = {“brand”:
# “Tesla”, “model”: “Model S”, “year”: 2020, “electric”: True}
# Вернуть: “Это 2020 Tesla Model S, и она электрическая.”

info = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2020,
    "electric": True
}

print(f" This is a {info['year']} {info['brand']} {info["model"]} and it is electric")

# Цикл — Извлечение длины слов Дан список: words = [“silver”, “nova”,
# “horizon”, “ember”, “flux”] Создать новый список, содержащий длину
# каждого слова с помощью цикла for. Результат: [6, 4, 7, 5, 4]
words = ["silver", "nova", "horizon", "ember", "flux"]
len_words = []
for i in words:
    len_words.append(len(i))
print (len_words)

# Фильтр — Слова с более чем 3 гласными Напишите функцию
# vowel_rich(words), которая возвращает только те слова, в которых
# больше 3 гласных. Пример: [“audio”, “crystal”, “queue”, “sky”] →[“audio”, “queue”]
def vowel
vowel_rich = ["audio", "crystal", "queue", "sky"]
words = []
for word in vowel_rich:
    count = "" 
    for i in word:
        if i in "aeou":
            count += i