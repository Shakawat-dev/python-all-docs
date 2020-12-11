# n! = 1 * 2 * 3 * 4 * 5......n
# n! = [1 * 2 * 3 * 4 * 5......n-1] * n
# n! = (n-1) * (n-2) * (n-3).....n * (n-1)!

# normal factorial  
def factorial_iter(n):
    num = 1
    for i in range(n):
        num *= (i + 1)
    return num
print(factorial_iter(5))


# factorial recursion 
def factorial_recursion(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursion(n - 1)
print(factorial_recursion(5))
