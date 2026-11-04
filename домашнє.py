# Запитуємо числа
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
if number1 < number2:
    start = number1
    end = number2
else:
    start = number2
    end = number1
result = 1
count = 0
for i in range(start, end + 1):
    # Перевіряємо ділення на 4
    if i % 4 == 0:

      if i % 6 != 0:
            result = result * i
            count = count + 1

if count > 0:
    print("Добуток чисел дорівнює:")
    print(result)
else:
    print("Чисел, що діляться на 4, але не діляться на 6, немає.")
