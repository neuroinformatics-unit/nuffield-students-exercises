# ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ 
# Tutorial 1: Introduction to Python
# ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ 


# ⁌------------------------------------⁍
# What you will learn:
# ✓ use the print() function
# ✓ use for loops
# ✓ define functions
# ✓ raise exceptions
# ✓ write a basic algorithm
# ⁌------------------------------------⁍


# ~~~~~~~~~~~
# Exercise 1.1
# Print the numbers from 1 to 100.
# Hint: Use a for loop.
print("\n ~~~~~~~~~~~")
print("Exercise 1.1")

# ..... your code here .....
for number in range(1, 101,):
     print(number)

# ~~~~~~~~~~~
# Exercise 1.2
# Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead.
# Hint: Use a for loop and the modulo operator %.
print("\n ~~~~~~~~~~~")
print("Exercise 1.2")

# ..... your code here .....
for number in range (1, 101):
    if number %3 ==0:
        print("Fizz")
    else:
        print(number)

# ~~~~~~~~~~~
# Exercise 1.3
# Print the numbers from 1 to 100, but if the number is divisible by 3, print "Fizz" instead, 
# and if the number is divisible by 5, print "Buzz" instead. If the number is divisible by both 3 and 5, print "FizzBuzz".
print("\n ~~~~~~~~~~~")
print("Exercise 1.3")

# ..... your code here .....
for number in range(1, 101):
        if number %3 == 0:
            print("Fizz")
        if number %5 == 0:
            print ("Buzz")
        if (number %5 == 0) and (number %3 == 0):
            print ("FizzBuzz")
else:
            print(number)
# ~~~~~~~~~~~
# Exercise 1.4
# Wrap the code from Exercise 1.3 in a function called fizzbuzz that takes a single argument n,
# and prints the numbers from 1 to n according to the rules of FizzBuzz.
# Hint: Use the function definition syntax `def function_name(argument):`
print("\n ~~~~~~~~~~~")
print("Exercise 1.4")

# ..... your code here .....

def FizzBuzz(n):
    for number in range (1, n+1):

        if (number %5 == 0) and (number %3 == 0):
            print ("FizzBuzz")
        elif number %3 == 0:
            print("Fizz")
        elif number %5 == 0:
            print ("Buzz")
    
    else:
        print(number)




# ~~~~~~~~~~~
# Exercise 1.5
# Super-Mario exercise! 🍄 
# See instructions at https://cs50.harvard.edu/x/2024/psets/1/mario/less/ (but do not use C, use Python instead).
print("\n ~~~~~~~~~~~")
print("Exercise 1.5")

def super_mario(h: int) -> None:
    """Prints a Mario-style pyramid of height h made of hashes (#).
    The height h must be an integer between 1 and 8, inclusive.
    If the height is invalid, the function will throw a message.

    Example:
    super_mario(5)
        #
       ##
      ###
     ####

    Parameters
    ----------
    h : int
        The height of the pyramid.
    
    Raises
    ------
    ValueError
        If the height is not between 1 and
    """
    # Part 1
    # ensure valid input; prompt user if h is <1 or >8
    # Hint: you can use an if statement and raise an exception if the condition is not met
    # Exception type: ValueError
        
    # ..... your code here .....
    print("Welcome to the Mario Pyramid Game!")
    print("What would you like the height of the pyramid to be?")
    if (h > 8) | (h < 1):
        raise ValueError("THE HEIGHT IS NOT BETWEEN 1 AND 8😡")
    else:
        for n_row in range (1, h+1):
            n_of_hash = n_row * 2 - 1
            n_spaces = h - n_row
            print(" " * n_spaces, end="")
            print("#" * n_of_hash)
        




    # Part 2
    # print the pyramid
    # Hint: use a for loop to iterate through the rows of the pyramid

    # ..... your code here .....

    
super_mario(5)


# ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~ ~〄~
# References
# FizzBuzz problem: https://www.codenewbie.org/blogs/how-to-solve-fizzbuzz
# Python exceptions: https://docs.python.org/3/tutorial/errors.html
