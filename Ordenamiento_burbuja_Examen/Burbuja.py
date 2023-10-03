def bubb_Recur(lista, n):  # Definir función recursiva
    if n <= 1:  # Caso base: si la longitud de la lista es 1 o menos, no hay nada que ordenar
        return

    for i in range(n - 1):  # Bucle para revisar la lista
        if lista[i] > lista[i + 1]:  # Compara elementos en la lista
            lista[i], lista[i + 1] = lista[i + 1], lista[i]  # Intercambia elementos si están en el orden incorrecto

    bubb_Recur(lista, n - 1)  # Llama de manera recursiva a la función

def bubb_Iterat(lista):  # Define una función iterativa
    n = len(lista)  # Obtiene la longitud de la lista

    for i in range(n):  # Bucle externo para revisar la lista
        Swap = False  # Verifica si se realizan intercambios en esta pasada

        for j in range(0, n - i - 1):  # Bucle para comparar elementos y realizar intercambios
            if lista[j] > lista[j + 1]:  # Compara elementos en lista
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambia elementos si están en posicion incorrecta
                Swap = True  # Marca que se ha realizado un intercambio en esta pasada

        if not Swap:  # Si no se ha realizado ningún intercambio en esta pasada, la lista está ordenada
            break  # Sale del bucle externo

# Pedir al usuario el tamaño de la lista y los elementos
n = int(input("Ingrese el tamaño de la lista: "))  # Solicita al usuario el tamaño de la lista
lista = []  # Crea una lista vacía
for i in range(n):  # Bucle para pedir elementos uno por uno
    fact= int(input(f"Ingrese el elemento {i + 1}: "))  # Solicita al usuario ingresar un elemento
    lista.append(fact)  # Guarda elemento en la lista

lista_2 = lista[:]  # Crea una copia de la lista original

print("Lista original:", lista)  # Imprime la lista original ingresada por el usuario

bubb_Recur(lista, n)  # Llama a la función de ordenamiento recursivo para ordenar la lista
print("Lista ordenada (recursiva):", lista)  # Imprime la lista ordenada utilizando el algoritmo recursivo

bubb_Iterat(lista_2)  # Llama a la función de ordenamiento iterativo para ordenar la copia de la lista
print("Lista ordenada (iterativa):", lista_2)  # Imprime la lista ordenada utilizando el algoritmo iterativo

