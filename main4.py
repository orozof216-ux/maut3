import flet as ft 
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorite_names = []
    last_name = ""

    greeting_text = ft.Text('История:')
    favorite_text = ft.Text('Избранные:')

    # загрузка
    try:
        with open("history.txt", "r") as f:
            greeting_history = [i.strip() for i in f]
            greeting_text.value = "История:\n" + "\n".join(greeting_history)
    except:
        pass

    def text_name(e):
        nonlocal last_name
        name = text_input.value.strip()

        if name:
            last_name = name
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE
            text_input.value = ""

            t = datetime.now().strftime("%H:%M")
            greeting_history.append(f"{name} ({t})")
            greeting_history[:] = greeting_history[-5:]

            with open("history.txt", "w") as f:
                f.write("\n".join(greeting_history))

            greeting_text.value = "История:\n" + "\n".join(greeting_history)

        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

        page.update()

    def thememode(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История:"
        open("history.txt", "w").close()
        page.update()

    def add_favorite(e):
        if last_name and last_name not in favorite_names:
            favorite_names.append(last_name)
            favorite_text.value = "Избранные:\n" + "\n".join(favorite_names)
        page.update()

    def filter_morning(e):
        greeting_text.value = "Утро:\n" + "\n".join(
            [i for i in greeting_history if int(i.split("(")[-1][:2]) < 12]
        )
        page.update()

    def filter_evening(e):
        greeting_text.value = "Вечер:\n" + "\n".join(
            [i for i in greeting_history if int(i.split("(")[-1][:2]) >= 12]
        )
        page.update()

    text_hello = ft.Text('Как тебя зовут?')
    text_input = ft.TextField(label='Имя', on_submit=text_name)
    btn = ft.ElevatedButton('send', on_click=text_name)

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    fav_button = ft.ElevatedButton('В избранное', on_click=add_favorite)
    morning_btn = ft.ElevatedButton('Утро', on_click=filter_morning)
    evening_btn = ft.ElevatedButton('Вечер', on_click=filter_evening)

    page.add(
        text_hello,
        ft.Row([text_input, btn, clear_button]),
        ft.Row([morning_btn, evening_btn, fav_button]),
        theme_btn,
        greeting_text,
        favorite_text
    )

ft.app(main_page, view=ft.AppView.WEB_BROWSER)