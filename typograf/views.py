# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator

from typograf import typograf


class TypografView(View):

    def post(self, request):
        try:
            result = typograf(request.POST.get('text'))
            if request.POST.get('plain'):
                return HttpResponse(result)
            return JsonResponse({'success': True, 'text': result})
        except Exception as e:
            return JsonResponse({'success': False, 'error': e.__str__()})

    def get(self, request):
        raise Http404

    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        return super(TypografView, self).dispatch(request)



