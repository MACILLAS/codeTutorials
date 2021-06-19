'''
Let's Learn About Logic!
-------------------------

Computers work by processing a series of 0s and 1s...
This is analogous to OFF and ON, respectively; or False and True.
Where False is 0 and True is 1. (A variable that stores either True or False state is called a Boolean variable)

Computers, at its core (lowest level), is just a machine that compares Boolean variables!

Analogous to Logic Gates (another topic for another time) the computer can perform a few different checks...

AND, OR and NOT

Follow the examples below! Put your code in the specified sections. To complete this unit, run this script without any assertion errors.
'''

# Example 1 (AND)
print("EXAMPLE 1: ")
'''
Consider a black box with two inputs and one output. (All boolean)
Only when both inputs are True will the output be True. 
Any other combination will result in False.
'''
A = True
B = False
C = True

output = A and C
print("A AND C : ", output)

output = A and B
print("A and B : ", output)

# Now you try!
# Use the 'and' function to construct a True output and a False output
# Assign True output to output_True and False output to output_False
output_True = None
output_False = None
A = False
B = True
C = False
### YOUR CODE HERE ###


######################
assert output_True is True
assert output_False is False

# Example 2 (OR)
print("EXAMPLE 2: ")
'''
OR statements are similar to AND except it is True when either inputs are True.
ie. True or False = True , True and True = True , False and False = False
'''
A = True
B = False
C = True

output = A or B
print("A OR B : ", output)
output = A or C
print("A OR C : ", output)

# Now you try!
# Use variable A, B and C craft a False statement
output_False = None
A = True
B = False
C = True
### YOUR CODE HERE ###

######################
assert output_False is False

# Example 3 (NOT)
print("EXAMPLE 3: ")

'''
NOT gives the opposite of a boolean.
ie NOT True is False and NOT False is True
'''
A = True
B = False
C = True

output = not A
print("NOT A : ", output)
# NOT is often represented by ! in code
output = not B
print("NOT B : ", output)

# Now you try!
# Use only variable D to craft a True and False statement
output_True = None
output_False = None
D = True
### YOUR CODE HERE ###


######################
assert output_False is False
assert output_True

# Example 4 (Multiple Logicals)
print("EXAMPLE 4: ")

'''
Great! We now know how to use AND, OR and NOT. 
However we've only use these to compare 2 boolean variables, what if we need compare multiple together?
'''
A = True
B = False
output = A and B or not B
print("A AND B OR NOT B :", output)
# Let's break this down...
# A AND B is False. NOT B is True. Such that False or True is True!
# Alternatively, not B is True. B or True is True. A and True is True.
# You can see logical statements are associative!

# Your turn!
# Modify output such that output is True
A = True
B = False
output = A and not not B or A and B
### YOUR CODE HERE ###

######################
assert output

'''
IF, ELIF, ELSE
Now that we have mastered logicals we can tell the computer to use these values to tell the computer what to do!
To do this we will utilize the IF statement. 
The simplest implementation of IF statements are like this...

IF condition is True :
    action 

'''

# Example 5 (IF)
print("EXAMPLE 5: ")

A = True
B = False

if A:
    print("A is True")

# Example 6 (IF ELSE)
print("EXAMPLE 6: ")
'''
Suppose we wanted to to print("A is True") when A is True and print("A is not True") if A is False...
We could do the following...
'''

if A:
    print("A is True")

if not A:
    print("A is not True")

'''
But this is too cumbersome. Since A can only be either True or False we can confidently employ a Else statement. 
'''
if A:
    print("A is True")
else:
    print("A is not True")

# Now you try!
'''
Let's make a XNOR eXclusive Not OR gate! 

Given inputs A and B, the XNOR gate returns TRUE when A and B are the same. 
Write a function using an IF - ELSE statement 
'''


def XNOR(A, B):
    output = None
    ### YOUR CODE HERE ###
    # check if A and B are the same... Use the == comparison (ie A == B) output = True
    # else output = False

    ######################
    return output


assert XNOR(A=True, B=True) and XNOR(A=False, B=False) and not XNOR(A=True, B=False)

# Example 7 (IF, ELIF, ELSE)
print("EXAMPLE 7: ")
'''
Lastly, we will introduce the ELIF or else-if

Consider A and B are some integer between 1, 2 or 3. And you want to output something about the relationship between A and B...
'''
A = 3
B = 1

if A == B:
    print("A is equal to B")
else:
    if A > B:
        print("A is greater than B")
    else:
        print("B is greater than A")

'''
We can write the previous using elif...
'''
if A > B:
    print("A is greater than B")
elif A < B:
    print("A is less than B")
else:
    print("A is equal to B")

# Now You Try!
'''
Using the tools we have learned we can make more complicated logical structures.

For example we can construct an XOR or eXclusive OR

An XOR functions like an OR except the case TRUE xor TRUE will result in FALSE
'''


def XOR(A, B):
    output = None
    ### YOUR CODE HERE ###
    # check if both A and B are True
    # check if both A and B are False
    # else A and B are different

    ######################
    return output


assert XOR(A=True, B=True) is False and XOR(A=False, B=True)

# BONUS
''' 
Can we rewrite XNOR using our XOR function?
'''

'''
def XNOR (A, B):

'''