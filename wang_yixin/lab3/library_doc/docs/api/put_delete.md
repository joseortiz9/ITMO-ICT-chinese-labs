# Выполнение операций над книгой

Просматривайте конкретную информацию о книге, редактируйте или удаляйте ее с помощью api.

**URL** : `/books/<int:pk>/`

**Method** : `GET , PUT , DELETE`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : 


###GET
```
{
    "id": 10086,
    "book_name": "9981",
    "Type": "novel",
    "year_of_pub": "2022-03-11"
}
```
###PUT
```
{
    "id": 10086,
    "book_name": "NEW_NAME",
    "Type": "novel",
    "year_of_pub": "2022-03-11"
}
```
###DELETE
Обновление страницы после операции удаления дает следующий результат:

Book matching query does not exist.
