import math

def largest_prime_factor(n):

    # while n is even, right shift by 2
    while n % 2 == 0:
        max_prime = 2
        n = n // 2

    # divide by the prime factors you encounter
    # because, i is not prime, it is the product of primes that are smaller than it
    # but we already divided by the primes that were smaller 
    i = 3
    while i <= math.sqrt(n):
        while n % i == 0:
            max_prime = i
            n = n // i
        i += 2

    if n > 2:
        max_prime = n

    return max_prime

print(largest_prime_factor(119))

