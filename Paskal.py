#построение треугольника паскаля


def combination(n, k):# вызываем функцию с 2 аргументами

    if k == 0 or k == n:#если к равно 0 или n, то
        return 1#возвращаем 1
    return combination(n - 1, k - 1) + combination(n - 1, k)#Если k не равно 0 и n, функция вызывает саму себя с новыми аргументами

def pascals_triangle(lines):#функция для колличества строк

    for line in range(lines):#цикл
        current = "" #пустая строка, для хранения значения текущей строки
        for column in range(line + 1):#цикл для столбцов 
            current = current + str(combination(line, column)) + "\t"#вычесление биноминального коэфицента  
        print(current)#вывод


lines = int(input("Введите количество строк: "))#вводим количества строк с клавиатуры
pascals_triangle(lines)#вызов функции
