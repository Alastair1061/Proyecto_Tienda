import flet as ft

def main(page: ft.Page):

    def saludar(e):
        
        saludo = ft.Text("")
        saludo.value=f"Hola {nombre.value}"
        page.add(saludo)
        
        nombre.value=""
        nombre.focus()

        page.update()

    nombre = ft.TextField(
        hint_text="Ingresa tu nombre",
        on_submit=saludar,
    )

    page.add(nombre)

ft.app(target=main)