import random

from db import agregar_jugador, lista_jugadores, gano, perdio


class Player:

    def __init__(self, categoria, ataque, defensa, vida, vida_maxima, velocidad, arma):
        self.categoria = categoria
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.velocidad = velocidad
        self.arma = arma

    def recibir_daño(self, daño, enemigo):
        total_damage = (daño - self.defensa + enemigo.ataque)
        if total_damage > 0:
            self.vida -= total_damage
        else:
            self.vida -= 1


    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f'Categoria: {self.categoria} \nAtaque: {self.ataque} \nDefensa: {self.defensa}' \
               f'\nVida: {self.vida} / {self.vida_maxima} \nVelocidad: {self.velocidad} \nArma: {self.arma}'


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
        super(Caballero, self).__init__("Caballero", 9, 20, 100, 100, 3, "Espada")


class Mago(Player):
    def __init__(self):
        super(Mago, self).__init__("Mago", 6, 4, 100, 100, 6, "Varita")


class Arquero(Player):
    def __init__(self):
        super(Arquero, self).__init__("Arquero", 3, 3, 70, 70, 9, "Arco y Flecha")


class Orko(Player):
    def __init__(self):
        super(Orko, self).__init__("Orko", 8, 6, 20, 20, 2, "Mazo")


class Elfo_Oscuro(Player):
    def __init__(self):
        super(Elfo_Oscuro, self).__init__("Elfo_oscuro", 6, 4, 14, 14, 6, "Magia Oscura")


class Ladron(Player):
    def __init__(self):
        super(Ladron, self).__init__("Ladron", 2, 1, 5, 5, 2, "Golpes")


class Jefe_Final(Player):
    pass


class Armadura_Dorada(Player):
    def __init__(self):
        super(Armadura_Dorada, self).__init__("Armadura Dorada", 6, 4, 25, 25, 11, "Gigante")


class Protego(Player):
    def __init__(self):
        super(Protego, self).__init__("Troll de la montaña", 8, 5, 20, 20, 15, "Mazo de madera")


class Merlin(Player):
    def __init__(self):
        super(Merlin, self).__init__("Mago Supremo", 7, 4, 18, 18, 15, "Varita de Sauco")


class Hombre_Lobo(Player):
    def __init__(self):
        super(Hombre_Lobo, self).__init__("Hombre Lobo", 10, 5, 16, 16, 25, "Mordedura")


def tirar_dado():
    input("Presione Enter para tirar el dado.\n")
    resultado = random.randint(7, 7)  # solo debug

    return resultado

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

    while True:
        opcion = input("¿Desea crear un usuario nuevo o usar uno existente?, seleccione 'n' (nuevo) o 'e' (existente)\n")
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
    print(jugador, "\n")


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


def tablero(jugador, nombre, boss):
    winner = False
    recorrer_tablero = 0
    while jugador.esta_vivo():
        resultado = tirar_dado()
        print("El dado giro y obtuvo: {}".format(resultado))
        if recorrer_tablero < 10:
            recorrer_tablero = min(recorrer_tablero + resultado, 10)
        elif recorrer_tablero < 15:
            recorrer_tablero = min(recorrer_tablero + resultado, 15)
        else:
            recorrer_tablero += resultado
        if recorrer_tablero in (1, 2, 8, 11, 16, 17, 18, 19):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Vuelva a tirar el dado\n")
        elif recorrer_tablero == 9:
            if jugador.vida == jugador.vida_maxima:
                jugador.vida = jugador.vida_maxima
                print("Escontraste un arbol de manzanas y comes una, recuperas 2 de energía:", jugador.vida, "/",
                      jugador.vida_maxima)
            else:
                jugador.vida += 2
                print("Escontraste un arbol de manzanas y comes una, recuperas 2 de energía:", jugador.vida, "/", jugador.vida_maxima)

        elif recorrer_tablero in (3, 7):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un Orko te ataca!!!\n")
            atacar_orko(jugador, nombre)

        elif recorrer_tablero in (4, 6):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un ladron te ataca!!\n")
            atacar_ladron(jugador, nombre)

        elif recorrer_tablero in (5, 14):
            print("Usted avanza a la posición: {}\n".format(recorrer_tablero))
            print("Un elfo oscuro te ataca!!")
            atacar_elfo_oscuro(jugador, nombre)

        elif recorrer_tablero == 12:
            dormir(jugador, nombre)

        elif recorrer_tablero == 10:
            if jugador.categoria == "Caballero":
                print("""Si entras por el bosque podrás tratar de conseguir la armadura dorada.  Pero te en cuenta que
si pierdes haciendo esta misiòn moriras y se terminara el juego.\n""")
                while True:
                    opcion = input("""¿Esta seguro que desea conseguir la armadura? Ingrese 'y' si quiere ir por la
armadura o 'n' si prefiere seguir por el camino\n""")
                    if opcion.lower() == "y":
                        sec_armadura_dorada(jugador, nombre)
                        break
                    elif opcion.lower() == "n":
                        print("No necesito la armadura dorada para salvar el reino, voy a continuar\n")
                        break
                    else:
                        print("La opcion ingresada es incorrecta, vuelva a intentarlo")

            elif jugador.categoria == "Mago":
                print("""En el bosque de las hadas se dice que su lider el Hada Azul tiene la habilidad de enseñarte el 
hechizo Protego.  Pero para aprenderlo, el Hada Azul solo te pide una condición.  Que derrotes al semi gigante que desde
hace años esta atacando el bosque y mantando a todo el que se le cruce en el camino.
Pero te en cuenta que si pierdes haciendo esta misiòn moriras y se terminara el juego.\n
                """)
                while True:
                    opcion = input("""¿Esta seguro que desea aprender el hechizo protego? Ingrese 'y' si quiere 
aprenderlo o 'n' si prefiere seguir por el camino\n""")
                    if opcion.lower() == "y":
                        sec_armadura_dorada(jugador, nombre)
                        break
                    elif opcion.lower() == "n":
                        print("No necesito aprender un hechizo para salvar el reino, voy a continuar\n")
                        break
                    else:
                        print("La opcion ingresada es incorrecta, vuelva a intentarlo")

        elif recorrer_tablero == 15:
            if jugador.categoria == "Caballero":
                sec_espada_excallibur(jugador, nombre)

            elif jugador.categoria == "Mago":
                print("Lucha contra merlin por la Varita de Sauco")
                sec_varita_sauco(jugador, nombre)

            elif jugador.categoria == "Arquero":
                print("Tiene la posibilidad de conseguir el Arco de Robin Hood")
                sec_arco_robin_hood(jugador, nombre)

        elif recorrer_tablero >= 20:
            print("Lucha contra el jefe final!!")
            print("============================")
            winner = jefe_final(jugador, boss, nombre)
            break

    if winner:
        gano(nombre)
        print("Ha salvado el Reino")
    else:
        perdio(nombre)
        print("Perdiste, el Reino ha caido y mueres")


def atacar_ladron(jugador, nombre):
    ladron = Ladron()
    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2)  # solo debug
        print("El dado giro y obtuvo: ", resultado_tablero)
        print("Ladron: {} / {}\n{}: {} / {}".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 2)
            print("Le sacas {} de energía a tu enemigo".format(resultado))
            ladron.recibir_daño(resultado, jugador)
            if ladron.vida >= ladron.vida_maxima:
                ladron.vida = ladron.vida_maxima
                if ladron.esta_vivo():
                    print("Ladrón: {} / {}\n{}: {} / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Ladrón: {} / {}\n{}: 0 / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida_maxima))
            else:
                if ladron.esta_vivo():
                    print("Ladrón: {} / {}\n{}: {} / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print("Ha ganado la pelea, continue jugando")
                    break
        else:
            input("El Ladron va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 6)
            print(resultado)
            jugador.recibir_daño(resultado, ladron)
            if jugador.vida >= jugador.vida_maxima:
                jugador.vida = jugador.vida_maxima
                if jugador.esta_vivo():
                    print("Ladrón: {} / {}\n{}: {} / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Ladrón: {} / {}\n{}: 0 / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida_maxima))
            else:
                if jugador.esta_vivo():
                    print("Ladrón: {} / {}\n{}: {} / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Ladrón: {} / {}\n{}: 0 / {}\n".format(ladron.vida, ladron.vida_maxima, nombre, jugador.vida_maxima))


def atacar_elfo_oscuro(jugador, nombre):
    elfo_oscuro = Elfo_Oscuro()
    while jugador.esta_vivo():
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))
        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("Le sacas {} de energía a tu enemigo".format(resultado))
            elfo_oscuro.hacer_daño(resultado, jugador)
            if elfo_oscuro.vida >= elfo_oscuro.vida_maxima:
                elfo_oscuro.vida = elfo_oscuro.vida_maxima
                if elfo_oscuro.esta_vivo():
                    print("Elfo Oscuro: {} / {}\n{}: {} / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Elfo Oscuro: {} / {}\n{}: 0 / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida_maxima))
            else:
                if elfo_oscuro.esta_vivo():
                    print("Elfo Oscuro: {} / {}\n{}: {} / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print("Ha ganado la pelea, continue jugando")
                    break
        else:
            input("El Elfo Oscuro va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 6)
            print(resultado)
            jugador.recibir_daño(resultado, elfo_oscuro)
            if jugador.vida >= jugador.vida_maxima:
                jugador.vida = jugador.vida_maxima
                if jugador.esta_vivo():
                    print("Elfo Oscuro: {} / {}\n{}: {} / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Elfo Oscuro: {} / {}\n{}: 0 / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida_maxima))
            else:
                if jugador.esta_vivo():
                    print("Elfo Oscuro: {} / {}\n{}: {} / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida,
                                                                jugador.vida_maxima))
                else:
                    print(
                        "Elfo Oscuro: {} / {}\n{}: 0 / {}\n".format(elfo_oscuro.vida, elfo_oscuro.vida_maxima, nombre, jugador.vida_maxima))


def atacar_orko(jugador, nombre):
    orko = Orko()
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo!")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 6)
            print("Le sacas {} de energía a tu enemigo".format(resultado))
            orko.recibir_daño(resultado, jugador)
            if orko.esta_vivo():
                print("Orko: {} / {}\n{}: {} / {}\n".format(orko.vida, orko.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Orko: 0 / {}\n{}: {} / {}\n".format(orko.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
                print("Ha ganado la pelea, continue jugando")
                break
        else:
            input("El Orko va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 6)
            print(resultado)
            jugador.recibir_daño(resultado, orko)
            if jugador.esta_vivo():
                print("Orko: {} / {}\n{}: {} / {}\n".format(orko.vida, orko.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Orko: {} / {}\n{}: 0 / {}\n".format(orko.vida, orko.vida_maxima, nombre, jugador.vida_maxima))


def jefe_final(jugador, boss, nombre):
    print(boss)
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo!\n")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 6)
            print("Le sacas {} de energia a tu enemigo".format(resultado))
            boss.recibir_daño(resultado)
            if boss.esta_vivo():
                print("Orion: {} / {}\n{}: {} / {}\n".format(boss.vida, boss.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                return True
        else:
            input("Orion va a atacarte, presiona Enter para continuar!\n")
            resultado = random.randint(1, 6)
            jugador.recibir_daño(resultado, boss)
            if jugador.esta_vivo():
                print("Orion: {} / {}\n{}: {} / {}\n".format(boss.vida, boss.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
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


def sec_armadura_dorada(jugador, nombre):
    print("""Cuenta la leyenda que en los bosques susurrantes esta la armadura legendaria.  Capaz de disminuir el poder
de los ataques del enemigo y de resistir cualquier golpe.  
Pero para conseguirla deberás vencer al Gigante de Hierro.
""")
    armadura_dorada = Armadura_Dorada()
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo!\n")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 6)
            print("El dado giro y obtuvo: {}".format(resultado))
            armadura_dorada.recibir_daño(resultado, jugador)
            if armadura_dorada.esta_vivo():
                print("Gigante de Hierro: {} / {}\n{}: {} / {}\n".format(armadura_dorada.vida, armadura_dorada.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Ha ganado la pelea y obtienes la armadura dorada., continue jugando\n")
                jugador.defensa += 2
                print(jugador, "\n")
                break
        else:
            input("El Gigante de Hierro va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            print(resultado)
            jugador.recibir_daño(resultado, armadura_dorada)
            if jugador.esta_vivo():
                print("Gigante de Hierro: {} / {}\n{}: {} / {}\n".format(armadura_dorada.vida, armadura_dorada.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Gigante de Hierro: {} / {}\n{}: 0 / {}\n".format(armadura_dorada.vida, armadura_dorada.vida_maxima, nombre, jugador.vida_maxima))


def sec_espada_excallibur(jugador, nombre):
    print("""Bienevido {} {}. Te encontraste con la espada de Excalibur atrapada en una roca.
Para obtenerla debe tirar con fuerza de la espalda para sacarla de la roca.
Reglas:
Podras tirar el dado hasta 4 veces y deberas sumar 10 o más punto para obtener la espada.
Si tiraste el dado las 4 veces y no sumaste 10 la espada desaparecerá y no podrás volver a intentarlo.
    """.format(jugador.categoria, nombre))
    contador = 0
    resultado = 0
    while contador < 4:
        input("Presione Enter para tirar el dado.")
        dado = random.randint(1, 6)
        contador += 1
        print("El dado giro y obtuvo: {}".format(dado))
        resultado = dado + resultado
        if resultado >= 10:
            print("Felicitaciones, obtuviste la espada de Escalibur, tu ataque se incrementa en +2")
            jugador.ataque += 2
            break
        else:
            print("Tiraste de la espada {} veces y tu puntajes es {}.\n".format(contador, resultado))
    else:
        print("No eres digno de tener la espada de escalibur")

def sec_hechizo_escudo(jugador, nombre):
    protego = Protego()
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo\n!")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 6)
            print("El dado giro y obtuvo: {}".format(resultado))
            protego.recibir_daño(resultado, jugador)
            if protego.esta_vivo():
                print("Troll de la montaña: {} / {}\n{}: {} / {}\n".format(protego.vida, protego.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Ha ganado la pelea, continue jugando\n")
                jugador.defensa += 2
                break
        else:
            input("Troll de la montaña va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado, protego)
            if jugador.esta_vivo():
                print("Troll de la montaña: {} / {}\n{}: {} / {}\n".format(protego.vida, protego.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Troll de la montaña: {} / {}\n{}: 0 / {}\n".format(protego.vida, protego.vida_maxima, nombre, jugador.vida_maxima))


def sec_varita_sauco(jugador, nombre):
    merlin = Merlin()
    while jugador.esta_vivo():
        input("Presione Enter para tirar el dado.")
        resultado_tablero = random.randint(1, 6)
        print("El dado giro y obtuvo: {}".format(resultado_tablero))

        if resultado_tablero in (1, 3, 5):
            print("Ataca a tu enemigo\n!")
            input("Presione Enter para tirar el dado.")
            resultado = random.randint(1, 6)
            print("El dado giro y obtuvo: {}".format(resultado))
            merlin.recibir_daño(resultado, jugador)
            if merlin.esta_vivo():
                print("El Mago Merlin: {} / {}\n{}: {} / {}\n".format(merlin.vida, merlin.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("Ha ganado la pelea, continue jugando\n")
                break
        else:
            input("El Mago Merlin va a atacarte, presiona Enter para continuar!")
            resultado = random.randint(1, 2)
            jugador.recibir_daño(resultado, merlin)
            if jugador.esta_vivo():
                print("El Mago Merlin: {} / {}\n{}: {} / {}\n".format(merlin.vida, merlin.vida_maxima, nombre, jugador.vida, jugador.vida_maxima))
            else:
                print("El Mago Merlin: {} / {}\n{}: 0 / {}\n".format(merlin.vida, merlin.vida_maxima, nombre, jugador.vida_maxima))


def sec_arco_robin_hood(jugador, nombre):
    print("""Bienevido {} {}. Estas en la guarida donde vivia Robin Hood.
    Reglas:
    Podras tirar el dado hasta 4 veces y deberas sumar 10 o más punto para obtener la espada.
    Si tiraste el dado las 4 veces y no sumaste 10 el escudo desaparecerá y no podrás volver a intentarlo.
        """.format(jugador.categoria, nombre))
    contador = 0
    resultado = 0
    while contador < 4:
        input("Presione Enter para tirar el dado.")
        dado = random.randint(3, 3)
        contador += 1
        print("El dado giro y obtuvo: {}".format(dado))
        resultado = dado + resultado
        if resultado >= 10:
            print("Felicitaciones, obtuviste el arco de Robin Hood, tu ataque se incrementa en +2")
            break
        else:
            print("Tiraste con tu arco {} veces y tu puntajes es {}.\n".format(contador, resultado))
    else:
        print("No eres digno de tener el arco de Robin Hood")


def dormir(jugador, nombre):
    print("""Ya es de noche y debes descansar.  Este lugar del bosque parece seguro.
Pero debes tomar una importante decisión.

Reglas
1 - Si eliges dormir sin prender una fogata te aseguras de que ningun animal te ataquedurante la noche.  
Pero solo recuperarás 5 de energía ya que en el bosque hace mucho frío y te costará dormirte.
2 - Si elegis dormir con una fogata encendida hay posibilidades de que los lobos te ataquen durante la noche y 
tendras que pelear (al momento de pelear tu energia estará al maximo)
Pero si a pesar de la fogata ningun lobo te encuentra al despertar tendrás tu energia al máximo      
    """)
    while True:
        print("Tu vida actual es {} / {}, que vas a hacer?\n".format(jugador.vida, jugador.vida_maxima))
        print("¿Que vas a hacer?, selecciona 1 o 2: ")
        opcion = input()
        if opcion == '1':
            print("No quiero correr riegos, voy a domir en la oscuridad para que nadie me encuentre\n")
            jugador.vida += 5
            input()
            print("A pesar del frio pudiste descansar, tu nueva vida es {} / {}\n".format(jugador.vida, jugador.vida_maxima))
            break

        elif opcion == '2':
            print(jugador)
            print("Hace mucho frio esta noche, voy a encender una fogata o no podré descansar\n")
            input("Presione Enter para continuar.\n")
            dado = random.randint(1, 6)
            print("salio", dado) #debug
            if dado in (1, 6):
                print("Pasaste la noche sin ningun peligro")
                jugador.vida = jugador.vida_maxima
                print("Tenes la vida al máximo {} / {}\n".format(jugador.vida, jugador.vida_maxima))
                break
            else:
                print("Un Hombre Lobo te encontró y va a atacarte")
                jugador.vida = jugador.vida_maxima
                print("Tenes la vida al máximo {} / {}".format(jugador.vida, jugador.vida_maxima))
                hombre_lobo = Hombre_Lobo()
                while jugador.esta_vivo():
                    input("Presione Enter para tirar el dado.")
                    resultado_tablero = random.randint(1, 6)
                    print("El dado giro y obtuvo: {}".format(resultado_tablero))

                    if resultado_tablero in (1, 3, 5):
                        print("Ataca a tu enemigo!\n")
                        input("Presione Enter para tirar el dado.")
                        resultado = random.randint(1, 6)
                        print("El dado giro y obtuvo: {}".format(resultado))
                        hombre_lobo.recibir_daño(resultado, jugador)
                        if hombre_lobo.esta_vivo():
                            print(
                                "Hombre Lobo: {} / {}\n{}: {} / {}\n".format(hombre_lobo.vida, hombre_lobo.vida_maxima,
                                                                                     nombre, jugador.vida,
                                                                                     jugador.vida_maxima))
                        else:
                            print("Ha ganado la pelea, continue jugando\n")
                            break

                    else:
                        input("Hombre Lobo va a atacarte, presiona Enter para continuar!")
                        resultado = random.randint(1, 2)
                        jugador.recibir_daño(resultado, hombre_lobo)
                        if jugador.esta_vivo():
                            print(
                                "Hombre Lobo: {} / {}\n{}: {} / {}\n".format(hombre_lobo.vida, hombre_lobo.vida_maxima,
                                                                                     nombre, jugador.vida,
                                                                                     jugador.vida_maxima))
                        else:
                            print("Hombre Lobo: {} / {}\n{}: 0 / {}\n".format(hombre_lobo.vida, hombre_lobo.vida_maxima,
                                                                                      nombre, jugador.vida_maxima))

        else:
            print("La opción ingresada es incorrecta, vuelva a intertarlo")

        break


# Merlin esta durmiendo si la suma da 10 es tuyas y no te vas corriendo y no la volves a ver
# funcion batalla le paso dos personajes (jugador, enemigo)