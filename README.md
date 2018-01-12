Типограф Евгения Лепёшкина
========================
Обёртка для этого замечательного [инструмента](http://www.typograf.ru/)

Возможно подключение к Django>=1.7

## Требования

Python 2.7.* – 3.6.*

## Как поставить
   ```bash
      pip install python-typograf
   ```

## Как пользоваться

   ```python
       from typograf import typograf

       typograf(text, **params)
   ```

Список и описание параметров [тут](http://www.typograf.ru/webservice/about/)
Дефолтный словарик с параметрами тут `typograf.settings.TYPOGRAF_SETTINGS`

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

* Выставьте необходимые параметры в `typograf.settings.TYPOGRAF_SETTINGS`

* Пользуйтесь
    ```javascript
        POST /typograf/
        {
            'text': 'Это "Типограф"?',
            'plain': 1  // при plain=0 вернет JSON {success: True, text: text}
        }

    ```

## Веб-сервис
    http://www.typograf.ru/

## Автор
 - <img src="https://avatars2.githubusercontent.com/u/1587683?s=40&v=4" width="30"/> [Melfi Silver](https://github.com/diveru4i)
