# api_final

### Описание:

API для Yatube сервиса

### Работа выполенена:

Соловей Никита Сергеевич https://github.com/TLS228

### Стек:

* Python 3.9.13
* Django
* Django REST framework
* Djoser + JWT

### Как установить и запустить проект:

1. Клонировать репозиторий в папку, и перейти в него написав в командной строке:

```
git@github.com:TLS228/api_yatube.git
```

```
cd api_final_yatube
```

2. Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/scripts/activate
```

3. Обновить pip и установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполнить миграции в проекте:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

5. Запустить проект командой:

```
python manage.py runserver
```
