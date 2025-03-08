# recursion concept in fibonacci sequence
#Recursion in Python
"""
Recursion is a programming technique where a function calls itself to solve a problem. Each recursive call breaks the problem into smaller subproblems, eventually reaching a base case where recursion stops.

Key Components of Recursion
Base Case: A condition where the function stops calling itself.
Recursive Case: A case where the function calls itself with a smaller problem.
"""

def fibonacci(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

n = 12
print("The fibonacci sequence is : \n", fibonacci(n))
     
"""
Importance of Base Case in Recursion
The base case is crucial in recursion because it terminates the recursive function. Without a base case, the function would keep calling itself indefinitely, leading to a stack overflow error.

Why is the Base Case Important?
Prevents Infinite Recursion: Without a base case, the function will never stop calling itself.
Reduces Computation Overhead: The base case stops unnecessary calculations, making recursion more efficient.
Ensures Correct Output: The function must eventually return a definite value; otherwise, it will keep running indefinitely.
"""

# factorial of a number using recursion

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1) # recursive case

n = 7
print("The factorial of a number is : \n", factorial(n))
    
    