****************
API документация
****************

GET: Получить предмет
=====================

.. http:get:: /api/item/(str:item_id)

    **Example request**:

    .. sourcecode:: http

      GET /api/item/23abc45 HTTP/1.1
      Host: example.com
      Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        {
            "name":     "Красное платье",
            "images":   ["12.jpg", "11.jpg"],
            "tags":     [],
            "cost":     1200,
            "category": "dresses"
        }


   :reqheader Accept:
   :resheader Content-Type:
   :statuscode 200: OK
   :statuscode 404: предмет с item_id не найден

GET: Получить предметы с категорией
===================================
.. http:get:: /api/items/(str:category)

    **Example request**:

    .. sourcecode:: http

        GET /api/items/dresses HTTP/1.1
        Host: example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        [
            {
                "name":     "Красное платье",
                "images":   ["red1.jpg", "red2.jpg"],
                "tags":     [],
                "cost":     12200,
                "category": "dresses"
            },
            {
                "name":     "Синее платье",
                "images":   ["blue1.jpg"],
                "tags":     ["new"],
                "cost":     14000,
                "category": "dresses"
            }
        ]


   :reqheader Accept:
   :resheader Content-Type:
   :statuscode 200: OK
   :statuscode 404: категория(category) не существует

GET: Получить список категорий
==============================

.. http:get:: /api/categories/

    **Example request**:

    .. sourcecode:: http

        GET /api/categories HTTP/1.1
        Host: example.com
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Vary: Accept
        Content-Type: application/json

        [
            {
                "name":     "clothes",
                "rus_name": "одежда",
                "sub_categories":
                [
                    {
                        "name": "dresses",
                        "rus_name": "платья",
                        "info": "Тут описание категории..."
                    },
                    {
                        "name": "skirts",
                        "rus_name": "юбки",
                        "info": "Тут описание категории..."
                    }
                ]
            }
            {
                "name":     "accessories",
                "rus_name": "аксессуары",
                "sub_categories":
                [
                    {
                        "name": "bags",
                        "rus_name": "сумки",
                        "info": "Тут описание категории..."
                    }
                ]
            }
        ]


    :statuscode 200: OK

POST: Создать предмет
=====================

.. http:post:: /api/item

    :form fields: список полей см. в модели ItemModel

    .. autoclass:: api.models.ItemModel
        :members:
        :undoc-members:

    **Example request**:

    .. sourcecode:: http

        POST /api/item HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "name":     "Красное платье",
            "images":   ["red1.jpg", "red2.jpg"],
            "tags":     [],
            "cost":     12200,
            "category": "dresses"
        }

    **Example response error**:

    .. sourcecode:: http

        HTTP/1.1 400 Bad request
        Vary: Accept
        Content-Type: application/json

        {
            "errors": "..."
        }

    :statuscode 201: CREATED
    :statuscode 400: Validation error


PUT: Изменить предмет
=====================

.. http:put:: /api/item/(str:item_id)

    :form fields: список полей см. в модели ItemModel

    .. autoclass:: api.models.ItemModel
        :members:
        :undoc-members:

    **Example request**:

    .. sourcecode:: http

        PUT /api/item/234abcd HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "name":     "Красное платье",
            "images":   ["red1.jpg", "red2.jpg"],
            "tags":     ["sale"],
            "cost":     12200,
            "sale_cost":10800,
            "category": "dresses"
        }

    :statuscode 204: UPDATED
    :statuscode 404: предмет с item_id не найден

DEL: Удалить предмет
====================

.. http:delete:: /api/item/(str:item_id)

    **Example request**:

    .. sourcecode:: http

        DELETE /api/item/234abcd HTTP/1.1
        Host: example.com

    :statuscode 204: UPDATED
    :statuscode 404: предмет с item_id не найден

POST: Создать категорию
=======================

.. http:post:: /api/category

    :form fields: список полей см. в модели CategoryModel

    .. autoclass:: api.models.CategoryModel
        :members:
        :undoc-members:

    **Example request**:

    .. sourcecode:: http

        POST /api/category HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "name":     "dresses",
            "rus_name":   "платья",
            "parent":     "clothes",
            "info":     "описание категории платья...",
        }

    **Example response error**:

    .. sourcecode:: http

        HTTP/1.1 400 Bad request
        Vary: Accept
        Content-Type: application/json

        {
            "errors": "..."
        }

    :statuscode 201: CREATED
    :statuscode 400: Validation error

PUT: Изменить категорию
=======================

.. http:put:: /api/category/(str:category)

    :form fields: список полей см. в модели CategoryModel

    .. autoclass:: api.models.CategoryModel
        :members:
        :undoc-members:

    **Example request**:

    .. sourcecode:: http

        PUT /api/category HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "name":     "dresses",
            "rus_name":   "платья",
            "parent":     "clothes",
            "info":     "изменено описание категории...",
        }

    :statuscode 204: UPDATED
    :statuscode 404: категория(category) не найдена

DEL: Удалить категорию
======================

.. http:delete:: /api/category/(str:category)

    Удалить можно только пустую(без дочерних категорий и предметов) категорию.

    **Example request**:

    .. sourcecode:: http

        DELETE /api/category/dresses HTTP/1.1
        Host: example.com

    :statuscode 204: DELETED
    :statuscode 409: Не пустая категория не может быть удалена
    :statuscode 404: категория(category) не найдена

POST: Загрузить картинку
========================

.. http:post:: /api/upload/img

    Загрузка картинки в base64

    **Example request**:

    .. sourcecode:: http

        POST /api/category HTTP/1.1
        Host: example.com
        Content-Type: application/json

        {
            "filesize": "54836",
            "filetype": "image/jpeg",
            "filename": "profile.jpg",
            "base64":   "/9j/4AAQSkZJRgABAgAAAQABAAD//gAEKgD/4gIctcwIQA..."
        }

    :statuscode 200: OK
    :statuscode 400: Не корректные данные
