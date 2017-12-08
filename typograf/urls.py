# -*- coding: utf-8 -*-
from django.conf.urls import url

from typograf.views import TypografView


urlpatterns = [
    url(r'$', TypografView.as_view(), name='typograf'),
]

