def max_of_list(numbers):
    max_number = numbers[0]
    second_max = numbers[1]

    for number in numbers:
        if number > max_number:
            second_max = max_number
            max_number = number
        elif number > second_max and number != max_number:
            second_max = number

    return max_number, second_max


print(max_of_list([11, 4, 72, 3, 10, 5, 8]))
    


