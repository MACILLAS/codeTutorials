"""
A software package will usually have a main.py...

In main.py are the highest level code (More English Like), which uses lower level code (More Like Computers :P), usually written elsewhere.
This hierarchy of code languages is called 'abstraction'. Essentially, the higher the abstraction the easier it is to
get stuff done but we also more heavily depend on other people's code. As a rule of thumb don't reinvent the wheel.

BUT reinventing the wheel is a pretty good way to learn the fundamentals of code, so that's exactly what we will do!

First some fundamentals! Continue from if __name__ == "__main__":
"""

'''
if __name__ == "__main__":

From our logic lesson we can identify this is an if statement that is comparing the variable __name__ and the string "__main__"...

Underscores "__" in Python indicate a protected private variables. Here __name__ in an indicator of where the script is called from.
Because we will use this script to run other scripts the __name__ will be __main__.

This allows us to control what happens when another program runs this code vs when we run this code. 
Ultimately this is very useful when developing software as we can test the file individually before sending it off. 

'''
if __name__ == "__main__":
    """
    * How do we use other people's code? >> IMPORTS

    Let's say I wanted to add 2 numbers A and B... 
    And I want to use the sum() function I wrote in ./test_dir/test_test_dir/add.py

    (Take a second to locate add.py in ./oop/test_dir/test_test_dir/add.py)

    Well first need to import the program add.py
    """
    print("EXAMPLE 1:")
    # import add from its directory (notice the import is relative to the current location of this file, main.py)
    from test_dir.test_test_dir import add
    A = 1
    B = 2

    output = add.sum(A, B)
    # This is a notation called f-string.
    print(f"A + B is: {output}")

    # OKAY NOW YOU TRY!!!
    '''
    Create a file in ./test_dir called math.py
    Write a function called multiply(A, B) that takes in values. Use add.py as a template. 
    import math.py and use the multiply function to multiply A and B. 
    '''
    output = None
    ### YOUR CODE HERE ###

    print(f"A * B is: {output}")
    ######################
    #assert output == A * B

    """
    Now for something a little different... 
    """
    print("EXAMPLE 2")