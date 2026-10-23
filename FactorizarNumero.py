def es_primo(n):

    mul_resto =1
    for i in range (2,n) :   # contamos desde 2 hasta n-1
        mul_resto *= n%i    # multiplicamos todos los restos

    if mul_resto == 0:  # si alguno de los restos es cero
        return False
    else :
        return True


def lista_primos (primos_hasta) :
# genera una lista con los primos hasta el argumento de entrada
    lista_primos = []
    for j in range (2,primos_hasta) :
        if es_primo(j) == True :
            lista_primos.append(j)
    return(lista_primos)


def FactorizarNumero(numero):
    if (type(numero)!= int or numero<=0 or es_primo(numero)==True):

        return None

    print("el numero no es primo")
    #  puedo recortar la lista de factores primos hasta 50 sin problemas
    #  primos_subn = lista_primos(n//2) esta seria la opcion inicial
    #  pero para la mayoria de los numeros no es necesario
    primos_subn = lista_primos(50)

    exp = 1
    i = 0
    div = numero
    fact_exp = {} # el diccionario me permite modificar en el loop el valor
    #                   del exponente solamente

    while div/primos_subn[i] != 1: # si no termine de dividir

        if div%primos_subn[i] != 0 : # si no es divisible por este factor
            exp = 1
            i +=1
        else :
    #  si es divisible por este factor incluyo en el diccionario el
            fact_exp[primos_subn[i]] = exp  # par factor:exponente
    # por mas que se modifique el exponente el factor no cambia
            exp += 1
            div = div//primos_subn[i]
    else:
        fact_exp[primos_subn[i]] = exp
        lista = []
        for key in fact_exp:
            lista_i =[key,fact_exp[key]]
            lista.append(lista_i)

    return lista




