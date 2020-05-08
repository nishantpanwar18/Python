import time
import math
def is_prime(n):
    """Returns True if 'n' is a prime number, False otherwise. """
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor+1, 2):
        if n % d == 0:
            return False
    return True


t0 = time.time()
for n in range(1, 1000001):
    is_prime(n)
t1 = time.time()

print("Time elapsed: ", t1 - t0)

