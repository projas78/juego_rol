from db import crear_bd
from players_game import contar_prologo, reglas_batalla, tablero, ingresar_nombre, \
    lista_jugadores, mostrar_reglas, elegir_jugador, decir_bienvenido, guardar_jugador, jefe_final, Jefe_Final

crear_bd()
mostrar_reglas()
nombre = ingresar_nombre()
jugador = elegir_jugador()
boss = Jefe_Final(jugador.categoria, jugador.ataque * 2, jugador.defensa * 2, jugador.vida * 2, jugador.velocidad * 2, jugador.arma)
guardar_jugador(nombre, jugador.categoria)
decir_bienvenido(nombre, jugador)
contar_prologo()
reglas_batalla()
tablero(jugador, nombre, boss)


"""
que se guarden las victorias y derrotas
mejoras los textos
diseñar jefes final
misiones secunderias de la cueva
"""