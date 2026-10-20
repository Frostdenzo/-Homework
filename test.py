# Введення трьох чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

# Вибір дії
choice = input("Оберіть дію:\n1 - Максимум із трьох\n2 - Мінімум із трьох\n3 - Середньоарифметичне трьох чисел\nВаш вибір: ")

if choice == "1":
    result = max(a, b, c)
    print("Максимум із трьох чисел:", result)
elif choice == "2":
    result = min(a, b, c)
    print("Мінімум із трьох чисел:", result)
elif choice == "3":
    result = (a + b + c) / 3
    print("Середньоарифметичне трьох чисел:", result)
else:
    print("Невірний вибір. Введіть 1, 2 або 3.")
