from db import crear_bd
from players_game import contar_prologo, reglas_batalla, tablero, ingresar_nombre, \
    lista_jugadores, mostrar_reglas, elegir_jugador, decir_bienvenido, guardar_jugador, jefe_final


crear_bd()
mostrar_reglas()
nombre = ingresar_nombre()
jugador = elegir_jugador()
guardar_jugador(nombre, jugador.categoria)
decir_bienvenido(nombre, jugador)
contar_prologo()
reglas_batalla()
tablero(jugador, nombre)


"""
que se guarden las victorias y derrotas
mejoras los textos
diseñar jefes final
misiones secunderias de la cueva
"""