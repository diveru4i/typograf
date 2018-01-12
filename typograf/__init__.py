# -*- coding: utf-8 -*-
import urllib3

try:
    from django.conf import settings
    TS = settings.TYPOGRAF_SETTINGS
except:
    from .settings import TYPOGRAF_SETTINGS as TS


VERSION = '0.2.0'

__doc__ = u'''http://www.typograf.ru/webservice/about/

tags (теги) — значения: 0 — не расставлять; 1 — расставлять. Атрибут delete — значения: 0 — не удалять; 1 — удалять до типографирования; 2 — удалять после типографирования.
paragraph (параграфы) — атрибут insert: 1 — ставить; 0 — не ставить. start/end теги задают внешний вид обрамления параграфа, начальные и конечные теги соответственно (могут быть пустыми).
newline — перевод строки. Атрибут insert: 1 — ставить; 0 — не ставить. Внутри тега пишутся теги перевода строки.
dos-text — удаляет одинарные переводы строк и переносы. Атрибут delete: 0 — не удалять; 1 — удалять.
nowraped — неразрывные конструкции. Атрибут insert: 1 — ставить; 0 — не ставить. Атрибут nonbsp: 0 — не использовать неразрывные конструкции вместо (неразрывного пробела); 1 — наоборот. Атрибут length: не объединять в неразрывные конструкции слова, написанные через дефис, с общей длинной больше N знаков. Если 0 то не используется. start/end аналогично параграфам.
hanging-punct — висячая пунктуация. Атрибут insert: 1 — использовать; 0 — не использовать.
hanging-line — висячие строки. Атрибут delete: 1 — удалять; 0 — не удалять.
minus-sign — указывает какой символ использовать вместо знака минус: — &ndash; или &minus;.
acronym — выделять сокращения. Атрибут insert: 1 — выделять; 0 — не выделять.
symbols — как выводить типографированный текст. Атрибут type: 0 — буквенными символами (&nbsp;); 1 — числовыми (&#160;).
link — добавляет дополнительные атрибуты к ссылкам
'''


def typograf(text,
    tags=TS['tags'],
    paragraph=TS['paragraph'],
    newline=TS['newline'],
    dos_text=TS['dos_text'],
    nowraped=TS['nowraped'],
    hanging_punct=TS['hanging_punct'],
    hanging_line=TS['hanging_line'],
    minus_sign=TS['minus_sign'],
    hyphen=TS['hyphen'],
    acronym=TS['acronym'],
    symbols=TS['symbols'],
    link=TS['link']):

    service_url = 'http://www.typograf.ru/webservice/'

    XML = u'''<?xml version="1.0" encoding="windows-1251" ?>
        <preferences>
            <!-- Теги -->
            <tags delete="{tags[delete]}">{tags[value]}</tags>
            <!-- Абзацы -->
            <paragraph insert="{paragraph[insert]}">
                <start><![CDATA[{paragraph[start]}]]></start>
                <end><![CDATA[{paragraph[end]}]]></end>
            </paragraph>
            <!-- Переводы строк -->
            <newline insert="{newline[insert]}"><![CDATA[{newline[value]}]]></newline>
            <!-- Переводы строк <p>&nbsp;</p> -->
            <cmsNewLine valid="0" />
            <!-- DOS текст -->
            <dos-text delete="{dos_text[delete]}" />
            <!-- Неразрывные конструкции -->
            <nowraped insert="{nowraped[insert]}" nonbsp="{nowraped[nobsp]}" length="{nowraped[length]}">
                <start><![CDATA[{nowraped[start]}]]></start>
                <end><![CDATA[{nowraped[end]}]]></end>
            </nowraped>
            <!-- Висячая пунктуация -->
            <hanging-punct insert="{hanging_punct[insert]}" />
            <!-- Удалять висячие слова -->
            <hanging-line delete="{hanging_line[delete]}" />
            <!-- Символ минус -->
            <minus-sign><![CDATA[{minus_sign[value]}]]></minus-sign>
            <!-- Переносы -->
            <hyphen insert="{hyphen[insert]}" length="hyphen[length]" />
            <!-- Акронимы -->
            <acronym insert="{acronym[insert]}"></acronym>
            <!-- Вывод символов 0 - буквами 1 - числами -->
            <symbols type="{symbols[type]}" />
            <!-- Параметры ссылок -->
            <link target="{link[target]}" class="{link[class]}" />
        </preferences>
    '''.format(**locals())
    text = urllib3.PoolManager().request('POST', service_url, fields={'text': text, 'chr': 'UTF-8', 'xml': XML}).data.decode('utf8')
    return text
