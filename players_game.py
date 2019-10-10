import random
from tabulate import tabulate

from db import agregar_jugador


class Player:

    def __init__(self, categoria, ataque, defensa, vida, velocidad, arma):
        self.categoria = categoria
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.velocidad = velocidad
        self.arma = arma

    def recibir_daño(self, daño):
        self.vida = self.vida - daño

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f'Categoria: {self.categoria} \nAtaque: {self.ataque} \nDefensa: {self.defensa}' \
               f'\nVida: {self.vida} \nVelocidad: {self.velocidad} \nArma: {self.arma}'


class Personajes:

    def __init__(self, nombre, categoria, victorias, derrotas):
        self.nombre = nombre
        self.categoria = categoria
        self.victorias = victorias
        self.derrotas = derrotas

    def __str__(self):
        return f'Nombre: {self.nombre} \nCategoria {self.categoria} \nVictorias: {self.victorias}' \
               f'\nDerrotas: {self.derrotas}\n'

    def save(self):
        agregar_jugador(self.nombre, self.categoria, self.victorias, self.derrotas)


class Caballero(Player):
    def __init__(self):
        super(Caballero, self).__init__("Caballero", 10, 9, 10, 3, "Espada")


class Mago(Player):
    def __init__(self):
        super(Mago, self).__init__("Mago", 7, 4, 8, 6, "Varita")


class Arquero(Player):
    def __init__(self):
        super(Arquero, self).__init__("Arquero",6, 5, 7, 9, "Arco y Flecha")


class Orko (Player):
    def __init__(self):
        super(Orko, self).__init__("Orko", 14, 12, 18, 2, "Mazo")


class Elfo_oscuro(Player):
    def __init__(self):
        super(Elfo_oscuro, self).__init__("Elfo_oscuro", 6, 4, 8, 6, "Magia Oscura")


class Ladron(Player):
    def __init__(self):
        super(Ladron, self).__init__("Ladron", 3, 3, 5, 4, "Golpes")


def tablero(jugador):
    recorrer_tablero = 0
    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado = random.randint(1, 3) #solo debug
        print("El dado giro y obtuvo: {}".format(resultado))
        recorrer_tablero = recorrer_tablero + resultado
        if recorrer_tablero in (1, 2, 11):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Vuelva a tirar el dado\n")
        elif recorrer_tablero == 9:
            jugador.vida += 2
            print("Escontraste un arbol de manzanas y comes una, recuperas 2 de energía:", jugador.vida)

        elif recorrer_tablero in (3, 7):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un Orko te ataca!!!\n")
            atacar_orko(jugador)

        elif recorrer_tablero in (4, 6):
            print("Usted avanza a la posición: \n".format(recorrer_tablero))
            print("Un ladron te ataca!!\n")
            atacar_ladron(jugador)

        elif recorrer_tablero in (5, 10):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un elfo oscuro te ataca!!")
            atacar_elfo_oscuro(jugador)

        elif recorrer_tablero >= 12:
            print("Lucha contra el jefe final!!")
            print("============================")
            print("Ganaste el juego!")
            break
    else:
        print("Perdiste, fin del juego!")


def atacar_ladron(jugador):
    ladron = Ladron()
    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2) #solo debug
        print("El dado giro y obtuvo: ", resultado_tablero)
        print("Ladron: {}\nJugador: {}".format(ladron.vida, jugador.vida)) #debug

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: {}".format(resultado))
            ladron.recibir_daño(resultado)
            if ladron.esta_vivo():
                print("Ladron: {}\nJugador: {}\n".format(ladron.vida, jugador.vida))
            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El ladron va a atacarte, presiona Enter para comenzar con la batalla!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado
                                 )
            if jugador.esta_vivo():
                print("Ladron: {}\nJugador: {}\n".format(ladron.vida, jugador.vida))
            else:
                print("Ladron: {}\nJugador: 0\n".format(ladron.vida))


def atacar_elfo_oscuro(jugador):
    elfo_oscuro = Elfo_oscuro()

    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: {}".format(resultado))
            elfo_oscuro.recibir_daño(resultado)
            if elfo_oscuro.esta_vivo():
                print("Elfo Oscuro: {}\nJugador: {}\n".format(elfo_oscuro.vida, jugador.vida))
            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El Elfo Oscuro va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)  # solo debug
            if jugador.esta_vivo():
                print("Elfo Oscuro: {}\nJugador: {}\n".format(elfo_oscuro.vida, jugador.vida))
            else:
                print("Elfo Oscuro: {}\nJugador: 0\n".format(elfo_oscuro.vida))
                
                
def atacar_orko(jugador):
    orko = Orko()

    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo!")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: {}".format(resultado))
            orko.recibir_daño(resultado)
            if orko.esta_vivo():
                print("Orko: {}\nJugador: {}\n".format(orko.vida, jugador.vida))
            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El Orko va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)
            if jugador.esta_vivo():
                print("Orko: {}\nJugador: {}\n".format(orko.vida, jugador.vida))
            else:
                print("Orko: {}\nJugador: 0\n".format(orko.vida))


def contar_prologo():
    input("Presione Enter para continuar.")
    print("Agregar historia aquí (next comming)\n")


def reglas_batalla():
    while True:
        print("Quiere ver las reglas de la batalla?, Ingrese 'y' o 'n'")
        opcion = input()
        if opcion.lower() == 'y':

            print("""Debes tirar el dado cada vez que te enfrentes a un enemigo
Si sacás 1, 3 o 5 podrás atacar.
Cada ataque vale 2 puntos mas el numero que saques del dado.
Cuando el enemigo llegue a cero podras volver a ejecutar el dado y continuar el juego           
Si sacás 2, 4 o 6 el enemigo te atacará.
Cada ataque vale el valor del dado mas el ataque que tenga cada enemigo
Si tu jugador queda en cero de vida perderás el juego
""")
            break
        elif opcion.lower() == 'n':
            break
        else:
            print("La opción ingresada es incorrecta")


def ms_cueva_Sorginak(jugador):
    print("""Te cruzaste con la cueva de Sorginak.\n Cuando entres veras que hay 2 caminos. Ten cuidado porque la cueva 
es maǵica y las entradas todo el tiempo cambian de lugar (No siempre el número que eligas sera la misma entrada).

Las 2 entradas pueden darte lo siguiente:

Duplica tu vida actual
Mueres

Elige un número entre 1 o 2 y deja que el destino haga el resto!!
    """)
    while True:
        opcion = input("Ingresa 1 o 2")
        if opcion == '1':
            print("Duplica tu vida actual")
            jugador.vida = jugador.vida * 2

        elif opcion == '2':
            jugador.vida = 0

            print("Mueres")
            break

        else:
            print("Opcion incorrecta.")

## 1 - Duplica tu vida maxima al doble.
## 2 - Recupera tu vida al 100%
## 3 - Te resta tu vida actual a la mitad.
## 4 - Te deja tu vida en cero y termina la partida.
## 5 - Al entrar por esa entrada vuelves a la posicion que estabas con la misma vida que tenias.