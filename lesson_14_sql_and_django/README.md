# Урок 14 "SQL и Django"

## SQL

Продолжаем практиковаться в sql. Любой желающий получит доступ к выделенной собственной БД доступной из интернета и сможет выполнить задания.
Нужно создать БД для хранения следующих моделей:
*Рабочие*
* id
* имя
* фамилия
* статус (новый, работает, удалён)
* дата и время создания
* баланс

*Контакты рабочих*
* id рабочего
* тип контакта (телефон, эл. почта)
* контакт

*Адреса рабочих*
* id рабочего
* индекс
* регион
* город
* улица
* дом
* квартира

*Учет рабочего времени*
* id рабочего
* дата и время
* тип события (приход и уход)

## Django
Читаем девчячий ресурс https://tutorial.djangogirls.org/ru/
Если стрёмно, находим любой другой. Цель: знать как создать проект и в нем одну страницу.