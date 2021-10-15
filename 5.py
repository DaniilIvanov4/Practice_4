x = int(input("Введи количество строк: "))
kolvo_probelov = 0
while kolvo_probelov < x:
    print('#', end='')
    probel_print = 0
    while probel_print < kolvo_probelov:
        print(' ', end='')
        probel_print += 1
    print('#')
    kolvo_probelov += 1