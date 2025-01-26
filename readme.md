## Инструкции по локальному запуску

1. Клонирование. Введите команду:
============================================
git clone https://github.com/Elbit27/maddevstt1.git
============================================

2. Перейдите в каталог проекта
После клонирования репозитория, перейдите в его директорию:
============================================
cd название_репозитория
============================================

3. Создайте виртуальное окружение, активируйте его и установите зависимости
============================================
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
============================================

4. Создайте файл .env и поместите туда:
============================================
SECRET_KEY=AJ9tVzrUeMXNCH65AhurV9SIULDNPgi4LL0K-6-6QeJAA8RLlShtdDnfILjke7tEBCE
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,
DB_NAME=mad_devs_tt1
DB_USER=elburs27
DB_PASSWORD=v58v5723
DB_HOST=localhost
DB_PORT=5432
============================================

5. Создайте базу данных подобную в .env файле (например mad_devs_tt1) и после создание проведите миграции с помощью
команды './manage.py makemigrations'.
6. Можно теперь запускать. Локально при помощи команды './manage.py runserver'. 
7. А запускается в докер контейнере при помощи команды 'sudo docker-compose up --build', Но перед запуском проекта в 
контейнере, в .env файле следует поменять значение переменной DB_HOST с 'localhost', на 'db'.