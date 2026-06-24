# Given n, returns fibonacci(n) based on the following definition:
#   fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
#
# Example:
#   fibonacci(0) = 0
#   fibonacci(1) = 1
#   fibonacci(2) = fibonacci(1) + fibonacci(0) => 0 + 1 = 1
#   fibonacci(3) = fibonacci(2) + fibonacci(1) => 1 + 1 = 2
#   fibonacci(4) = fibonacci(3) + fibonacci(2) => 2 + 1 = 3
#   fibonacci(5) = fibonacci(4) + fibonacci(3) => 3 + 2 = 5
def fibonacci(n):
    # Error case
    if n < 0:
        raise Exception("Enter a number n >= 0 when calling fibonacci(n)")
    a = 0
    b = 1
    for _ in range(n):
        fib = a + b
        a = b
        b = fib
    return a


# Given n, prints the first n numbers in the fibonacci sequence
def print_fibonacci(n):
    # Error case
    if n < 0:
        raise Exception("Enter a number n >= 0 when calling fibonacci(n)")
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=" ")
        fib = a + b
        a = b
        b = fib


for i in range(0, 10):
    print(f"fibonacci({i}) = {fibonacci(i)}")

print("---")

print_fibonacci(10)

print("\n---")

# Test error case - run after uncommenting this
print_fibonacci(-1)
