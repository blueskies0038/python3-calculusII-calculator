def factorial(n):  # takes the factorial of any whole number
    fact = 1
    if n == 0:
        return 1
    elif n < 0:
        for i in range(n, 0):  # range is different for negative numbers
            fact *= i  # we don't use this in the project but I still included in the function
    for i in range(1, n + 1):
        fact *= i
    return fact


def pi():  # uses Nilakantha method to estimate pi
    multiplier = 1
    denominator = 2
    pi = 3  # first term is 3
    for i in range(1, 100001):
        pi += ((4.0 / (denominator * (denominator + 1) * (denominator + 2))) * multiplier)
        denominator += 2
        multiplier *= -1  # takes care of the alternating part
    return pi


def e(x):  # uses Brothers Formula to estimate e^x
    output = 0
    for i in range(1001):
        output += (x ** (2 * i) * (x + 2 * i + 1)) / (factorial(2 * i + 1))
    return output


def ln(x):
    n = 99999999
    return n * ((x ** (1 / n)) - 1)  # limit as n approaches infinity of ((x**(1/n))-1)(n)


def logBase(b, x):  # calculates the log base b of x
    return ln(x) / ln(b)  # Change of base rule


def sin(x):  # estimates the sin(x) by using a Taylor Polynomial
    if x > 2 * pi():  # we only care about the angle after x
        x = x % (2 * pi())  # has made as many revolutions as it can
    if x < -2 * pi():
        x = ((-1*x) % (2 * pi())) * -1
    pos = neg = 0
    for i in range(25):
        pos += (x ** (4 * i + 1)) / (factorial(4 * i + 1))  # sums up all the positive terms
        neg += (x ** (4 * i + 3)) / (factorial(4 * i + 3))  # sums up all the negative terms
    output = pos - neg
    if output > 0 and output < 1.0e-10:  # will take care of inaccuracy by returning 0 instead of a number
        return 0.0  # super close to 0 by using an +-1.0e-5 as the epsilon
    elif output < 0 and output > -1.0e-10:
        return 0.0
    return output


def cos(x):  # estimates the cos(x) by using a Taylor Polynomial
    if x > 2 * pi():
        x = x % (2 * pi())  # same concept as sin(x)
    if x < -2 * pi():
        x = ((-1*x) % (2 * pi())) * -1
    pos = neg = 0
    for i in range(25):
        pos += (x ** (4 * i)) / (factorial(4 * i))  # same concept as sin(x)
        neg += (x ** (4 * i + 2)) / (factorial(4 * i + 2))
    output = pos - neg
    if output > 0 and output < 1.0e-10:  # same concept as sin(x)
        return 0.0
    elif output < 0 and output > -1.0e-10:
        return 0.0
    return output


def tan(x):  # estimates tan(x)
    if cos(x) == 0.0:  # 1/0 is undefined
        return "undefined"
    return sin(x) / cos(x)


def csc(x):  # estimates csc(x)
    if sin(x) == 0.0:
        return "undefined"
    return 1 / sin(x)


def sec(x):  # estimates sec(x)
    if cos(x) == 0.0:
        return "undefined"
    return 1 / cos(x)


def cot(x):  # estimates cot(x)
    if sin(x) == 0.0:
        return "undefined"
    return cos(x) / sin(x)


def arctan(x):  # estimates arctan(x) of all Real numbers bounded by [-pi/2, pi/2]
    output = 0
    if x >= -1 and x <= 1:
        for i in range(100001):
            output += (-1) ** i * (x ** (2 * i + 1)) / (2 * i + 1)  # arctan as a power series
    elif x > 1:
        output = pi() / 2 - arctan(1 / x)
    else:
        output = -1 * pi() / 2 - arctan(1 / x)
    return output


def arccot(x):  # estimates arccot(x) of all Real numbers
    if x == 0:  # would make 1/x undefined, cot is 0 at pi/2
        return pi() / 2
    return arctan(1 / x)  # arccot(x) = arctan(1/x)


def arcsin(x):  # estimates arcsin(x), bounded by [-pi/2, pi/2]
    if x == -1 or x == 1:  # when the denominator is 0
        return x * pi() / 2  # arcsin(1) and arcsin(-1) are +- pi()/2
    return arctan(x / ((1 - x ** 2) ** 0.5))  # arcsin(x) = arctan(x/sqrt(1-x^2))


def arccos(x):  # estimates arccos(x), bounded by [0, pi]
    if x == 0:
        return pi() / 2
    output = arctan(((1 - x ** 2) ** 0.5) / x)  # arcos(x) = arctan(sqrt(1-x^2)/x)
    if x < 0:  # arcos(x) is bounded by [0, pi] while arctan(x) is bounded by +- pi/2
        output += pi()  # if arccos(x) is negative we have to add pi() to get to QII
    return output


def arccsc(x):  # estimates arccsc(x)
    if x == 0:  # will make 1/x undefined
        return None  # csc can't = 0 b/c 1/sin(x) can't = 0
    return arcsin(1 / x)


def arcsec(x):  # estimates arcsec(x), same concept as arccsc(x)
    if x == 0:
        return None
    return arccos(1 / x)


def deriv(f, x):  # takes the derivative of f at a certain point, x
    h = 1e-10
    top = f(x + h) - f(x)  # limit as h apporaches 0 of (f(x+h) - f(x))/h
    return top / h


def integral(f, a, b):  # takes the integral from a to b of f
    output = 0
    for n in range(1, 100001):  # uses the summation technique: f(x*) * dx
        output += f(a + ((n - (1 / 2)) * ((b - a) / 100001)))  # adding up all the f(x*)
    return output * ((b - a) / 100001)  # multiplying by delta x


def zeroes(f, x):  # guesses the roots of function f with an initial guess of x, using Newtonn-Raphson Method
    for i in range(1000):  # Newton proved that if you have an initial guess, x,
        new_x = x - f(x) / (deriv(f, x))  # x - f(x)/f'(x) is a closer guess to the root
        if new_x - x > 0 and new_x - x < 1.0e-10: break  # when the difference between the guess and the even closer guess
        if new_x - x < 0 and new_x - x > -1.0e-10: break  # is super small, we'll be satisfied with the current guess
        x = new_x
    return x

"""Test Case:
def f(x):
  return (x-3)**2

print(zeroes(f, 0.7))"""