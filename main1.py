age = input("Введите возраст: ").strip()

if age == "":
    print("\033[33mВведите корректный возраст\033[0m")

elif age.isdigit():
    age = int(age)

    if age >= 18:
        print("\033[32mДоступ разрешен\033[0m")
    else:
        print("\033[31mДоступ запрещен\033[0m")

else:
    print("\033[33mВведите корректный возраст\033[0m")