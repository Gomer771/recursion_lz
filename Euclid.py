def evklid(a, b):#вызываем функцию
    if (b == 0):#задаём условие если второе число равно 0, то
        return a#возвращаем в значение а 
    else:#в противном случае
        return evklid(b, a % b) #возвращаем значение в b и делим a на b
a = int(input("Введите первое число:"))#вводим с клавиатуры првое число
b = int(input("Введите второе число:"))#вводим с клавиатуры второе число
evklid_1 = evklid(a, b)#присваиваем значение
print("НОД:", evklid_1)#выводим значение