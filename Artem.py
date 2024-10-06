Основываемся на этой структуре
fastapi-project
├── alembic/
├── src
│   ├── auth
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── dependencies.py
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── aws
│   │   ├── client.py  # client model for external service communication
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   └── utils.py
│   └── posts
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── models.py  # global models
│   ├── exceptions.py  # global exceptions
│   ├── pagination.py  # global module e.g. pagination
│   ├── database.py  # db connection related stuff
│   └── main.py
├── tests/
│   ├── auth
│   ├── aws
│   └── posts
├── templates/
│   └── index.html
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini

Сохраните все доменные каталоги внутри srcпапки
src/- самый высокий уровень приложения, содержит общие модели, конфигурации, константы и т. д.
src/main.py- корень проекта, который инициализирует приложение FastAPI
Каждый пакет имеет свой собственный маршрутизатор, схемы, модели и т. д.
router.py- это ядро ​​каждого модуля со всеми конечными точками
schemas.py- для пидантических моделей
models.py- для моделей БД
service.py- бизнес-логика, специфичная для модуля
dependencies.py- зависимости маршрутизатора
constants.py- константы и коды ошибок, специфичные для модуля
config.py- например, переменные окружения
utils.py- функции, не относящиеся к бизнес-логике, например, нормализация ответа, обогащение данных и т. д.
exceptions.py- исключения, специфичные для модуля, например PostNotFound,InvalidUserData
