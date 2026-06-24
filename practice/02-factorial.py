# Definition:
#   factorial(n) = n * factorial(n - 1)
#
# Example:
#   factorial(5) = 5 * factorial(4)
#                = 5 * 4 * factorial(3)
#                = 5 * 4 * 3 * factorial(2)
#                = 5 * 4 * 3 * 2 * factorial(1)
#                = 5 * 4 * 3 * 2 * 1 * factorial(0)
#                = 5 * 4 * 3 * 2 * 1 * 1
#                = 120
def factorial(n):
    if n < 0:
        raise Exception("Enter number n >= 0 when calling factorial(n)")
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact = i * fact
    return fact


for i in range(11):
    print(f"factorial({i}) = {factorial(i)}")

print("---")

# Test error case - try uncommenting this
factorial(-1)
