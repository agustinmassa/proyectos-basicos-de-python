import random


def adivina_el_numero(x):

    print('====================')
    print('Bienvenido al juego!')
    print('====================')
    print('El objetivo ed adivinar le numero generado por la computadora')

    numero_aleatorio=random.randint(1,x) #Numero aleatorio entre 1 y x

    prediccion= 0

    while prediccion != numero_aleatorio:
        prediccion=int(input(f'Adivine el numero entre 1 y {x}: '))

        if prediccion < numero_aleatorio:
            print('Intenta nuevamente, este numero es menor que el numero aleatorio')
        elif prediccion > numero_aleatorio:
            print('Intente nuevamente, este numero es mayor que el numero aleatorio')
    print(f'Felicitaciones el numero aleatorio era {numero_aleatorio}')

adivina_el_numero(10)



