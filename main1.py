import flet as ft

def main(page: ft.Page):
    page.title = "Проверка возраста"

    # поле ввода
    age_input = ft.TextField(label="Введите возраст")

    # текст результата
    result_text = ft.Text("")

    # функция проверки
    def check_age(e):
        age = age_input.value.strip()

        if age == "":
            result_text.value = "Введите корректный возраст"
            result_text.color = "yellow"

        elif age.isdigit():
            age_int = int(age)

            if age_int >= 18:
                result_text.value = "Доступ разрешен"
                result_text.color = "green"
            else:
                result_text.value = "Доступ запрещен"
                result_text.color = "red"

        else:
            result_text.value = "Введите корректный возраст"
            result_text.color = "yellow"

        page.update()

    # кнопка
    check_button = ft.ElevatedButton("Проверить", on_click=check_age)

    # добавляем на страницу
    page.add(age_input, check_button, result_text)

# запуск
ft.app(target=main)




