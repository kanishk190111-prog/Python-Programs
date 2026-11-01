guess = input("At n = 1000, O(n^2) takes how many steps? ")

input("Watch O(n) and O(n^2) grow, Press Enter ")
for n in [10, 100, 1000]:
    input(f"n = {n}, Press Enter ")
    print(f"O(n) = {n}, O(n^2) = {n**2}")

print("your guess?", guess)
input("Full ladder at n = 1000. Press Enter ")
print("O(1)=1 O(log n)=10 O(n)=1000 O(n^2)=1,000,000")