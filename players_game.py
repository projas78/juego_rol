import random

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
    while True:
        input("Presione cualquier tecla para tirar el dado.")
        resultado = random.randint(5, 6) #solo debug
        print("El dado giro y obtuvo: ", resultado)
        recorrer_tablero = recorrer_tablero + resultado
        if recorrer_tablero in (1, 2, 6, 9, 11):
            print("Usted avanza a la posición:", recorrer_tablero, "\n")
            print("Vuelva a tirar el dado\n")
        elif recorrer_tablero in (3, 7):
            print("Usted avanza a la posición:", recorrer_tablero, "\n")
            print("Un Orko te ataca!!!\n\n")
            orko(jugador)

        elif recorrer_tablero in (4, 6):
            print("Usted avanza a la posición:", recorrer_tablero, "\n")
            print("Un ladron te ataca!!, preparate para la batalla!!")
            atacar_ladron(jugador)

        elif recorrer_tablero in (5, 10):
            print("Usted avanza a la posición:", recorrer_tablero, "\n")
            print("Un elfo oscuro te ataca!!")
            elfo_oscuro(jugador)

        elif recorrer_tablero >= 12:
            print("Lucha contra el jefe final!!")
            print("============================")
            print("Ganaste el juego!")
            break


def atacar_ladron(jugador):
    ladron = Ladron()

    while True:
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(2, 3) #solo debug
        print("El dado giro y obtuvo: ", resultado_tablero)

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: ", resultado)
            ladron.recibir_daño(resultado)
            if ladron.esta_vivo():
                print("Al ladron le queda ", ladron.vida, " de vida")
            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El ladron va a atacarte, presiona cualquier tecla para comenzar con la batalla!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)
            print("El ladron te saco", resultado, "de vida y te quedan ", jugador.vida, " de energía")
            if jugador.esta_vivo():
                print("Continua")
            else:
                print("Fin del juego")
                break


def elfo_oscuro(jugador):
    elfo_oscuro = Elfo_oscuro()

    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: ", resultado_tablero)

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: ", resultado)
            elfo_oscuro.recibir_daño(resultado)
            if elfo_oscuro.esta_vivo():
                print("Al Elfo Oscuro le queda ", elfo_oscuro.vida, " de vida")
            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El Elfo Oscuro va a atacarte, presiona cualquier tecla para comenzar con la batalla!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)
            print("El Elfo Oscuro te saco", resultado, "de vida y te quedan ", jugador.vida, " de energía")

    else:
        print("Fin del juego")


def orko(jugador):
    orko = Orko()

    while True:
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: ", resultado_tablero)

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: ", resultado)
            orko.recibir_daño(resultado)
            if orko.esta_vivo():
                print("Orko:", orko.vida, "de vida")

            else:
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El Orko va a atacarte, presiona cualquier tecla para comenzar con la batalla!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)
            print("El Orko te saco", resultado, "de vida y te quedan ", jugador.vida, " de energía")
            if jugador.esta_vivo():
                print("Continua")
            else:
                print("Fin del juego")
                break

def contar_prologo():
    input("Presione cualquier tecla para continuar.")
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


