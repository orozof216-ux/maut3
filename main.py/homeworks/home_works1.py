import flet as ft

count = 0

def main(page: ft.Page):
    global count

    text_hello = ft.Text("Нажато: 0 раз")

    def on_click(e):
        global count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    page.add(
        text_hello,
        ft.ElevatedButton("Нажми меня", on_click=on_click)
    )

ft.app(target=main)