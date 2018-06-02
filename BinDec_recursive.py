def binDec(binary):
    binary_string = str(binary)

    if len(binary_string) == 1:
        return int(binary_string)
    else:
       return int(binary_string[0]) * 2 ** (len(binary_string) - 1) + binDec(int(binary_string[1:]))


binaryNumber = int(input("Binary number: "))
print(binaryNumber, "decimal representation:", binDec(binaryNumber))

