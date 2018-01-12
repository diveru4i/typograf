# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import urllib3

try:
    from django.conf import settings
    TYPOGRAF_SETTINGS = settings.TYPOGRAF_SETTINGS
except:
    from .settings import TYPOGRAF_SETTINGS


VERSION = '0.1.3'


def typograf(text,
    entity_type=TYPOGRAF_SETTINGS['entity_type'],
    use_br=TYPOGRAF_SETTINGS['use_br'],
    use_p=TYPOGRAF_SETTINGS['use_p'],
    max_nobr=TYPOGRAF_SETTINGS['max_nobr'],
    encoding=TYPOGRAF_SETTINGS['encoding']):

    text = text.replace('&', '&amp;').replace('<', '&lt;').replace ('>', '&gt;').replace(':«', ': «')

    SOAPBody = u'''
        <?xml version="1.0" encoding="{encoding}"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <ProcessText xmlns="http://typograf.artlebedev.ru/webservices/">
                <text>{text}</text>
                    <entityType>{entity_type}</entityType>
                    <useBr>{use_br}</useBr>
                    <useP>{use_p}</useP>
                    <maxNobr>{max_nobr}</maxNobr>
                </ProcessText>
            </soap:Body>
        </soap:Envelope>
    '''.format(text=text, entity_type=entity_type, use_br=use_br, use_p=use_p, max_nobr=max_nobr, encoding=encoding).strip().encode('utf8')

    headers = {
        'Host': 'typograf.artlebedev.ru',
        'Content-Type': 'text/xml',
        'Content-Length': str(len(SOAPBody)),
        'SOAPAction': 'http://typograf.artlebedev.ru/webservices/ProcessText'
    }

    service_url = 'http://typograf.artlebedev.ru/webservices/typograf.asmx'

    response = urllib3.PoolManager().request('POST', service_url, body=SOAPBody, headers=headers)
    result = ET.fromstring(response.data)
    return result.find('.//{http://typograf.artlebedev.ru/webservices/}ProcessTextResult').text
