import random
import sys
import os
import time

############----------############
#          By: LexaHck           #
#    https://github.com/LexaHck  #
#                                #
#     From the dark side...      #
#             -2023-             #
############----------############

os.system("clear")

def juego():
    opciones= ['Piedra', 'Papel', 'Tijera']

    for i in range(1):
        jugador = input("Piedra, papel o tijera?: ")
        jugador = jugador.capitalize()
        pc = random.choice(opciones)
    
        if jugador == pc:
            print(f"\nPC: {pc}! \n\nEmpate! Empieza de nuevo")
        elif jugador == 'Piedra' and pc == "Tijera":
            print(f"\nPC: {pc}! \n\nGenial, Ganaste!")
        elif jugador == 'Papel' and pc == 'Piedra':
            print(f"\nPC: {pc}! \n\nGenial, Ganaste!")
        elif jugador == 'Tijera' and pc == 'Papel':
            print(f"\nPC: {pc}! \n\nGenial, Ganaste!")
        elif pc == 'Piedra' and jugador == "Tijera":
            print(f"\nPC: {pc}! \n\nPerdiste, vuelve a intentarlo...")
        elif pc == 'Papel' and jugador == 'Piedra':
            print(f"\nPC: {pc}! \n\nPerdiste, vuelve a intentarlo...")
        elif pc == 'Tijera' and jugador == 'Papel':
            print(f"\nPC: {pc}! \n\nPerdiste, vuelve a intentarlo...")
        elif jugador == 'Salir':
            os.system("clear")
            sys.exit()
        else:
            print('\n[+] Eres tan pendejx que destruiste el juego!!!')
        
        time.sleep(1.5)
        os.system("clear")
        print("Reiniciando el juego.")
        time.sleep(0.8)
        os.system("clear")
    
try:   
    while True:
        print('''
          Bienvenidx a piedra, papel o tijera. :D
            + Cuando quieras salir escribe: salir
            + Procura escribir bien.
            + Espero te guste.
          ''')
        juego()
except KeyboardInterrupt:
    os.system("clear")
    print('Haz cerrado el juego con CTRL + C')