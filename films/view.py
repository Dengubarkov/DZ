def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):

        print("Действия с фильмами:")
        print("1 - Добавление фильма\n"
              "2 - Каталог фильмов\n"
              "3 - Просмотр определенного фильма\n"
              "4 - Удаление фильма")

        print("q - Выход из программы")
        user_answer = input("Выберите вариант действия: ")

        return user_answer

    @add_title("Добавление фильма")
    def add_user_film(self):
        dict_film = {
            "Название": None,
            "Жанр": None,
            "Режиссер": None,
            "Год выпуска": None,
            "Длительность": None,
            "Студия": None,
            "Актеры": None,
        }

        for key in dict_film:
            if key == "Длительность":
                dict_film[key] = input(f"Введите данные- {key} фильма в минутах: ")
            else:
                dict_film[key] = input(f"Введите данные- {key} фильма: ")

        return dict_film

    @add_title("Каталог фильмов:")
    def show_all_films(self, films):

        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")
    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film
    @add_title("Просмотр определенного фильма")
    def show_single_film(self, film):
        for key in film:
            if key == "Длительность":
                print(f"{key} фильма - {film[key]} минут")
            else:
                print(f"{key} фильма - {film[key]}")
    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self,user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма из каталога")
    def remove_single_film(self, user_title):
        print(f"Фильм {user_title} был удален из каталога")
    @add_title("Ошибка меню")
    def show_incorrect_answer_error(self, menu):
        print("Пункта меню {menu} не существует")


