def binDec(binary):
    binaryString = str(binary)
    decimal = 0

    for i in range(len(binaryString)):
        decimal += int(binaryString[-(i + 1)]) * 2 ** i

    return decimal


binaryNumber = int(input("Type a binary number: "))
print(binaryNumber, "decimal representation:", binDec(binaryNumber))

