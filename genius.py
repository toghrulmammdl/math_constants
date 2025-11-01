def pi():
    return chudnovsky_pi(4)

def tau():
    return 2 * pi()

def e():
    result_old = 0
    result = 1
    n = 1
    while abs(result - result_old) > 1e-20:
        result_old = result
        result += 1 / factorial(n)
        n += 1
    return result

def i():
    return complex(0, 1)

def reciprocal_fibonacci_constant():
    result = fibonacci(1)
    result_old = 0
    n=1
    while result-result_old>1e-20:
        if n>1:
            result_old = result
            result+=1/fibonacci(n)
        n+=1
    return result

def golden_ratio():
    return (1+(5**0.5)) / 2


# Helper functions:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def chudnovsky_pi(k):
    alpha = 12
    result = 0
    for n in range(0, k):
        result+= (-1)**n * factorial(6*n) * (13591409 + 545140134*n) / (factorial(3*n) * (factorial(n)**3) * (640320**(3*n + 1.5)))        
    return 1/(alpha * result)

def fibonacci(step):
    a, b = 0, 1
    for _ in range(step):
        a, b = b, a + b
    return a
