# USETECH hackathon case 3

## Описание
**Сервис позволяющий создавать пользователей и предоставлять им доступ к эндпоинтам по токену. Основной целью является создание независимой утилиты для обработки токенов и предоставления доступа, которая может встраиваться в любую систему**

Реализованный функционал: Создание пользователся, предоставление доступа к эндпоинту для пользователя по токену, генерация JWT ключей через keycloak.

## Как работать с проектом:
1. **Устанавливаем и активируем venv**

   ```bash
    python -m venv venv
    python3 -m pip install --upgrade pip
    source venv/Scripts/activate
    pip install -r 'requirements.txt'
   ``` 

2. **Устанавливаем Docker и Docker Compose:**


3. **Клонируем репозиторий:**
    ```bash
    git clone git@github.com:Mitsushidu/usetech-hackathon.git
    ```

4. **Создаем файл .env:**
    ```bash
    sudo nano .env
    ```
    **Заполняем его следующими данными:**
    ```
    SECRET_KEY=secret_key

    DB_VENDOR=POSTGRES
    DB_ADDR=postgres
    DB_DATABASE=keycloak
    DB_USER=keycloak
    DB_SCHEMA=public
    DB_PASSWORD=password
    KEYCLOAK_ADMIN=admin
    KEYCLOAK_ADMIN_PASSWORD=admin
    ```

5. **Запускаем контейнеры Docker**
    ```bash
    docker compose up
    ```

7. **Создаем пользователя в keycloak. Для этого переходим по ссылке localhost:8080, далее консоль администратора. Вводим логин и пароль сохраненные в .env. Далее создаем клиента, вписываем client_id и ставим галочку на client authenication. После чего переходим в профиль созданного клиента. Копируем client secret во вкладке credentials. Добавляем переменные в .env**
    ```
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    ```

8. **Получаем jwt-токен**
    ```bash
    python3 _gettoken.py
    ```

### Для проверки работоспособности используем api:

1. **Создаем миграции:**
    ```bash
    docker compose exec backend python manage.py migrate
    ```

2. **Создаём суперпользователя Django**
    ```
    docker compose exec backend python manage.py migrate
    ```

3. **Переходим в админ панель localhost:8000/admin и создаем там пользователя с client_id, добавляем эндпоинты для тестирования localhost:8000/service1 и localhost:8000/service2 и добавляем доступ пользователю к одному из эдпоинтов.**

4. **Отправляем запрос на оба эндпоинта, добавив в header jwt ключ  в формате jwt: your_jwt_key. В результате с эндпоинта, к которому есть доступ приходит код 200, а с другого код 403. Токен действует ограниченное время, поэтому если он истек, в ответе эндпоинта будет код 401**

## Технический стек:
* Django = 4.2.5
* djangorestframework = 3.14.0
* PyJWT = 2.8.0
* Postgres
* Docker


## Автор: mitsushidu