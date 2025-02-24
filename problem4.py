# U: Understand
# Task: Implement FizzBuzz based on divisibility rules.
# Input: An integer n (e.g., 5)
# Output: A list of strings foloowing FizzBuzz rules.

# C: Clues
# - Use a loop from 1 to n
# - Check divisinility by 3, 4, or both

# A: Assemble
def fizz_buzz(n):
  result = []
  for i in range(1, n + 1):
      if i % 3== 0 and i % 5 ==0:
         result.append("FizzBuzz")
      elif i % 3 ==0:
         result.append("Fizz")
      elif i % 5 ==0:
         result.append("Buzz")
      else:
         result.append(str(i))
  return result
# S: Solve
# Test cases
print (fizz_buzz(5)) # Expected: ["1", "2", "Fizz", "4", "Buzz"]
print (fizz_buzz(15)) # Expected: ["1", "2", "Fizz", "4", "Buzz", ..., "FizzBuzz"]

# E: Examine
# The function is efficient (O(n) time complexity) and follows the problem requirements
