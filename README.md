# DjangoProjectCalendar
MyCalendar

1. napisz model
2. stwórz migracje
3. podepnij modele by były widoczne w adminie
4. ogranicz widoczność zbędnych pól w adminie
5. stwórz widoki frontendowe dla zarządzania modelami
6. ogranicz widoczność zbędnych pól we frontendzie
7. "autoryzacja (po stronie aplikacji www)"
8. Celery
9. RESTful api
10. uwierzytelnianie dla api

Some commands:

create project:
./manage.py startproject NazwaProjektu ~/Dokumenty/PYTHON/project-repo

create app:
./manage.py startapp NazwaAplikacji

create admin:
./manage.py createsuperuser

create migration after writing models:
./manage.py makemigrations

apply those migrations:
./manage.py migrate

previous migrations info:
./manage.py showmigrations

server:
./manage.py runserver [port]

python shell:
./manage.py shell