from math import sqrt


def ishappy(n):
    cache = []
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in cache:
            return False
        cache.append(n)
    return True


def isprime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True


happies = []
happy_primes = []

for i in range(1, 1001):
    if ishappy(i): happies.append(i)

for i in happies:
    if isprime(i):
        happy_primes.append(i)

print("Happy numbers:")
for i in range(0, 8):
    print(happies[i])
# print()
# print("Happy primes:")
# print(happy_primes)
