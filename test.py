import math

def func(n):
    isFlag = True  # True = Primzahlen

    for i in range(2, n):
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                isFlag = False
                break

        if isFlag == True:
            print(i)
        isFlag = True

num = 10000000
print(func(num))