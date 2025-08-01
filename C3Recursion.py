def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

"""
This function calculates the factorial of a number.

If the number is 1, it just returns 1. That’s the base case, where it stops.

Otherwise, it says:
“I’ll multiply this number x by the factorial of one number less (x - 1)… but I’ll let the function itself figure that out.”

It keeps calling itself with smaller and smaller numbers until it finally hits 1, then it starts returning the results back up.

Recursion is when a function solves a problem by calling itself.

Each call is like a new “instance” of the same function, solving a smaller piece of the problem.

This keeps happening until the function reaches a base case, a simple condition where it stops calling itself.
Each function call waits for the one after it to finish, holding its place in memory. 
That’s why the stack grows bigger until the base case is reached, and then shrinks as the answers return."""