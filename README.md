Типограф студии Артемия Лебедева
========================
Обёртка для этого замечательного [инструмента](https://www.artlebedev.ru/typograf/)

Возможно подключение к Django>=1.7

## Требования

Python 2.7.* – 3.6.*

## Как поставить
   ```bash
      pip install -e git+https://github.com/diveru4i/typograf#egg=typograf
   ```

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
    ```javascript
        POST /typograf/
        {
            'text': 'Это "Типограф"?',
            'plain': 1  // при plain=0 вернет JSON {success: True, text: text}
        }

    ```

## Веб-сервис
    https://www.artlebedev.ru/typograf/

## Автор
 - <img src="https://avatars2.githubusercontent.com/u/1587683?s=40&v=4" width="30"/> [Melfi Silver](https://github.com/diveru4i)
