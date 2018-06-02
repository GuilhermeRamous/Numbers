def gcd(n1, n2):
    if n1 == 0 and n2 == 0:
        return "undefined"
    elif n1 == 0 or n2 == 0:
        if n1 == 0:
            return n2
        else:
            return n1
    elif n1 == n2:
        return n1
    else:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1

        return gcd(n1, n2)


num1 = int(input("Type a number: "))
num2 = int(input("Type another number: "))
print()
print(gcd(num1, num2))
