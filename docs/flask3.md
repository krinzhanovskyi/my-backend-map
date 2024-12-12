# Теория: Улучшение работы с формами при помощи Flask-WTF и отправка писем через Flask-Mail

Теперь ты знаешь, как использовать шаблоны, статические файлы и базовые формы. Давай сделаем следующий шаг: подключим валидацию форм через **Flask-WTF** и добавим возможность отправлять письма с помощью **Flask-Mail**.

## Зачем это нужно?

- **Flask-WTF** упростит тебе жизнь при работе с формами:
  - Ты определяешь форму как класс и задаёшь поля и валидаторы.
  - Flask-WTF автоматически проверяет корректность данных, генерирует CSRF-токен для безопасности и позволяет легко отображать ошибки.

- **Flask-Mail** позволит отправлять письма, например, уведомления или обратную связь от пользователя, прямо из приложения:
  - Ты настраиваешь SMTP-сервер.
  - С помощью `mail.send()` отправляешь письмо с нужным текстом.

## Установка

Установи необходимые пакеты:
```bash
pip install flask-wtf flask-mail
```

---

# Практика: Пошаговые действия

Предположим, у тебя уже есть проект со следующей структурой:

```
project/
    app.py
    forms.py
    static/
        style.css
    templates/
        index.html
        feedback.html
```

В `index.html` уже используются шаблоны, например `{{ name }}`, а `feedback.html` будет содержать форму для обратной связи.

### Шаг 1: Определи форму с валидаторами в `forms.py`

Создай или обнови файл `forms.py`:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=50)])
    message = TextAreaField('Your Message', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Submit')
```

### Шаг 2: Настрой Flask-Mail и Flask-WTF в `app.py`

В `app.py` подключим Flask-Mail и настроим SMTP-сервер. Например, для тестов используем локальный SMTP-сервер или тестовый сервис.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Настройка почтового сервера (например, локальный тестовый сервер)
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html', name='Sancho')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Получаем данные формы
        name = form.name.data
        message = form.message.data

        # Формируем письмо
        msg = Message(subject="New Feedback",
                      sender="no-reply@example.com",
                      recipients=["notreal@example.com"])  
        
        msg.body = f"Name: {name}\nMessage: {message}"
        
        # Отправляем письмо
        mail.send(msg)

        return redirect(url_for('home'))
    return render_template('feedback.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

### Что здесь происходит?

1. **Инициализируем Flask-Mail:**  
   Настраиваем сервер, порт, TLS/SSL (если нужно). В примере используется локальный SMTP-сервер на `localhost:1025`.

2. **Работа с формой (Flask-WTF):**  
   - Создаём экземпляр `FeedbackForm`.
   - Проверяем `if form.validate_on_submit():` чтобы убедиться, что форма отправлена и данные корректны.
   - Если всё ок, извлекаем `name` и `message`.

3. **Отправка письма:**  
   - Создаём объект `Message`, указываем `subject`, `sender` и `recipients`.
   - В `msg.body` записываем текст письма.
   - Вызываем `mail.send(msg)` для отправки письма.

### Шаг 3: Обнови шаблон `feedback.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Leave your feedback, Sancho!</h1>
    <form method="POST">
        {{ form.csrf_token }}
        
        <div>
            {{ form.name.label }}<br>
            {{ form.name(size=30) }}
            {% if form.name.errors %}
                <ul>
                {% for error in form.name.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </div>

        <div>
            {{ form.message.label }}<br>
            {{ form.message(rows="5", cols="30") }}
            {% if form.message.errors %}
                <ul>
                {% for error in form.message.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        </div>

        {{ form.submit() }}
    </form>
</body>
</html>
```

### Шаг 4: Проверка работы

1. Запусти локальный SMTP-сервер для тестирования. Например:
   ```bash
   python -m aiosmtpd -n -l localhost:1025
   ```
   В другом терминале запусти приложение:
   ```bash
   python app.py
   ```
2. Перейди на `http://127.0.0.1:5000/feedback`.
3. Попробуй отправить пустую форму — увидишь ошибки.
4. Заполни данные корректно и отправь. Если используешь локальный SMTP-сервер, письмо будет отображено в терминале, где он запущен.

---

# Итог

Теперь ты знаешь, как:

- Использовать Flask-WTF для более удобной работы с формами, валидацией и защитой от CSRF.
- Отправлять письма через Flask-Mail, интегрируя функционал рассылки сообщений прямо из своего приложения.

Сочетание Flask-WTF и Flask-Mail делает твой код чище, безопаснее и функциональнее. Следующий этап — интеграция с базами данных, авторизацией, сложными логическими проверками, и построение полноценных веб-приложений, готовых к боевому использованию.
