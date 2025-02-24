#File 1 (problem1.py): Write a function to reverse a string.

#Example:
#Input: "Hello"
#Output: "olleH"

def stringInReverse(s):
    return s[::-1]
    #function will display the word in "theString" in reverse.

theString = "Hello"
#declares "Hello" as the string we want to reverse.

reverseThestring = stringInReverse(theString)
#when we call "reverseThestring" the "stringInReverse" function should run, and 
#reverse the value of "theString" which is "Hello"

print(reverseThestring);
#Should print "olleH"




Understand

Summarize the problem in your own words.
Identify inputs and outputs.
Determine if input validation is needed (edge cases).
Ask clarifying questions.
Clues

Look for patterns, hints, or types of problems that indicate which coding tools to use.
Assemble

Write pseudocode.
Break down the problem into smaller steps.
Outline the steps needed to solve the question.
Solve

Translate pseudocode into actual code.
Implement the solution.
Test it out with sample inputs.
Examine

Check the results.
Ensure the solution is understandable at a glance.
Consider if you can improve the performance of the solution.
