import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    text_hello = ft.Text('Как тебя зовут?', size=20)
    greeting_text = ft.Text('История приветствия:')

    text_input = ft.TextField(label='Ваше имя')

    # логика
    def text_name(e):
        name = text_input.value.strip()

        # 1. пустое
        if not name:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.YELLOW
            page.update()
            return

        # 2. только цифры
        if name.isdigit():
            text_hello.value = "Имя не может состоять из цифр!"
            text_hello.color = ft.Colors.RED
            page.update()
            return

        # 3. меньше 2 символов
        if len(name) < 2:
            text_hello.value = "Имя слишком короткое!"
            text_hello.color = ft.Colors.RED
            page.update()
            return

        # 4. повтор
        if name in greeting_history:
            text_hello.value = "Это имя уже в истории!"
            text_hello.color = ft.Colors.RED
            page.update()
            return

        # 5. добавление (бонус — вверх)
        greeting_history.insert(0, name)

        # лимит 5
        if len(greeting_history) > 5:
            greeting_history.pop()

        text_hello.value = f"Привет! {name}"
        text_hello.color = ft.Colors.GREEN

        text_input.value = ""

        greeting_text.value = "История приветствия:\n" + "\n".join(greeting_history)

        page.update()

    btn = ft.ElevatedButton('send', on_click=text_name)

    # тема
    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    # очистка
    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # верх (Row)
    top_row = ft.Row(
        controls=[theme_btn, clear_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # центр (Row)
    main_row = ft.Row(
        controls=[text_input, btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # вся страница (Column)
    layout = ft.Column(
        controls=[
            top_row,
            text_hello,
            main_row,
            greeting_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)


ft.app(main_page, view=ft.AppView.WEB_BROWSER)