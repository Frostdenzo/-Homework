a = int(input("Введите число A: "))
n = int(input("Введите степень N: "))

result = 1

for i in range(n):
    result = result * a

print(result)
