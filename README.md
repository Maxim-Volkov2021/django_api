# django_api
<h1>Новини</h1>
/api/v1/news/ GET — виводить список новин з пагінацією.<br>
Приклад відповіді (json):<br>
{<br>
"count": кількість новин на сайті (integer),<br>
"next": силка наступної сторінка (string, або null якщо сторінки не існує),<br>
"previous":  силка попередньої сторінка (string, або null якщо сторінки не існує),<br>
"results": [<br>
{<br>
"id": id новини (integer),<br>
"title": заголовок новини (string),<br>
"content": контент новини (string),<br>
"timeCreate": дата створення новини (приклад: "2023-07-02T23:25:21.994787Z"),<br>
"author": id автора новини (integer),<br>
"tags": [<br>
список id тегів цієї новини (integers)<br>
],
"archive": показує чи архівна це новина, тільки автор може бачити свої архівні новини (boolean)<br>
},<br>
{<br>
...<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/news/”id news”/ GET — виводить новину по id (integer).<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/1/<br>
<br>
Приклад відповіді (json):<br>
{<br>
"id": id новини (integer),<br>
"title": заголовок новини (string),<br>
"content": контент новини (string),<br>
"timeCreate": дата створення новини (приклад: "2023-07-02T23:25:21.994787Z"),<br>
"author": id автора новини (integer),<br>
"tags": [<br>
список id тегів цієї новини (integers)<br>
],<br>
"archive": показує чи архівна це новина, тільки автор може бачити свої архівні новини (boolean)<br>
}<br>
<hr>
/api/v1/news/ POST — додавання новини на сайт. Можуть додавати новини тільки авторизовані користувачі що є авторами на сайті або адміни(автор буде null).<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ <br>
json - {<br>
"title": "test news",<br>
"content": "test news content",<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
}<br>
Приклад відповіді (json):<br>
{<br>
"id": 11,<br>
"title": "test news",<br>
"content": "test news content",<br>
"timeCreate": "2023-07-13T15:47:17.673925Z",<br>
"author": 1,<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
}<br>
<hr>

api/v1/news/”id news”/ PUT or PATCH — оновлює новину по id (integer), доступно тільки автору чи адміністратору сайту.<br>
*автор це авторизований користувач, який створив цю новину.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/1/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ <br>
json - <br>
{<br>
"title": "test title",<br>
"content": "test content",<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
}<br>
<br>
Приклад відповіді (json):<br>
{<br>
"id": 1,<br>
"title": "test title",<br>
"content": "test content",<br>
"timeCreate": "2023-05-08T13:25:20.192419Z",<br>
"author": 1,<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
}<br>
<hr>
/api/v1/news/”id news”/ DELETE — видаляє новину по id (integer), доступно тільки автору чи адміністратору сайту.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/1/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ <br>

<hr>
<h1>Теги</h1>
/api/v1/news/tags/ GET — виводить теги з пагінацією.<br>
Приклад відповіді (json):<br>
{<br>
"count": кількість тегів на сайті (integer),<br>
"next": силка наступної сторінка (string, або null якщо сторінки не існує),<br>
"previous":  силка попередньої сторінка (string, або null якщо сторінки не існує),<br>
"results": [<br>
{<br>
"id": id тегу (integer),<br>
"name": ім’я тегу (string)<br>
},<br>
{<br>
...<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/news/”id tag”/tag/  GET - виводить тег по id (integer).<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/1/tag/<br>
<br>
Приклад відповіді (json):<br>
{<br>
"count": кількість тегів на сайті (integer),<br>
"next": силка наступної сторінка (string, або null якщо сторінки не існує),<br>
"previous":  силка попередньої сторінка (string, або null якщо сторінки не існує),<br>
"results": [<br>
{<br>
"id": id тегу (integer),<br>
"name": ім’я тегу (string)<br>
}<br>
]<br>
}<br>
<hr>
<h1>Автори</h1>
/api/v1/news/authors/ GET — виводить авторів з пагінацією.<br>
Приклад відповіді (json):<br>
{<br>
"count": кількість авторів на сайті (integer),<br>
"next": силка наступної сторінка (string, або null якщо сторінки не існує),<br>
"previous":  силка попередньої сторінка (string, або null якщо сторінки не існує),<br>
"results": [<br>
{<br>
"id": id автору (integer),<br>
"name": псевдонім автора (string)<br>
},<br>
{<br>
...<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/news/”id author”/author/  GET - виводить автора по id (integer).<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/1/author/<br>

Приклад відповіді (json):<br>
{<br>
"count": кількість авторів на сайті (integer),<br>
"next": силка наступної сторінка (string, або null якщо сторінки не існує),<br>
"previous":  силка попередньої сторінка (string, або null якщо сторінки не існує),<br>
"results": [<br>
{<br>
"id": id автора (integer),<br>
"name": псевдонім автора (string)<br>
}<br>
]<br>
}<br>
<hr>
<h1>Пошук</h1>
Пошук виконується GET запитом з параметром “query”. Запит виконується певним чином, спочатку виконується параметр “OR” тільки потім “AND”, що дає більше можливостей для пошуку. Обов’язковим є пробіл з початку і в кінці параметру “OR” та “AND”. Також є два варіанти пошуку по полям, прямий пошук визначається знаком “:”(запит “title:hello”, виведе запис в якому буде заголовок “hello” і не буде виводить записи з заголовком “hello 1” чи “hello Alex”) та не прямий пошук “~”(запит “title~hello”, виведе запис в якому буде заголовок “hello”, “hello 1”, “hello Alex” чи інші де в заголовку буде слово “hello”).<br>
<br>
/api/v1/news/search/ GET — пошук по новинам.<br>
Поля для пошуку: <br>
id — номер новини;<br>
title — заголовок новини;<br>
content — контент новини;<br>
author.id — id автора;<br>
author.name — псевдонім автора;<br>
tags.id — id тегу;<br>
tags.name — ім’я тегу.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/search/?query=title:test 1 OR title:test 23 AND content:test 001.5 OR title:test 12<br>
Приклад відповіді (json):<br>
{<br>
"count": 1,<br>
"next": null,<br>
"previous": null,<br>
"results": [<br>
{<br>
"id": 6,<br>
"title": "test 1",<br>
"content": "test 001.5",<br>
"timeCreate": "2023-05-10T16:30:20.371473Z",<br>
"author": 1,<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/news/tags_search/ GET — пошук по тегам.<br>
Поля для пошуку: <br>
id — номер тегу;<br>
name — ім’я тегу.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/tags_search/?query=name~t AND id:2<br>
Приклад відповіді (json):<br>
{<br>
"count": 1,<br>
"next": null,<br>
"previous": null,<br>
"results": [<br>
{<br>
"id": 2,<br>
"name": "test 2"<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/news/authors_search/ GET — пошук по авторам.<br>
Поля для пошуку: <br>
id — номер автора;<br>
name — псевдонім автора.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/authors_search/?query=name~us<br>
Приклад відповіді (json):<br>
{<br>
"count": 2,<br>
"next": null,<br>
"previous": null,<br>
"results": [<br>
{<br>
"id": 18,<br>
"name": "user1"<br>
},<br>
{<br>
"id": 2,<br>
"name": "user_02"<br>
}<br>
]<br>
}<br>
<hr>
<h1>Авторизація</h1>
Авторизація проходить токенами JWT."access" токен використовується для доступу до сторінок сайту на якому це потрібно. "refresh" токен використовується для поновлення "access" токену.<br>
<br>
/api/token/ POST — авторизація користувачів. Параметри передаються в json форматі “username” — ім’я користувача, “password” — пароль користувача.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/token/<br>
json - {<br>
"username": "root",<br>
"password": "1234"<br>
}<br>
Приклад відповіді (json):<br>
{<br>
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTM0NTg2MCwiaWF0IjoxNjg5MjU5NDYwLCJqdGkiOiI3NzllZWZmNjBiYWU0NzE1OThiM2I1ZjQ4Y2E5YTE5OSIsInVzZXJfaWQiOjF9.JAKTOFdkHVH8eAmv9crr-d5hQYAUvO7UIwzsqS5xOsI",<br>
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYwMzYwLCJpYXQiOjE2ODkyNTk0NjAsImp0aSI6IjAzMTkwNGNkMzAwNTRjY2ZiNTQxZjAyZDYyZWMzMDc0IiwidXNlcl9pZCI6MX0.moTICw9khiHdD4U7idLzR_XjLDo7bMl9AbU1KzXeO7g"<br>
}<br>
<br>
<hr>
/api/token/refresh/ POST — поновлення "access" токену за допомогою "refresh" токену що видається після авторизації. "refresh" токен можна використовувати повторно.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/token/refresh/<br>
json - {<br>
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTM0NTg2MCwiaWF0IjoxNjg5MjU5NDYwLCJqdGkiOiI3NzllZWZmNjBiYWU0NzE1OThiM2I1ZjQ4Y2E5YTE5OSIsInVzZXJfaWQiOjF9.JAKTOFdkHVH8eAmv9crr-d5hQYAUvO7UIwzsqS5xOsI"<br>
}<br>
Приклад відповіді (json):<br>
{<br>
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYwMzg4LCJpYXQiOjE2ODkyNTk0NjAsImp0aSI6ImNmNGYwNGJhYzFhZDQwODA4ZDM0Mjg0MzgwMDhiNzc0IiwidXNlcl9pZCI6MX0.z1wqvhwCEI8e6-6XV23QRsMje9DfIvpy5xRYo5AeXTs"<br>
}<br>
<hr>
/api/register/ POST — регістрація користувачів на сайті.<br>
Обов’язкові поля:<br>
"username" — ім’я користувача, повинно бути унікальним(string);<br>
"password": - пароль користувача(string);<br>
"first_name": - ім’я людини(string);<br>
"last_name": - прізвище людини(string);<br>
"email": - електрона пошта користувача(string).<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/register/<br>
json - {<br>
"username": "test_useR03",<br>
"password": "hjh7p;g76534SgHH",<br>
"first_name": "user",<br>
"last_name": "03",<br>
"email": "email_user03@test.com"<br>
}<br>
Приклад відповіді (json):<br>
{<br>
"user": {<br>
"username": "test_useR03",<br>
"first_name": "user",<br>
"last_name": "03"<br>
},<br>
"message": "User Created Successfully. Now perform Login to get your token"<br>
}<br>
<hr>
<h1>Профіль</h1>
<br>
/api/account/profile/ GET — переглянути всій профіль на сайті, доступно тільки авторизованим користувачам.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/account/profile/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ <br>
Приклад відповіді (json):<br>
{<br>
"account": {<br>
"username": "test_useR02",<br>
"first_name": "user",<br>
"last_name": "02",<br>
"email": "email_user02@test.com",<br>
"is_author": true,<br>
"author_id": 2,<br>
"author_name": "user_02"<br>
}<br>
}<br>
"is_author" — показує чи користувач є автором на цьому сайті, тобто може створювати новини що будуть бачити всі користувачі та гості сайту(boolean).<br>
"author_id" — якщо користувач є автором, то йому показується свій номер автора(integer).<br>
"author_name" - якщо користувач є автором, то йому показується свій псевдонім автора(string).<br>
Якщо користувач не є автором йому показується наступне(json):<br>
{<br>
"account": {<br>
"username": "test_useR02",<br>
"first_name": "user",<br>
"last_name": "02",<br>
"email": "email_user02@test.com",<br>
"is_author": false,<br>
"application_to_become_an_author": false<br>
}<br>
}<br>
"application_to_become_an_author" — показує чи користувач подав заявку на авторство(boolean).<br>
<hr>
/api/v1/news/my/ GET — переглянути свої новини, доступно авторизованому користувачу, який є автором на сайті.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/news/my/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ <br>
Приклад відповіді (json):<br>
{<br>
"count": 3,<br>
"next": null,<br>
"previous": null,<br>
"results": [<br>
{<br>
"id": 1,<br>
"title": "test",<br>
"content": "test 001.1",<br>
"timeCreate": "2023-05-08T13:25:20.192419Z",<br>
"author": 1,<br>
"tags": [<br>
1<br>
],<br>
"archive": false<br>
},<br>
...<br>
]<br>
}<br>

<hr>
<h1>Заявки на авторство</h1>
/api/v1/author/new/ POST — створення тестової новини щоб адміністратори сайту могли оцінити ваші навички та додати вас до авторів. Доступно авторизованим користувачам які не є автором.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/author/new/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ<br>
json - {<br>
"title": "test news",<br>
"content": "test news content",<br>
"tags": [<br>
1, 2<br>
],<br>
"nameAuthor": "test"<br>
}<br>
Приклад відповіді (json):<br>
{<br>
"id": 2,<br>
"title": "test news",<br>
"content": "test news content",<br>
"timeCreate": "2023-07-13T16:04:13.746976Z",<br>
"user": 4,<br>
"tags": [<br>
1,<br>
2<br>
],<br>
"nameAuthor": "test"<br>
}<br>
"nameAuthor" — ім’я автора що має бути унікальним.<br>
<hr>
/api/v1/author/new/ GET — переглянути список заявок на авторство. Доступно тільки адміністраторам сайту.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/author/new/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ<br>
Приклад відповіді (json):<br>
{<br>
"count": 1,<br>
"next": null,<br>
"previous": null,<br>
"results": [<br>
{<br>
"id": 2,<br>
"title": "test news",<br>
"content": "test news content",<br>
"timeCreate": "2023-07-13T16:04:13.746976Z",<br>
"user": 4,<br>
"tags": [<br>
1,<br>
2<br>
],<br>
"nameAuthor": "test"<br>
}<br>
]<br>
}<br>
<hr>
/api/v1/author/new/”id news”/ GET — переглянути заявку на авторство за певним номер. Доступно тільки адміністраторам сайту.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/author/new/2/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ<br>
Приклад відповіді (json):<br>
{<br>
"id": 2,<br>
"title": "test news",<br>
"content": "test news content",<br>
"timeCreate": "2023-07-13T16:04:13.746976Z",<br>
"user": 4,<br>
"tags": [<br>
1,<br>
2<br>
],<br>
"nameAuthor": "test"<br>
}<br>
<hr>
/api/v1/author/new/”id news”/ DELETE — видаляє заявку певного номеру. При видаленні можна дати користувачу авторство, якщо “lamp” буде зі значенням true — створюється автор та додається новина для перегляду користувачам та гостям сайту. Якщо значення “lamp” буде false — заявка видаляється і користувач має право подати заявку знову. Доступно тільки адміністраторам.<br>
Приклад запиту:<br>
url - http://127.0.0.1:8000/api/v1/author/new/2/<br>
header — Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MjYyNTAwLCJpYXQiOjE2ODkyNjE2MDAsImp0aSI6IjI2MzkzOGVhMjQzOTQ0N2NhMjdmYjNhOGQ0ZmIyNzM5IiwidXNlcl9pZCI6NH0.MyZ6Z-VyqcccFjUKikHHpivKUkz9mOOxO4_DMObrnKQ<br>
json - {<br>
"lamp": true<br>
}<br>
or<br>
{<br>
"lamp": false<br>
}<br>
