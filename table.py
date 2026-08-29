num=int(input("enter your number:"))
for i in range(1,11):
    print(num, "x", i ,"=", num*i)

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):

    for j in range(i):

        print('*', end='')

    print()

    total_sum = 0
    num = 1

    while num <= 10:
        total_sum +=num
        num += 1

        print(f"the sum of the first ten natural numbers is {total_sum}")