scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]
#          1  2  3  4  5  6  7  8  9

input("List: " + str(scores) + " n = 9 Linear search - checks left to right. Press Enter     ")

target = int(input("Enter a number to search for: "))

input("Searching for " + str(target) + ". Press Enter to run ")
steps = 0
for score in scores:
    steps += 1
    if score == target:
        break
print(" target =", target, " found at position", steps, "checks =", steps)
input("Double Loop: checks every pair. Press Enter to run ")

steps = 0

for i in range(n):

    for j in range(n):

        steps += 1

print(" steps =", steps, " your guess:", guess, " -> O(n^2) quadratic time")

input("Two more notations. Press Enter ")

print(" Big Omega Ω -> best case lower bound")

print(" Big Theta Θ -> exact bound (worst = best)")