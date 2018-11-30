def sum35(n):
    ''' find the sum of all of the multiples of 3 and 5 under n
    costs: O(n)'''
    count = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count

# is there a faster way?
''' Maybe you can factor and use the sum of integers equation '''
def sum35_v2(n):
    sum_of_multiples = {}
    for multiple in [3, 5, 15]:
        upper_bound = n // multiple
        sum_of_multiples[multiple] = multiple * (upper_bound * (upper_bound + 1) // 2)
    return sum_of_multiples[3] + sum_of_multiples[5] - sum_of_multiples[15]


    
''' Now the question is, which one is faster? 
    1st one: O(n)
    2nd one: 
    Need to answer: How long does integer division take?
    If Python uses repeated subtraction, it would take O(n), or precisely n // d time
    That's for bound
    Multiplication takes O(n^2) or O(n^(log_3_(2)) if the number is big enough
    So the second algorithm is O(n ** 2), which is worse
    '''



print(sum35(15))
print(sum35(1000))
print(sum35_v2(15))
        
