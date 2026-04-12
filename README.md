# Django Comments

Система коментарів з вкладеними відповідями та прикріпленням файлів.

Зробив базові речі: валідацію, безпеку, роботу з файлами і трохи фронтенду.

---

## Що є в проєкті

* створення коментарів
* відповіді на коментарі (вкладене дерево)
* пагінація (25 записів)
* сортування (username, email, дата)
* preview повідомлення без перезавантаження (AJAX)
* captcha

### Файли

* картинки (jpg/png/gif)
* txt файли

Обмеження:

* зображення автоматично зменшуються до 320x240
* txt файли до 100kb

---

## Безпека

* HTML через bleach (щоб не було XSS)
* Django ORM (без SQL інʼєкцій)
* базова валідація форм

---

## Технології

* Django
* SQLite
* трохи JavaScript (AJAX)
* Pillow (для зображень)

---

## Як запустити

Склонуй репозиторій:

```bash id="y5s1w9"
git clone https://github.com/RToister/django-comments.git
cd django-comments
```

Створи віртуальне середовище:

```bash id="0c7q3k"
python -m venv venv
```

Активуй:

```bash id="l6qz6h"
venv\Scripts\activate
```

Встанови залежності:

```bash id="i8n1m3"
pip install -r requirements.txt
```

Міграції:

```bash id="e1n5x2"
python manage.py migrate
```

Запуск:

```bash id="p9k4a7"
python manage.py runserver
```

Відкрити:

```id="m8x2q1"
http://127.0.0.1:8000/
```

---

## Структура

```id="b2d9x4"
comments/       основна логіка
templates/      шаблони
media/          файли користувачів
test_project/   налаштування Django
```

---

## Реалізації

* вкладені коментарі через self ForeignKey
* обробка файлів прямо в моделі (resize + перевірки)
* дозволені HTML теги: a, code, i, strong
* використовую black + flake8 + pre-commit


---

## Автор

https://github.com/RToister


