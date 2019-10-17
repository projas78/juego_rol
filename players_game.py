import random

from db import agregar_jugador, lista_jugadores, gano, perdio


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
        super(Mago, self).__init__("Mago", 7, 4, 10, 6, "Varita")


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


class Jefe_Final(Player):
    pass


def mostrar_reglas():
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


def ingresar_nombre():
    jugadores = lista_jugadores()

    opcion = input("¿Desea crear un usuario nuevo o usar uno existente?, seleccione 'n' (nuevo) o 'e' (existente)\n")
    while True:
        if opcion.lower() == 'e':
            nombre = input("Ingrese el nombre de su usuario\n")
            nombre = nombre.capitalize()
            if nombre in jugadores:
                print("Bienvenido otra vez {}".format(nombre))
                break
            else:
                print("El usuario ingresado no existe")
        elif opcion.lower() == 'n':
            nombre = input("Ingrese un nombre para poder crear su usuario\n")
            nombre = nombre.capitalize()
            if len(nombre) < 3 or len(nombre) > 15:
                print("El nombre debe contener un minimo de 4 letras y un máximo de 15")

            elif nombre not in jugadores:
                print("Bienvenido al juego {}, Que comience el juego!!\n".format(nombre))
                break
            else:
                print("El nombre de usuario ya esta en uso, por favor eliga otro")
        else:
            print("La opcion ingresada es incorrecta, intentelo nuevamente")

    return nombre


def elegir_jugador():
    while True:
        print("""¿Qué jugador quiere elegir?
        1) Caballero
        2) Mago
        3) Arquero
        """)

        opcion = input()
        if opcion == '1':
            jugador = Caballero()
            break

        elif opcion == '2':
            jugador = Mago()
            break

        elif opcion == '3':
            jugador = Arquero()
            break

        else:
            print("La opción ingresada es incorrecta, vuelva a intertarlo")

    return jugador


def guardar_jugador(nombre, categoria):
    players_game = Personajes(nombre, categoria, 0, 0)
    players_game.save()


def decir_bienvenido(nombre, jugador):
    print("Bienvenido", jugador.categoria, nombre)
    print("Su jugador tiene los siguientes atributos\n")
    print(jugador)


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


def tablero(jugador, nombre):
    winner = False
    recorrer_tablero = 0
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado = random.randint(12, 12) #solo debug
        print("El dado giro y obtuvo: {}".format(resultado))
        recorrer_tablero += resultado
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
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un ladron te ataca!!\n")
            atacar_ladron(jugador)

        elif recorrer_tablero in (5, 10):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un elfo oscuro te ataca!!")
            atacar_elfo_oscuro(jugador)

        elif recorrer_tablero >= 12:
            print("Lucha contra el jefe final!!")
            print("============================")
            winner = jefe_final(jugador)
            break

    if winner:
        gano(nombre)
    else:
        perdio(nombre)


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
                print("Has ganado la pelea!!, continua jugando\n")
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


def jefe_final(jugador):
    jefe_final = Jefe_Final(jugador.categoria, jugador.ataque * 2, jugador.defensa * 2, jugador.vida * 2, jugador.velocidad * 2, jugador.arma)

    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo!")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: {}".format(resultado))
            jefe_final.recibir_daño(resultado)
            if jefe_final.esta_vivo():
                print("Orion: {}\nJugador: {}\n".format(jefe_final.vida, jugador.vida))
            else:
                print("Ha salvado el Reino")
                return True
        else:
            input("Orion va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado)
            if jugador.esta_vivo():
                print("Orion: {}\nJugador: {}\n".format(jefe_final.vida, jugador.vida))
            else:
                print("Perdiste, el Reino ha caido")
                return False


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

def armadura_legendaria():
    print("""Cuenta la leyenda que en los bosques susurrantes esta la armadura legendaria.  Capaz de disminuir el poder 
de los ataques y de resistir cualquier golpe.  
Deberás desviarte de tu camino e introducirte en la pronfundidad del bosque
Pero para conseguirla debes hacer 3 desafios.
 
""")


## 1 - Duplica tu vida maxima al doble.
## 2 - Recupera tu vida al 100%
## 3 - Te resta tu vida actual a la mitad.
## 4 - Te deja tu vida en cero y termina la partida.
## 5 - Al entrar por esa entrada vuelves a la posicion que estabas con la misma vida que tenias.

##un demonio dorado, que tenga 100 de vida,
# que cuando grita se cura 5 de vida y daña 20 potenciado


# print("-Pense que nunca vendrias o que ya estarias muerto-", nombre)
# print("-¿Quien eres?-, pregunto el",jugador.categoria)
# print("-Despues de todo este camino, no descubriste quien soy, hermano....")
# print("-Yo no tengo ningun hermano-. dijo el",jugador.categoria, nombre)
# print("-Jajaja, eso es lo que siempre creiste-\n")
# print("mas historia proximamente\n")
# print("-Pero hoy moriras, el reino de Camelot caera y a ti nadie te recordada-")
# print("-Eso lo veremos-. Dijo el", jugador.categoria, nombre)