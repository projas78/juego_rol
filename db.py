import sqlite3
import random


def crear_bd():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute('''Create table if not exists jugadores (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        categoria varchar (20) NOT NULL,
                        ataque INTEGER NOT NULL, 
                        defensa INTEGER NOT NULL, 
                        vida INTEGER NOT NULL,
                        velocidad INTEGER NOT NULL,
                        arma varchar (20) NOT NULL
                        )
    ''')

    conexion.commit()
    conexion.close()


def agregar_jugador():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute("insert into jugadores values (null, 'Caballero',10 ,9,10, 3,'Espada')")
    cursor.execute("insert into jugadores values (null, 'Mago',7 ,4,8, 6,'Varita')")
    cursor.execute("insert into jugadores values (null, 'Arquero',6 ,5,7, 9,'Arco y Flecha')")
    cursor.execute("insert into jugadores values (null, 'Orko',14 ,12,18, 2,'Mazo')")
    cursor.execute("insert into jugadores values (null, 'Elfo_oscuro',6 ,4,8, 6,'Magia Oscura')")
    cursor.execute("insert into jugadores values (null, 'Ladron',3 ,3,5, 4,'Golpes de puño')")
    cursor.execute("insert into jugadores values (null, 'Jefe', 20, 18, 30, 14, 'Arma mortal')")

    conexion.commit()
    conexion.close()

def menu():
    while True:
        print("""¿Qué jugador quiere elegir?
        1) Caballero
        2) Mago
        3) Arquero
        """)
        conexion = sqlite3.connect('jugadores.db')
        cursor = conexion.cursor()

        opcion = input()
        if opcion == '1':
            cursor.execute("select * from jugadores where id = {}".format(opcion))
            jugadores = cursor.fetchall()

            print("Felicitaciones usted elegió al caballero, por favor ingrese un nombre: ")
            nombre = input()
            print("Bienvenido al juego Caballero {}.".format(nombre.capitalize()))

            print("======================================")
            print("Su jugador tiene los siguientes atributos")
            lista_jugador = []
            for jugador in jugadores:
                ID = jugador[0]
                categoria = jugador[1]
                ataque = jugador[2]
                defensa = jugador[3]
                vida = jugador[4]
                velocidad = jugador[5]
                arma = jugador[6]
                personaje = 'ID = {}\nCategoria = {}\nAtaque = {}\nDefensa = {}\nVida = {} \nVelocidad = {} \nArma = {}'.format(
                    ID, categoria, ataque, defensa, vida, velocidad, arma)
                lista_jugador.append(personaje)
            for jugador in lista_jugador:
                print(jugador,"\n")
            break

        elif opcion == '2':
            cursor.execute("select * from jugadores where id = {}".format(opcion))
            jugadores = cursor.fetchall()

            print("Felicitaciones usted elegió al Mago, por favor ingrese un nombre: ")
            nombre = input()
            print("Bienvenido al juego Mago {}.".format(nombre.capitalize()))

            print("======================================")
            print("Su jugador tiene los siguientes atributos")
            lista_jugador = []
            for jugador in jugadores:
                ID = jugador[0]
                categoria = jugador[1]
                ataque = jugador[2]
                defensa = jugador[3]
                vida = jugador[4]
                velocidad = jugador[5]
                arma = jugador[6]
                personaje = 'ID = {}\nCategoria = {}\nAtaque = {}\nDefensa = {}\nVida = {} \nVelocidad = {} \nArma = {}'.format(
                    ID, categoria, ataque, defensa, vida, velocidad, arma)
                lista_jugador.append(personaje)
            for jugador in lista_jugador:
                print(jugador, "\n")
            break

        elif opcion == '3':
            cursor.execute("select * from jugadores where id = {}".format(opcion))
            jugadores = cursor.fetchall()

            print("Felicitaciones usted elegió al Arquero, por favor ingrese un nombre: ")
            nombre = input()
            print("Bienvenido al juego Arquero {}.".format(nombre.capitalize()))

            print("======================================")
            print("Su jugador tiene los siguientes atributos")
            lista_jugador = []
            for jugador in jugadores:
                ID = jugador[0]
                categoria = jugador[1]
                ataque = jugador[2]
                defensa = jugador[3]
                vida = jugador[4]
                velocidad = jugador[5]
                arma = jugador[6]
                personaje = 'ID = {}\nCategoria = {}\nAtaque = {}\nDefensa = {}\nVida = {} \nVelocidad = {} \nArma = {}'.format(
                    ID, categoria, ataque, defensa, vida, velocidad, arma)
                lista_jugador.append(personaje)
            for jugador in lista_jugador:
                print(jugador, "\n")
            break

        else:
            print("La opción ingresada es incorrecta, vuelva a intentarlo")


def contar_prologo():
    print("Agregar historia aquí (next comming)")
    print("")


def tablero():
    recorrer_tablero = 0
    while True:
        input("Presione cualquier tecla para tirar el dado.")
        resultado = random.randint(1, 2)
        print("El dado giro y obtuvo: ", resultado)
        recorrer_tablero = recorrer_tablero + resultado
        if recorrer_tablero in (1, 2, 6, 9, 11):
            print("Ustes esta en la posicion:", recorrer_tablero, "\n")
            print("Vuelva a tirar el dado\n")
        elif recorrer_tablero in (3, 7):
            print("Ustes esta en la posicion:", recorrer_tablero, "\n")
            print("Un Orko te ataca!!!\n\n")

        elif recorrer_tablero in (4, 6):
            print("Ustes esta en la posicion:", recorrer_tablero, "\n")
            print("Un ladron te ataca!!, preparate para la batalla!!")
            atacar_ladron()

        elif recorrer_tablero in (5, 10):
            print("Ustes esta en la posicion:", recorrer_tablero, "\n")
            print("Un elfo oscuro te ataca!!")

        elif recorrer_tablero >= 12:
            print("Lucha contra el jefe final!!")
            print("============================")
            print("Ganaste el juego!")
            break


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


def atributos():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute("select * from jugadores")
    jugadores = cursor.fetchall()
    lista_jugador = []
    for jugador in jugadores:
        ID = jugador[0]
        categoria = jugador[1]
        ataque = jugador[2]
        defensa = jugador[3]
        vida = jugador[4]
        velocidad = jugador[5]
        arma = jugador[6]
        personaje = 'ID = {}Categoria = {}\nAtaque = {}\nDefensa = {}\nVida = {} \nVelocidad = {} \nArma = {}'.format(ID, categoria, ataque, defensa, vida, velocidad, arma)
        lista_jugador.append(personaje)
    for jugador in lista_jugador:
        print(jugador)


def borrar_tablero():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute("delete from jugadores")
    conexion.commit()
    conexion.close()


def atacar_ladron():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute("select * from jugadores where categoria = 'Ladron'")
    ladron = cursor.fetchall()
    vida = ladron[0][4]
    ataque = ladron[0][2]
    while True:
        input("Presione cualquier tecla para tirar el dado.")
        resultado_tablero = random.randint(1, 2)
        print("El dado giro y obtuvo: ", resultado_tablero)

        if resultado_tablero in (1, 3, 5):

            print("batalla vale:", vida) #debug
            print("Ataca a tu enemigo, tira el dado")
            input("Presione cualquier tecla para tirar el dado.")
            resultado = random.randint(1, 2)
            print("El dado giro y obtuvo: ", resultado)
            vida = vida - resultado
            if vida <= 0:
                print("Ha ganado la pelea, continue jugando")
                break
            else:
                print("Al ladron le queda", vida, "de vida")
        else:
            print("batalla vale", vida) #debug
            input("El ladron va a atacarte, presiona cualquier tecla para comenzar con la batalla!")
            resultado = random.randint(1, 2)
            print("El ladron te saco", resultado, "de vida y te quedan", vida, "de energía")
            #if vida > 0:

    conexion.close()