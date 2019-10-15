import sqlite3


def crear_bd():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute('''Create table if not exists jugadores (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nombre varchar (15) unique,
                        categoria varchar (20) NOT NULL,
                        victorias INTEGER, 
                        derrotas INTEGER 
                        )
    ''')

    conexion.commit()
    conexion.close()


def agregar_jugador(nombre, categoria, victorias, derrotas):
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    try:
        fila = [nombre, categoria, victorias, derrotas]
        cursor.execute("insert into jugadores values (null,?,?,?,?)", fila)
    except sqlite3.IntegrityError:
        print("El usuario ya existe")

    conexion.commit()
    conexion.close()


def lista_jugadores():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()
    cursor.execute("select nombre from jugadores")

    jugadores = cursor.fetchall()
    list_jugadores = []
    for jugador in jugadores:
        list_jugadores.append(jugador[0])

    conexion.close()

    return list_jugadores