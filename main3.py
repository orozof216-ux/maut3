import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    greeting_text = ft.Text('История заполнения:')

    def text_name(e):
        name = text_input.value.strip()

        if name:
           text_hello.value = f"Привет! {name}"
           text_hello.color = ft.Colors.BLUE
           text_input.value = ""
           greeting_history.append(name)
           greeting_text.value = f'История приветсвия: \n' + "\n".join(greeting_history)

        else:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900

        page.update()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()


    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)


    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветсвия:"


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    main_object = ft.Row(
        controls=[text_input, btn, clear_button],
        alignment=ft.MainAxisAlignment.CENTER
        ) 

    page.add(text_hello, main_object, theme_btn, greeting_text)


ft.app(main_page, view=ft.AppView.WEB_BROWSER)