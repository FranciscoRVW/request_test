# request_test/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import json


# Create your views here.

@csrf_exempt
def apiV1(request):
    print(f'''{request.method}
      {request.headers}''')
    return JsonResponse({"status": "ok"}, status=200,)
