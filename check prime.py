def is_prime(n):
    """Return (True or False, number of checks) using trial division up to sqrt(n)."""
    checks = 0
    if n < 2:
        return False, checks
    i = 2
    while i * i <= n:
        checks = checks + 1
        if n % i == 0:
            return False, checks
        i = i + 1
    return True, checks

def brute_force_checks(n):
    """Brute force, for comparison only: try every i from 2 to n - 1."""
    checks = 0
    for i in range(2, n):
        checks = checks + 1
        if n % i == 0:
            break
    return checks

text = input("Type a whole number to test: ").strip()
if text.isdecimal() and len(text) <= 13 and int(text) <= 10 ** 12:
    prime, checks = is_prime(int(text))
    if prime:
        print(text, "is a prime number (", checks, "checks )")
    else:
        print(text, "is not a prime number (", checks, "checks )")
else:
    print("Please type a whole number from 0 to 1000000000000, for example 97.")
print()
print("      n prime? checks up to sqrt(n)  checks brute force")
for n in [1, 2, 9, 97, 100, 7919, 1000003]:
    prime, checks = is_prime(n)
    print(f"{n:>9} {str(prime):<6} {checks:>20} {brute_force_checks(n):>18}")