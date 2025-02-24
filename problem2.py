def factorial (n):
    #Edge cases - number is negative
    if n < 0:
        return "Not defined for negative numbers"
    #one and zero have 1 as facotrial
    elif n == 0 or n == 1
        return 1
    else:
        result = 1
        #start from 2 because we already did cases for 0 and 1
        for i in range(2, n+1):
            result *= i
        return result

print(factorial(4))  # Output: 24
