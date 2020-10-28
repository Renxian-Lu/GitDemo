import math

def func(n):
    isFlag = True  # True = Primzahlen

    for i in range(2, n):
        j=2
        while j <= math.sqrt(i):
            if i % j == 0:
                isFlag = False
                break
            j += 1

        if isFlag == True:
            print(i)
        isFlag = True

num = 50
print(func(num))
11111
