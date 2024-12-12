# Definimos sumar_lista:
def sumar_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
# Definimos la lista de números y le decimos que separe por comas el input de la lista:
lista_de_numeros_str = input("Inserte una lista de números separados por comas: ")
lista_de_numeros = [int(x) for x in lista_de_numeros_str.split(",")]
# Imprimimos el resultado de la suma:
resultado = sumar_lista(lista_de_numeros)
print("La suma de la lista es:", resultado)