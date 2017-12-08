Типограф студии Артемия Лебедева
========================
Обёртка для этого замечательного [инструмента](https://www.artlebedev.ru/typograf/)

Возможно подключение к Django>=1.7

## Требования

Python 2.7.* – 3.*.*

## Как пользоваться
    ```python
    from typograf import typograf

    typograf(text, entity_type=1, use_br=0, use_p=0, max_nobr=3, encoding='UTF-8')
    ```

## Работа с Django

* Добавьте в INSTALLED_APPS
    ```python
        INSTALLED_APPS = [
            ...
            'typograf',
            ...
        ]
    ```

* Добавьте в urls.py
    ```python
    urlpatterns = [
        ...
        url(r'typograf/', include('typograf.urls')),
        ...
    ]
    ```

* Пользуйтесь
    ```
        POST /typograf/
        {
            'text': 'Это "Типограф"?',
            'plain': 1  # при plain=0 вернет JSON {success: True, text: text}
        }

    ```

## Веб-сервис
    https://www.artlebedev.ru/typograf/

## Автор
 - <img src="https://svn.designdepot.ru/uploads/-/system/user/avatar/2/200.jpg" width="30"/> Melfi Silver
