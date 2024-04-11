import flet as ft
import EjemploSQlite as sq
from EjemplosClases import Cliente

def main(page: ft.Page):

    def pintarClientes():
        datos = sq.RecuperarDatos()
        for id, nombre, nombre_imagen in datos:
            page.add(
                ft.Row(
                    controls=[
                        ft.Text(nombre),
                        ft.Text(nombre_imagen)
                    ]
                )
            )
        page.update()

    def añadirCliente(e):
        nuevo_cliente = Cliente()
        if nuevo_cliente.set_nombre(recuadro_nombre.value) and nuevo_cliente.set_imagen(recuadro_imagen.value):
            sq.IngresarDatos(nuevo_cliente)
            page.add(ft.Text("Datos ingresados correctamente"))
        else:
            page.add(ft.Text("Datos incorrectos"))
        page.update()
    
    pintarClientes()

    recuadro_nombre = ft.TextField(
        hint_text="Ingresa el nombre del cliente"
    )

    recuadro_imagen = ft.TextField(
        hint_text="Ingresa el nombre de la imagen"
    )

    page.add(
        recuadro_nombre,recuadro_imagen,ft.ElevatedButton("Añadir nuevo cliente", on_click=añadirCliente)
    )

    

    
    

ft.app(target=main)