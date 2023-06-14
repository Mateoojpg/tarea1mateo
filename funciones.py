def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def lista_primos_menores(numero):
    primos_menores = []
    for i in range(2, numero):
        if es_primo(i):
            primos_menores.append(i)
    return primos_menores

numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

primos_menores = lista_primos_menores(numero)
print("Números primos menores:")
print(primos_menores)
