from db import crear_bd, agregar_jugador, contar_prologo, tablero, atributos, reglas_batalla, borrar_tablero, \
    atacar_ladron, menu

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


crear_bd()
agregar_jugador()
menu()
contar_prologo()
reglas_batalla()
tablero()
borrar_tablero()