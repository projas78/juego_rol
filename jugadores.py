from db import crear_bd
from players_game import Caballero, Mago, Arquero, contar_prologo, reglas_batalla, tablero, Personajes, ingresar_nombre, \
    lista_jugadores, mostrar_reglas, elegir_jugador, decir_bienvenido, guardar_jugador

crear_bd()
mostrar_reglas()
nombre = ingresar_nombre()
jugador = elegir_jugador()
guardar_jugador(nombre, jugador.categoria)
decir_bienvenido(nombre, jugador)
contar_prologo()
reglas_batalla()
tablero(jugador)