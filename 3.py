x = int(input("Введи неотрицательное число "))
def factor(n):
    if n == 0:
        return 1
    return factor(n - 1) * n
if x > 0:
    print(factor(x))
else:
    print(1)



