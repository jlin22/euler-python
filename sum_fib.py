import math

def sum_fib(n):
    ''' find the sum of all of the even fibonacci numbers under n, starting
    with 1 and 2 '''
    back_two = 1
    back_one = 2
    total = 2
    while back_one < n:
        next_fib = back_two + back_one
        if next_fib % 2 == 0: total += next_fib
        back_two = back_one
        back_one = next_fib
    return total

def sum_fib2(n):
    ''' find the sum of even fibonacci numbers under n 
    let's use binet's formula
    Fn = 1/(sqrt(5)) ( ((1 + sqrt(5)) / 2)^n - ((1 - sqrt(5)) / 2) ^ n )
    we can show that the only even fibonacci numbers are of form 3k, k>=1'''

    # let's keep the first part and second part of Fn separate
    F_left = ((1 + math.sqrt(5)) / 2) ** 3 / math.sqrt(5)
    F_right = ((1 - math.sqrt(5)) / 2) ** 3 / math.sqrt(5)

    fib_scalar_left = ((1 + math.sqrt(5)) / 2) ** 3 
    fib_scalar_right = ((1 - math.sqrt(5)) / 2) ** 3 

    F_current = F_left - F_right
    
    total = 0

    while F_current < n:
        total += F_current
        F_left *= fib_scalar_left
        F_right *= fib_scalar_right
        F_current = F_left - F_right

    return int(total)

def sum_fib3(n):
    ''' cache the values, only add every 3rd one '''
    fib_cache = [0, 1, 1]
    i = 2
    total = 0
    while fib_cache[i] < n:
        if i % 3 == 0:
            total += fib_cache[i]
        fib_cache.append(fib_cache[i - 1] + fib_cache[i])
        i += 1
    return total


print(sum_fib(35))
print(sum_fib2(35))
print(sum_fib3(35))
        
