# Метод золотого сечения
# f (x) = −x^2 + 5x − 6  --> min на [−5, 2,5]
# f (x) = x^4 −10x^3 +36x^2  + 5x на отрезке [3, 5].
import math


def funcFirst(x):
    return -(math.pow(x, 2)) + 5 * x - 6


def funcSecond(x):
    return math.pow(x, 4) - 10 * math.pow(x, 3) + 36 * math.pow(x, 2) + 5 * x


def GoldenSectionMethod(func, a_start, b_start, eps):
    a = a_start
    b = b_start
    inter = b - a
    x1 = a + (((3 - math.sqrt(5)) / 2) * (b - a))
    x2 = a + (((math.sqrt(5) - 1) / 2) * (b - a))
    y1 = func(x1)
    y2 = func(x2)

    while inter > eps:
        if y1 > y2:
            a = x1
            x1 = x2
            x2 = a + (math.sqrt(5) - 1) / 2 * (b - a)
            y1 = y2
            y2 = func(x2)

        else:
            b = x2
            x2 = x1
            x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
            y2 = y1
            y1 = func(x1)

        inter = b - a
    print(a, b)
    return (a + b) / 2.0


eps = 0.001

resultFirst = GoldenSectionMethod(funcFirst, -5, 2.5, eps)
resultFirstFunc = funcFirst(resultFirst)

print("1 функция: " + str(resultFirst), str(resultFirstFunc))

resultSecond = GoldenSectionMethod(funcSecond, 3, 5, eps)
resultSecondFunc = funcSecond(resultSecond)

print("2 функция: " + str(resultSecond), str(resultSecondFunc))
