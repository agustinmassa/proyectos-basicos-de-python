import random
import time

def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return 'No esta en la lista'

# Cuando la lista tenga miles o millenos de numeros esta busqueda va a ser muy lenta
# Por este motivo hacemos la busqueda binaria
# Lo unico que para que funcione la lista tiene que estar ordenada de forma ascendente
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0                     # Es el primer indice

    if limite_superior is None:
        limite_superior = len(lista)-1          # Es el ultimo indice
    
    if limite_superior < limite_inferior:
        return 'No estas definiendo bien los limites'
    
    punto_medio = ((limite_inferior + limite_superior) // 2)  # // Va a dividir y como resultado tira el valor entero
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif lista[punto_medio] < objetivo:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)
    else:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)


# Ahora vamos a comprar cuanto tardan las dos busquedas
# Creamos unas lista ordenada de 5000 elementos

tamaño = 5000
conjunto=set()

while len(conjunto) < tamaño:
    conjunto.add(random.randint(-3*tamaño, +3*tamaño))

lista_ordenada = sorted(list(conjunto))  

# Medimos el tiempo de busqueda ingenua

inicio= time.time()
for objetivo in lista_ordenada:
    busqueda_ingenua(lista_ordenada, objetivo)
fin= time.time()
print(f'El tiempo de busqueda ingenua es: {fin - inicio} segundos.')

# Medimos el tiempo de busqueda binaria
inicio= time.time()
for objetivo in lista_ordenada:
    busqueda_binaria(lista_ordenada, objetivo)
fin= time.time()
print(f'El tiempo de busqueda binaria es: {fin - inicio} segundos.')

