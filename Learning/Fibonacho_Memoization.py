fibonacci_cache = {}
def fibonacci(n):
    # cache the value first and then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the n term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 1010000):
    print(n, ": ", fibonacci(n))