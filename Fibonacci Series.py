def print_fibonacci(n):
    a, b = 0, 1

    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to 1 term:")
        print(a)
    else:
        print(f"Fibonacci sequence up to {n} terms:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print() 

try:
    terms = int(input("Enter the number of terms: "))
    print_fibonacci(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")