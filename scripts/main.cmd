# меняет "директорию" на предыдущую, т.к. мы находимся в папке "scripts"

cd ..\

# обновляет "глобально" версию пакетов pip
python.exe -m pip install --upgrade pip

# устанавливает "глобально" библиотеку для создания виртуальных окружений
pip install env

# создаёт виртуальное окружение
python -m venv env

# активация виртуального окружения
call .\env\Scripts\activate.bat

# обновляет "локально" версию пакетов pip
pip install --upgrade pip



# "построчно" читает данные с файла и устанавливает эти библиотеки в активированное виртуальное окружение
pip install -r requirements.txt

# "замораживает" установленные библиотеки из виртуального окружения
pip freeze > requirements.txt



# устанавливает в виртуальное окружение библиотеки "Django" и pillow(для работы с изображениями) установленные библиотеки из виртуального окружения
pip install django
pip install pillow

# создание Django-проекта с именем "settings" в этой же директории
django-admin startproject settings .
# или для удобства названия django-admin startproject backend_settings . 


# создание Django-приложение с именем "app_second" в этой же директории
django-admin startapp app_second

# создание миграций к базе данных
python manage.py makemigrations

# применение миграций к бд
python manage.py migrate

# Создание суперпользователя
# python manage.py createsuperuser
python manage.py createsuperuser --username temir --email temir@gmail.com



# сбор статических файлов
python manage.py collectstatic --noinput


# запускает "development"(сервер для разработки) 0.0.0.0:88
python manage.py runserver 127.0.0.1:8000



# для реакта
# добавить для обращения в backend на фронте в package.json "proxy": "http://127.0.0.1:8000",  
https://github.com/bogdandrienko?tab=repositories
https://www.youtube.com/playlist?list=PLFH0jFGRecS0btzEqlp6f4Ua8FwJYkH1m




14.07.22 отправка писем, многопоточность итд
15.07.22 создаём заново приложение django и react парсинг многопоточность



роутинг react https://www.youtube.com/watch?v=0auS9DNTmzE&list=TLPQMTYwNzIwMjJdHYJAkUWCpg&index=4


питон основы https://www.youtube.com/watch?v=Lw8TeLS4_IA&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=3
https://www.youtube.com/watch?v=78PTvj2wYH8&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=6 остановился



# 1 вопросы 
картинки сохранение и вывод
