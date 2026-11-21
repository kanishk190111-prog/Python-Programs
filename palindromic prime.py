def sieve(n):
    """Return (list of all primes from 2 to n, number of crossings) for
    n of 2 or more."""
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    crossings = 0
    prime = 2
    while prime * prime <= n:
        if is_prime[prime]:
            for multiple in range(prime * prime, n + 1, prime):
                is_prime[multiple] = False
                crossings = crossings + 1
        prime = prime + 1
    primes = []
    for k in range(2, n + 1):
        if is_prime[k]:
            primes.append(k)
    return primes, crossings


def reverse_number(n):
    """Reverse the digits of n with % 10 and // 10. Returns (reversed
    number, digit steps)."""
    rev, steps = 0, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
        steps = steps + 1
    return rev, steps


print("Primes up to 30:", sieve(30)[0])
print()
print("        n   primes   crossings   crossings per number")
for n in [10 ** 4, 10 ** 5, 10 ** 6]:
    primes, crossings = sieve(n)
    print(f"{n:>9} {len(primes):>8} {crossings:>11} {crossings / n:>22.3f}")
print()

limit = 3000
text = input("Find the palindromic primes up to (type 3000): ").strip()
if text.isdecimal() and len(text) <= 6 and int(text) >= 2:
    limit = int(text)
primes, steps = sieve(limit)
palindromes = []
for prime in primes:
    rev, digit_steps = reverse_number(prime)
    steps = steps + digit_steps
    if rev == prime:
        palindromes.append(prime)
print("Palindromic primes up to", limit, ":", palindromes)
print("How many:", len(palindromes), " Steps (crossings + digit steps):", steps)
print("Brute force would divide every number by 1..num:", limit * (limit + 1) // 2, "divisions")