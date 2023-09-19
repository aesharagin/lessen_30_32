max = int(input("Введите максимальное число массива: "))
min = int(input("Введите минимальное число массива: "))
array_1 = [-5, 9, 0, 30, -1, -2, 1, 4, -2, 10, 2, 0, -9, 80, 10, -9, 0, -5, -5, 7]

for i in range(len(array_1)):
    if min <= array_1[i] <= max:
        print(i)