a = float(input("введите число: "))
b = float(input("введите число: "))
c = float(input("введите число: "))

action =input("виберіть дію:\n1 - максимальне з трьох \n2 - мінімальне з трьох \n3 - середньоарифметичне трьох чисел \n Ваш вибір: ")

if action == "1":
    result = max(a, b, c)
    print("Максимум із трьох чисел:", result)
elif action == "2":
    result = min(a, b, c)
    print("Мінімум із трьох чисел:", result)
elif action == "3":
    result = (a + b + c) / 3
    print("Середньоарифметичне трьох чисел:", result)
else:
    print("Невірний вибір. Введіть 1, 2 або 3.")

