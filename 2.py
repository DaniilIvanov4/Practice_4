print('Введите положительное число')
entered_number = 0
value = 0
while entered_number >= 0:
    value += entered_number
    entered_number = int(input('Введи число; '))
print('Окончательная сумма равна ', value)