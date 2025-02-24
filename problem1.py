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




#U: 
#Function will reverse a word thats the value of "theString".
#Method reverseThestring will have the value of the value of reverseThestring
#theString has the value of what we want to reverse.

#C:
#As we need to reverse a word, we will have to return s(the value of the parameteres, in this case, "Hello") but display it in reverse
#so we must yse [::-1]

#S:




    
