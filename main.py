while True:
    print("Пожалуйста введите 2 числа")
    first = int(input())
    second = int(input())
    print("Выберите операцию: 1 - сложение; 2 - вычитание; 3 - умножение; 4 - деление")
    operation = int(input())
    if operation == 1:
        print(first + second)
    elif operation == 2:
        print(first - second)
    elif operation == 3:
        print(first * second)
    elif operation == 4 and second != 0:
        print(first / second)
    else:
        print("Некорректный ввод")
