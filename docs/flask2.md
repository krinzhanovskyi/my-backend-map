# Теория: Шаблоны и статические файлы во Flask

Давай сперва разберём немного теории. Это нужно, чтобы ты понимал, что происходит «под капотом», прежде чем начнёшь писать код.

### Шаблоны (Jinja2)

Flask использует шаблонизатор Jinja2. Проще говоря, ты отделяешь HTML-код от кода на Python. В итоге у тебя есть специальная папка с шаблонами, где ты пишешь HTML, а данные подставляешь уже из Python-кода.

**Основные моменты:**

1. **Папка `templates`:**  
   Создай папку `templates` в корне своего проекта. Flask по умолчанию будет искать шаблоны именно там.

2. **Создание шаблона:**  
   Внутри папки `templates` ты можешь сделать, например, файл `index.html` и использовать в нём специальный синтаксис `{{ }}` для вывода переменных. Например:
   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
   Если ты передашь в шаблон переменную `name='Flask User'`, на странице отобразится «Hello, Flask User!».  
   (Пример выше — просто иллюстрация. В дальнейшем мы будем использовать другие значения.)

3. **Динамические данные:**  
   Для вывода динамических данных ты используешь двойные фигурные скобки `{{ }}`. Всё, что передашь в шаблон с помощью `render_template`, сможешь потом отобразить в HTML.

### Статические файлы

Помимо HTML и данных, тебе нужны стили, скрипты и изображения. Эти файлы не меняются от запроса к запросу, поэтому их называют статическими.

1. **Папка `static`:**  
   Создай папку `static` для хранения CSS, JS и изображений.

2. **Подключение статических файлов:**  
   Чтобы подключить статический файл, например `style.css`, в шаблоне напиши:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   ```

### Передача переменных с помощью `render_template`

Функция `render_template` позволяет рендерить (отображать) шаблон и передавать в него переменные. Пример:
```python
return render_template('index.html', name='Sancho')
```
Затем в шаблоне `index.html` ты можешь написать `{{ name }}`, и на странице будет выведено значение `'Sancho'`.

---

# Практика: Пошаговые действия

У тебя уже есть файл `app.py` со следующим содержимым:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Sho ty, Golova!"

if __name__ == '__main__':
    app.run(debug=True)
```

При переходе на `http://127.0.0.1:5000/` ты сейчас увидишь просто «Sho ty, Golova!». Давай это изменим, чтобы вернуть шаблон с динамическими данными.

### Шаг 1: Создай папку `templates` и добавь `index.html`

1. В корневой директории проекта создай папку `templates`.
2. Внутри неё создай файл `index.html`.

Пример `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is FuckinG Flask Page</title>
</head>
<body>
    <h1>Bonjour, {{ name }}!</h1>
    <p>Welcome to Hell.</p>
</body>
</html>
```

Обрати внимание, что в `<h1>` есть `{{ name }}`, куда мы позже подставим значение.

### Шаг 2: Подключи шаблон к маршруту `/`

Обновим `app.py`, чтобы маршрут `/` возвращал наш шаблон и подставлял значение `'Sancho'`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Передаём шаблону переменную name='Sancho'
    return render_template('index.html', name='Sancho')

if __name__ == '__main__':
    app.run(debug=True)
```

Перезапусти приложение (или оно перезапустится само, если у тебя включён режим отладки). Перейди на `http://127.0.0.1:5000/`, и теперь ты увидишь страницу с заголовком «Bonjour, Sancho!».

### Шаг 3: Добавь папку `static` и файл `style.css`

1. Создай в корне проекта папку `static`.
2. Внутри `static` сделай файл `style.css`:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
}
```

### Шаг 4: Подключи CSS к шаблону

В `index.html` в `<head>` добавь ссылку на CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is FuckinG Flask Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Bonjour, {{ name }}!</h1>
    <p>Welcome to Hell.</p>
</body>
</html>
```

Перезагрузи страницу. Теперь фон страницы светло-серый, а заголовок имеет другой цвет.

### Шаг 5: Создай новый шаблон `about.html` и маршрут `/about`

1. В папке `templates` сделай файл `about.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Page</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>About {{ project_name }}</h1>
    <p>This is a stupid Flask application created to learn templates and static files.</p>
</body>
</html>
```

2. В `app.py` добавь маршрут:

```python
@app.route('/about')
def about():
    return render_template('about.html', project_name='Fucking Flusk')
```

Перейди на `http://127.0.0.1:5000/about`, и ты увидишь страницу «About Fucking Flusk».

---

# Итог

Поздравляю! Теперь ты знаешь, как:

- Создавать и использовать HTML-шаблоны с динамическими данными.
- Организовывать шаблоны в папке `templates`.
- Подключать статические ресурсы (CSS, JS, изображения) из папки `static`.
- Работать с `render_template` и `url_for` для удобной и аккуратной разработки.

Ты получил базовые знания, чтобы двигаться дальше: подключать базы данных, работать с формами, аутентификацией и многим другим. Теперь у тебя есть фундамент для построения полноценных веб-приложений!
