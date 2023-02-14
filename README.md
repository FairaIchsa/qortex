# Проект API для музыкального каталога
## Как запустить
### В командной строке

Клонировать репозиторий:
  
    git clone https://github.com/fairaichsa/qortex.git

Перейти в папку проекта и создать виртуальное окружение:

    cd qortex

    python -m venv venv

    venv\Scripts\activate.bat (Windows) или source venv/bin/activate (Unix, MacOS)
 
    pip install -r requirements.txt
    
Запустить:
    
    python manage.py runserver
    
## Swagger

Для работы с API через Postman нужно импортировать его по следующей ссылке:
    
    http://127.0.0.1:8000/download-api/
    (В Postman это делается через Import -> Link)
