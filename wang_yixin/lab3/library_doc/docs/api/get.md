# Показать всех книги

Выводит информацию обо всех книгах

**URL** : `/books/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : 

```json
{
    "books": [
        {
            "id": 5,
            "book_name": "Harry Potter",
            "Type": "n",
            "year_of_pub": "2022-03-08",
            "author": 3
        },
        {
            "id": 1,
            "book_name": "How steel was tempered",
            "Type": "n",
            "year_of_pub": "2022-03-08",
            "author": 1
        },
        {
            "id": 4,
            "book_name": "People's Daily",
            "Type": "n",
            "year_of_pub": "2022-03-08",
            "author": null
        },
        {
            "id": 6,
            "book_name": "Python:from beginner to master",
            "Type": "t",
            "year_of_pub": "2022-03-08",
            "author": null
        },
        {
            "id": 2,
            "book_name": "Three bodies",
            "Type": "n",
            "year_of_pub": "2022-03-08",
            "author": 2
        },
        {
            "id": 3,
            "book_name": "Time",
            "Type": "m",
            "year_of_pub": "2022-03-08",
            "author": null
        }
    ]
}
```