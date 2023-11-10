#Mochila fraccionaria

import random
import time
import matplotlib.pyplot as plt

def mochila_fraccionaria(capacidad, objetos):
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        else:
            frac = capacidad / peso
            mochila.append((valor * frac, peso * frac))
            total_objetos += valor * frac
            break
    return total_objetos, mochila

def generar_objetos_y_capacidad(n):
    objetos = [(random.randint(1, 10), random.randint(1, 20)) for _ in range(n)]
    capacidad = random.randint(20, 50)
    return capacidad, objetos

def graficar_tiempos(tiempo_ejecucion):
    plt.plot(range(1, len(tiempo_ejecucion) + 1), tiempo_ejecucion, marker='o')
    plt.xlabel('Iteración')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempos de ejecución de las iteraciones')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    tiempo_ejecucion = []  # Lista para almacenar los tiempos de ejecución

    for i in range(10):
        capacidad, objetos = generar_objetos_y_capacidad(4)

        start_time = time.time()
        total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
        
        print()
        print(f'{i + 1}: El total de objetos es {total_objetos} y la mochila quedó {mochila}')
        end_time = time.time()

        execution_time = end_time - start_time
        tiempo_ejecucion.append(execution_time)  # Agregar el tiempo a la lista
        print(f'Tiempo de ejecución: {execution_time} segundos')
        print()

    graficar_tiempos(tiempo_ejecucion)  # Llama a la función para graficar los tiempos