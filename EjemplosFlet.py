import flet as ft
import EjemploSQlite as sq
from EjemplosClases import Cliente

def main(page: ft.Page):

    clientes = ft.Column()

    def actualizarClientes():
        clientes.controls.clear()
        datos = sq.RecuperarDatos()
        for id, nombre, nombre_imagen in datos:
            clientes.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(nombre),
                        ft.Text(nombre_imagen)
                    ]
                )
            )
        clientes.update()

    page.add(clientes)
    actualizarClientes()

    recuadro_nombre = ft.TextField(
        hint_text="Ingresa el nombre del cliente"
    )

    recuadro_imagen = ft.TextField(
        hint_text="Ingresa el nombre de la imagen"
    )

    def añadirCliente(e):
        nuevo_cliente = Cliente()
        if nuevo_cliente.set_nombre(recuadro_nombre.value) and nuevo_cliente.set_imagen(recuadro_imagen.value):
            sq.IngresarCliente(nuevo_cliente)
            page.add(ft.Text("Datos ingresados correctamente"))
        else:
            page.add(ft.Text("Datos incorrectos"))
        
        actualizarClientes()
        page.update()

    page.add(
        recuadro_nombre,recuadro_imagen,ft.ElevatedButton("Añadir nuevo cliente", on_click=añadirCliente)
    )

    eliminar_cliente = ft.TextField(
        hint_text="Ingresa el nombre del cliente a eliminar"
    )

    def eliminarCliente(e):
        if sq.EliminarCliente(eliminar_cliente.value):
            page.add(ft.Text("Cliente eliminado"))
        else:
            page.add(ft.Text("No se pudo"))
        
        actualizarClientes()
        page.update()

    page.add(
        eliminar_cliente, ft.ElevatedButton("Eliminar cliente", on_click=eliminarCliente)
    )

ft.app(target=main)