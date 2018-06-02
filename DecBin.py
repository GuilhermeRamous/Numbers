def decBin(dec):
    binary = ""

    while dec //  2 >= 0 and dec != 0:
        binary = str(dec % 2) + binary
        dec //= 2 

    return binary


decimalNumber = int(input("Type a decimal number: "))
print(decimalNumber, "binary representation:", decBin(decimalNumber))


