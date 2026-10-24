"""โปรแกรม FibonacciRecursionV1"""

def fib(num, a=0, b=1):
    """Calculate the Fibonacci number."""
    if not num:
        return a
    return fib(num - 1, b, a + b)


n = int(input())
print(fib(n))
