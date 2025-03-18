# Fibonacci sequence using recursion

def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generate_fibonacci_sequence(terms):
    if terms <= 0:
        return "Number of terms must be positive."
    sequence = [fibonacci(i) for i in range(1, terms + 1)]
    return sequence


terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:", generate_fibonacci_sequence(terms))
