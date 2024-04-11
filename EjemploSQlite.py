import sqlite3
from EjemplosClases import Cliente

def IngresarDatos(Cliente):

    nombre = Cliente._nombre
    nombre_imagen = Cliente._nombre_imagen

    try:
        #Conexion a la base de datos
        conexion = sqlite3.connect("DB_mi_tienda.db")

        #Crear un cursor 
        cursor = conexion.cursor()

        #Ejecutar consulta en la base de datos
        cursor.execute("INSERT INTO Clientes (nombre, nombre_imagen) VALUES (?, ?)", (nombre, nombre_imagen))

        #Hacer commit para guardar datos en DB
        conexion.commit()

        #aviso que se realizo correctamente
        print("Exito!")
    
    except sqlite3.Error as error:
        print("No se pudo")

    finally:
        #Cerrar la conexion
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

