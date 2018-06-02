def factorial(n):
    resultado = 1

    for i in range(n, 0, -1):
        resultado *= i

    return resultado


number = int(input("Type a number: "))
print(str(number) + "! = " +  str(factorial(number)))
