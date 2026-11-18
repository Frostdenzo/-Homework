def classify_numbers(numbers):
    even = []
    odd = []
    positive = []
    non_positive = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

        if number > 0:
            positive.append(number)
        else:
            non_positive.append(number)

    return even, odd, positive, non_positive


numbers = [-5, -4, -1, 0, 2, 3, 6, 9]

even, odd, positive, non_positive = classify_numbers(numbers)

print("Парні числа:", len(even))
print("Непарні числа:", odd)
print("Позитивні числа:", positive)
print("Непозитивні числа:", non_positive)
