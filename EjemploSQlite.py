import sqlite3
from EjemplosClases import Cliente

def IngresarCliente(Cliente):
    try:
        #conecta con la base y crea el cursor
        conexion = sqlite3.connect("DB_mi_tienda.db")
        cursor = conexion.cursor()

        #Ejecuta la insercion de datos
        cursor.execute("INSERT INTO Clientes (nombre, nombre_imagen) VALUES (?, ?)", (Cliente._nombre, Cliente._nombre_imagen))
        conexion.commit()
        print("Exito!")
    
    #Si existe algun error con la base de datos nos avisa
    except sqlite3.Error as error:
        print("No se pudo, error:", error)

    #Se cierra la conexión
    finally:
        if conexion:
            conexion.close()

def EliminarCliente(nombre_cliente):
    try:
        #Conecta con la base y crea el cursor
        conexion = sqlite3.connect("DB_mi_tienda.db")
        cursor = conexion.cursor()

        #Busca el nombre del cliente en la base
        cursor.execute("SELECT nombre FROM Clientes WHERE nombre = ?", (nombre_cliente,))

        #Si encuentra el nombre del cliente procede a eliminar el registro
        if cursor.fetchall():
            cursor.execute("DELETE FROM Clientes WHERE nombre = ?", (nombre_cliente,))
            conexion.commit()
            print("Exito!")
            return True
        
        #Si no encuentra 
        else:
            print("No existe el cliente")
            return False

    #Si existe algun error con la base de datos nos avisa
    except sqlite3.Error as error:
        print("No se pudo, error:", error)
        return False

    #Se cierra la conexión
    finally:
        if conexion:
            conexion.close()

def RecuperarDatos():

    #Conexion a la base de datos
    conexion = sqlite3.connect("DB_mi_tienda.db")

    #Crear un cursor 
    cursor = conexion.cursor()

    #Ejecutar consulta en la base de datos
    cursor.execute("SELECT * FROM Clientes ORDER BY nombre")

    #Obtener los resultados de la consulta 
    registro_cliente = cursor.fetchall()

    #Cerrar la conexion
    conexion.close()

    return registro_cliente

