class Cliente:

    def __init__(self, nombre="", nombre_imagen="") -> None:
        """
        La clase cliente recibe dos cadenas para el nombre del cliente y el nombre de su imagen
        """
        self._nombre = nombre
        self._nombre_imagen = nombre_imagen

    def set_nombre(self, nombre):
        """
        El nombre solo se asigna si es una cadena sin caracteres especiales ni numeros
        """
        if isinstance(nombre, str) and nombre.replace(" ","").isalpha():
            self._nombre = nombre.title()

    def set_imagen(self, nombre_imagen):
        """
        Todavia no sabemos las condiciones aqui, pero algún dia :3
        """
        self._nombre_imagen = nombre_imagen

class Producto:

    def __init__(self, nombre="", precio=0.0) -> None:
        """
        La clase producto recibe la cadena del nombre del producto y su precio.
        """
        self._nombre = nombre
        self._precio = precio

    def set_nombre(self, nombre):
        """
        El nombre solo se asigna si es una cadena sin caracteres especiales
        """
        if isinstance(nombre, str) and nombre.replace(" ","").isalnum():
            self._nombre = nombre.capitalize()

    def set_precio(self, precio):
        """
        El precio solo se asigna si es un número flotante mayor que cero
        """
        if isinstance(precio, float) and precio > 0.0:
            self._precio = float(precio)

