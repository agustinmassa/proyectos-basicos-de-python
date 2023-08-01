import random


def adivina_el_numero_computadora(x):

    print('===================')
    print('Bienvenido al juego')
    print('===================')
    print(f'Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo')

    limites_inferior = 1
    limites_superior = x

    respuesta= ''
    while respuesta != 'c':
        #Prediccion
        if limites_inferior != limites_superior:
            prediccion=random.randint(limites_inferior,limites_superior)
        else:
            prediccion= limites_superior #tambien al limite inferior
        
        #Respuesta
        respuesta=input(f'Mi prediccion es {prediccion}. Si es alta, ingresa (A). Si es baja ingresa (B). Si es correcta, ingresa (C):').lower()

        if respuesta == 'a':
            limites_superior= prediccion - 1
        elif respuesta == 'b':
            limites_inferior= prediccion + 1

    print(f'Esooo, la computadora adivino tu numero correctamente: {prediccion} ') 

adivina_el_numero_computadora(10)


        

