import random

def jugar():
    usuario=input('Escoge una opcion: "pi" para peidra, "pa" para papel y "ti" para tijera \n').lower()
    computadora=random.choice(['pi','pa','ti'])

    if usuario == computadora:
        return 'Empataron, intenta de nuevo'
    
    if gano_el_jugador(usuario,computadora):
        return 'Esoo ganasteee'
    else:
        return f'Oh perdiste, la computadora eligio {computadora}'
    

def gano_el_jugador(jugador,oponente):
    if ((jugador == 'pi' and oponente == 'ti') or (jugador == 'pa' and oponente == 'pi') or (jugador == 'ti'and oponente == 'pa')):
        return True
    else: 
        return 

print(jugar())