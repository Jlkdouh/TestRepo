def Factorial(numero):

    if (numero < 1) or (type(numero) != int):
        return None
    factorial = 1
    for i in range(numero):
        factorial *= (i+1)

    return factorial


