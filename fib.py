def fib(numberOfElements):
    n1 = 1
    n2 = 1
    lis = [n1, n2]

    for i in range(numberOfElements - 2):
        n1 += n2
        n2 = (n1 - n2)
        lis.append(n1)

    return lis


numberOfElements = int(input("Type the number of elements of your fibonacci sequence: "))

for i in fib(numberOfElements):
    print(i, end=" ")

print()


