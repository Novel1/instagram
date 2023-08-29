INSTAGRAM
---

# Описание
Разработан instagram в формате web-приложения

---
# Запуск проекта
## Инструкция по запуску проекта:

1. Создать или открыть папку куда будет копироваться проект
2. Открыть папку и прописать команду git clone (url github)
3. Перейти в появившуюся папку и открыв терминал, создать виртуальное окружение командой virtualenv venv -p python
4. Активировать виртуальное окружение . venv/bin/activate
5. Установите зависимости командой pip install -r requirements.txt
6. Загрузите фикстуры командой python3 manage.py loaddata fixtures/users.json, python3 manage.py loaddata fixtires/dump.json
7. Делаем миграцию командой ./manage.py migrate
8. И запустите приложение командой ./manage.py runserver

---


