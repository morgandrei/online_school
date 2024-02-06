Этот проект предназначен для демонстрации работы джанго-проекта сайта онлайн-школы через Postman и Docker

Для запуска проекта необходимо установить и запустить DockerDesktop по инструкции по ссылке https://docs.docker.com/engine/install/

Загрузите на локальную машину контейнеры:

  - База данных PostgreSQL, команда docker pull postgres:latest
  - Инструмент кэширования Redis, команда docker pull redis
  - Планировщик асинхронных задач Celery, команда docker pull celery

Создайте пользователя базы данных PostgreSQL c паролем, команда docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest
где postgres - имя пользователя БД, mysecretpassword - пароль к БД.

Подключитесь к базе данных командой docker exec -it postgres psql - postgres -d postgres

Создайте базу данных online_school внутри контейнера командой create database online_school

Соберите образ командой docker-compose build

Запустите проект командой docker-compose up
