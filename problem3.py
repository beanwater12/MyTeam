# 0 is even
# 1 is odd
# string input return error
# negative number return true


def is_even(num):
    return num%2 == 0 # return if the number is even (true) or odd (false)

print(is_even(4)) # True
print(is_even(5)) # False
print(is_even(-4)) # True
print(is_even(0)) # True
print(is_even("hello")) # Error
