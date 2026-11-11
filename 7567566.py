number = int(input("Введіть ціле число: "))

first = 0
second = 1
is_fibonacci = False

while first <= number:
    if first == number:
        is_fibonacci = True
        break

    next_number = first + second
    first = second
    second = next_number

if is_fibonacci:
    print("Число", number, "належить послідовності Фібоначчі")
else:
    print("Число", number, "не належить послідовності Фібоначчі")
