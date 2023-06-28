[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/I4ZLpAx7)
**Тьюториал: Оркестрация контейнеров с помощью Docker Compose в Django проекте**

Шаг 1: Установка Docker и Docker Compose
Если вы еще не установили инструменты, выполните их установку.
1. Установите Docker на вашу машину, следуя официальной документации Docker: https://docs.docker.com/get-docker/
2. Установите Docker Compose, инструмент для определения и управления многоконтейнерными приложениями, следуя официальной документации Docker Compose: https://docs.docker.com/compose/install/

Хорошо, предлагаю следующие шаги для создания виртуальной среды (virtual environment) и установки зависимостей с использованием venv:

Шаг 2: Клонирование проекта, cоздание виртуальной среды и установка зависимостей

1. Клонируйте репозиторий с проектом с помощью команды: 
   ```
   git clone <URL репозитория>
   ```
2. Перейдите в каталог вашего проекта: 
   ```
   cd myproject
   ```
3. Создайте новую виртуальную среду внутри вашего проекта с помощью следующей команды:
   ```
   python3 -m venv venv
   ```
4. Активируйте виртуальную среду. В зависимости от операционной системы, используйте одну из следующих команд:
   - Для Linux/Mac:
     ```
     source venv/bin/activate
     ```
   - Для Windows:
     ```
     venv\Scripts\activate
     ```
5. Установите зависимости проекта из файла requirements.txt с помощью команды:
   ```
   pip install -r requirements.txt
   ```
Теперь у вас есть виртуальная среда, созданная внутри вашего проекта, и в неё установлены все зависимости из файла requirements.txt. Вы можете продолжить работу с проектом и перейти к настройке Docker Compose.

Шаг 3: Настройка Docker Compose
1. Создайте файл `docker-compose.yml` в корневой директории вашего проекта.
2. Внутри файла `docker-compose.yml` определите сервисы, которые вы хотите запустить в контейнерах. Например, сервис базы данных PostgreSQL и сервис веб-сервера Django.
3. Определите настройки каждого сервиса, такие как порты, переменные окружения, примонтированные тома и т.д.

Шаг 4: Определение Dockerfile
1. Создайте файл `Dockerfile` в корневой директории вашего проекта.
2. Внутри файла `Dockerfile` определите инструкции для сборки образа вашего Django приложения. Например, указать базовый образ, скопировать код проекта, установить зависимости и т.д.

Шаг 5: Запуск контейнеров
1. В терминале перейдите в корневую директорию вашего проекта.
2. Запустите контейнеры, используя команду `docker-compose up`.
3. Docker Compose выполнит сборку образов, создаст и запустит контейнеры, и вы увидите вывод логов контейнеров.

Шаг 6: Проверка работоспособности
1. Откройте веб-браузер и перейдите по адресу `http://localhost:8000`.
2. Вы должны увидеть запущенное Django приложение.

## Использование автоматизированных тестов:

1. Автоматизированные тесты организованы в директории `products/tests`. В этой директории содержатся два файла тестов: `test_products.py` для юнит-тестов и `test_product_list.py` для UI-тестов.
2. Для запуска UI-тестов с использованием Selenium, в Docker-образ уже включен браузер Chrome.

```

RUN apt-get update \
    && apt-get install -y \
        python3-pip \
        chromium \
        chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

```

Если вам необходимо провести тестирование с другими браузерными движками, вы можете настроить их, добавив соответствующие менеджеры WebDriver и зависимости в `Dockerfile` или `requirements.txt`.

3. Организация тестов

  Файл `test_products.py` содержит юнит-тесты для модуля `products.py`. Здесь вы можете проверить отдельные функции, методы или классы вашего кода. 

В файле `test_products.py` заполнение тестовыми данными может осуществляться через fixtures.
Обычно фикстуры размещаются в отдельном файле для повторного использования в разных тестовых файлах.

Сначала создадим файл `conftest.py` и определим в нем фикстуру:

```python
import pytest
from products.models import Product

@pytest.fixture
import pytest
from django.core.management import call_command
from products.models import Product

@pytest.fixture(scope='session')
def init_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock(): 
        call_command('loaddata', "init_data.json") # данные для заполнения лежат в init_data.json
```

В файле `test_products.py` определим тесты, использующие фикстуру. Отметив pytest.mark.django_db мы указываем что для теста нужно использовать базу данных, он вызовет django_db_setup и init_data сам.  Например:

```python
@pytest.mark.django_db
def test_product_creation():
    # Здесь мы принимаем фикстуру `filled_database` в качестве аргумента теста
    # Фикстура автоматически заполнит базу данных тестовыми данными перед выполнением этого теста

    # Создаем новый продукт
    product = Product.objects.create(name='New Product', price=9.99, description='Test product', category='Test Category')

    # Проверяем, что продукт был успешно создан и сохранен в базе данных
    assert product.id is not None
    assert product.name == 'New Product'
    assert product.price == 9.99
    assert product.description == 'Test product'
    assert product.category == 'Test Category'
```

Теперь у нас есть отдельный файл с фикстурой, который будет заполнять базу данных тестовыми данными, и отдельный файл с тестом, который использует эту фикстуру для проверки создания продукта.

Чтобы фикстура работала укажите в pytest.ini ее имя и описание

```
markers =
    init_data: Заполнение тестовыми данными
```

При запуске Pytest автоматически найдет тесты, определенные в файлах, соответствующих шаблону `test_*.py`, и выполнит их. Фикстуры, определенные в `conftest.py`, будут автоматически использованы pytest при выполнении тестов.

4. UI-тестирование с Selenium

 Файл `test_product_list.py` содержит UI-тесты для проверки функциональности вашего Django-приложения. Здесь вы можете использовать Selenium для взаимодействия с веб-интерфейсом и проверки отображаемых элементов. Пример кода в файле `test_product_list.py` может выглядеть следующим образом:

```python
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestProductList:

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # для работы в headless режиме
        chrome_options.add_argument("--no-sandbox") #для работы внутри контейнера
        chrome_options.add_argument('--disable-dev-shm-usage')

        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
        cls.driver.get('http://localhost:8000/')

    @pytest.mark.django_db
    def test_product_card_exists(self):
        product_cards = self.driver.find_elements(By.CLASS_NAME, 'product-container')
        assert len(product_cards) > 0, 'No product cards found.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
```

5. Запуск pytest в контейнере Docker

При запуске pytest автоматически обнаруживает и выполняет все файлы, которые начинаются с `test_` и содержат функции с префиксом `test_`. Он ищет эти файлы и функции во всех директориях, начиная с текущей рабочей директории.

Чтобы запустить pytest в контейнере, убедитесь, что Docker-контейнер запущен с помощью `docker-compose up`.

Далее можно выполнить pytest с помощью 
```cmd
docker compose exec web pytest
```
Здесь web это имя django веб сервиса.