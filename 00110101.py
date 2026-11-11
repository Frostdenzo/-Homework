summa = 0
maximum = None
minimum = None

while True:
    number = int(input("Введіть число: "))

    if number == 7:
        print("Good bye!")
        break

    summa = summa + number

    if maximum is None or number > maximum:
        maximum = number

    if minimum is None or number < minimum:
        minimum = number

print("Сума:", summa)

if maximum is not None:
    print("Максимум:", maximum)
    print("Мінімум:", minimum)
else:
    print("Чисел для обчислення не введено.")
