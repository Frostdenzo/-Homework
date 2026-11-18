def sum_and_avg(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    print("Сума:", total)
    print("Середнє значення:", average)


sum_and_avg([11, 4, 72, 3, 10, 5])
