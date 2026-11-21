def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

bus_a = int(input("Enter interval for Bus A (in minutes): "))
bus_b = int(input("Enter interval for Bus B (in minutes): "))
count = int(input("How many shared departure times do you want to list? "))

lcm = find_lcm(bus_a, bus_b)
print(f"\nThe buses leave together every {lcm} minutes.")

print("Next shared departure times (in minutes):")
for i in range(1, count + 1):
    print(f"{i}. {lcm * i} minutes")