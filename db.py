import sqlite3


def crear_bd():
    conexion = sqlite3.connect('jugadores.db')
    cursor = conexion.cursor()

    cursor.execute('''Create table if not exists jugadores (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nombre varchar (15) NOT NULL,
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

    fila = [nombre, categoria, victorias, derrotas]
    cursor.execute("insert into jugadores values (null,?,?,?,?)", fila)

    conexion.commit()
    conexion.close()


