from django.shortcuts import render, HttpResponse
from .task import sleepy, email_send_our_user
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home_view(request):
    email_send_our_user.delay()
    wish = 'hello World'
    return HttpResponse(f'{wish}')


def name_view(request, name):
    wish = f'hello World {name}'
    if wish:
        print('working')
    return HttpResponse(f'{wish}')
