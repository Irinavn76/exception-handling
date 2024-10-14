# Запрашиваем ввод двух чисел


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2

    # Обрабатываем исключение ValueError (ввели не числовое значение)


except:
    ValueError
print("Ошибка: Введено не число!")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

# Обрабатываем исключение ZeroDivisionError (деление на ноль)


except:
    ZeroDivisionError
print("Ошибка: Деление на ноль!")

# Выводим результат при успешном выполнении деления


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("10 / 2 = 5")

# Завершение работы программы через блок finally


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2

finally:
    print("Завершение работы программы")

# Спасибо за Ctrl+Alt+L )))