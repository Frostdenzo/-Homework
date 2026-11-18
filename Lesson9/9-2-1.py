def factorial_list(n):
    result = []
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        result.append(factorial)

    return result


number = int(input("Введите число: "))
print(factorial_list(number))

