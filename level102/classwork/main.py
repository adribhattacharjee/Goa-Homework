# 1. **Приветствие**
def hi(name):

    print("hello " + name)

hi("adri")
#    * Напиши функцию `greet(name)`, которая принимает имя и выводит: "Привет, \[имя]!"

# 2. **Сумма двух чисел**
def add(a,b):
    
    print(a + b)

add(10,21)
#    * Напиши функцию `add(a, b)`, которая возвращает сумму двух чисел.

# 3. **Удвоение числа**
def double(n):

    print(n * 2)

double(20)
#    * Напиши функцию `double(n)`, которая возвращает число, умноженное на 2.

# 4. **Проверка на чётность**
def is_even(n):

    if n % 2 == 0:
        print(True)
    elif n % 2 != 0:
        print(False)

is_even(27736762)
#    * Напиши функцию `is_even(n)`, которая возвращает `True`, если число чётное, и `False` — если нечётное.

# 5. **Максимум из двух**
def max_of_two(a,b):

    if a > b:
        print(a)
    elif b > a:
        print(b)
max_of_two(20,11)
#    * Напиши функцию `max_of_two(a, b)`, которая возвращает большее из двух чисел.

# 6. **Проверка возраста**
def is_adult(age):

    if age >= 18 :
        print(True)
    else:
        print(False)
is_adult(17)
#    * Напиши функцию `is_adult(age)`, которая возвращает `True`, если возраст 18 или больше.

# 7. **Сравнение строк**
def is_same(s1,s2):

    if s1 == s2:
        print(True)
    elif s1 != s2:
        print(False)

is_same("hi my name is Adri","hi my name is Nika")
#    * Напиши функцию `is_same(s1, s2)`, которая возвращает `True`, если строки одинаковые.

# 8. **Сумма трёх чисел**
def max_of_three(a, b, c):

    print(a + b + c)

max_of_three(20,22,21)
#    * Напиши функцию `sum_three(a, b, c)`, которая возвращает сумму трёх чисел.

# 9. **Простое сравнение трёх чисел**
def max_of_three(a, b, c):

    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
max_of_three(222,333,3333333)
#     * Напиши функцию `max_of_three(a, b, c)`, которая возвращает наибольшее из трёх чисел.

# 10. **Кратность числа**
def is_multiple_of(x, y):

    if x % y == 0:
        print(True)
    else:
        print(False)
#     * Напиши функцию `is_multiple_of(x, y)`, которая возвращает `True`, если `x` делится на `y`.

# 11. **Оценка по баллам**
def grade(score):
    
    if score >= 90:
        print("Great")
    elif score >= 75:
        print("good")
    elif score >= 60:
        print("Satisfactorily")
    else:
        print("Unsatisfactory")
grade(90)
#     * Напиши функцию `grade(score)`, которая возвращает строку:

#       * `"Отлично"` — если `score >= 90`
#       * `"Хорошо"` — если `score >= 75`
#       * `"Удовлетворительно"` — если `score >= 60`
#       * `"Неудовлетворительно"` — если меньше 60