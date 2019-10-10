from db import crear_bd
from players_game import Caballero, Mago, Arquero, contar_prologo, reglas_batalla, tablero, Personajes

from tabulate import tabulate

print("""Bienvenido a Mundo Medieval
===========================
Reglas del juego
================
1 - Deberás elegir entre ser un Caballero, un Mago o un Arquero.  Cada uno tiene habilidades diferentes
2 - Tirar un dado con los números entre 1 al 6
3 - El número que salga es la cantidad de casilleros que deberá avanzar.
4 - Cada Casillero puede tener un desafío
5 - Para ganar deberá vencer todos los desafios y al jefe final.
""")

while True:
    print("""¿Qué jugador quiere elegir?
    1) Caballero
    2) Mago
    3) Arquero
    """)
    crear_bd()

    opcion = input()
    if opcion == '1':

        jugador = Caballero()
        print("Felicitaciones usted elegió al caballero, por favor ingrese un nombre: ")

        if __name__ == "__main__":

            while True:
                nombre = input()
                if len(nombre) < 3 or len(nombre) > 15:
                    print("El nombre debe contener un minimo de 4 letras y un máximo de 15")
                else:
                    print("Bienvenido al juego Caballero {}.".format(nombre.capitalize()))
                    print("=========================================")
                    print("Su jugador tiene los siguientes atributos\n")
                    print(jugador, "\n")
                    break
            break

            players_game = Personajes(nombre, categoria, victorias, derrotas)
            players_game.save()

    elif opcion == '2':
        jugador = Mago()
        print("Felicitaciones usted elegió al Mago, por favor ingrese un nombre: ")

        while True:
            nombre = input()
            if len(nombre) < 3 or len(nombre) > 15:
                print("El nombre debe contener un minimo de 4 letras y un máximo de 15")
            else:
                print("Bienvenido al juego Mago {}.".format(nombre.capitalize()))

                print("======================================")
                print("Su jugador tiene los siguientes atributos\n")
                print(jugador, "\n")
                break
        break

    elif opcion == '3':
        jugador = Arquero()
        print("Felicitaciones usted elegió al Arquero, por favor ingrese un nombre: ")

        while True:
            nombre = input()
            if len(nombre) < 3 or len(nombre) > 15:
                print("El nombre debe contener un minimo de 4 letras y un máximo de 15")
            else:
                print("Bienvenido al juego Arquero {}.".format(nombre.capitalize()))

                print("======================================")
                print("Su jugador tiene los siguientes atributos\n")
                print(jugador, "\n")
                break
        break

    else:
        print("La opción ingresada es incorrecta, vuelva a intertarlo")

contar_prologo()
reglas_batalla()
tablero(jugador)


