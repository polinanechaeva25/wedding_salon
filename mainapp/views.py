from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.conf import settings
from django.core.mail import send_mail


class MainListView(ListView):
    model = User
    template_name = 'mainapp/index.html'


class EmailView(View):
    def get(self, request):
        print('JUST POST REQUEST IS ADMITTED!')
        return redirect("mainapp:index")

    def post(self, request):
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            title = f'САЙТ - новое письмо.'
            email_body = f'Имя: {name}\nТелефон: {phone}\nEmail: {email}\nСообщение: {message}'
            print('SENDING EMAIL:')
            send_mail(title, email_body, settings.EMAIL_HOST_USER,
                      ['L.A.WED@yandex.ru'])  # justitdevelopment@gmail.com
        except Exception as e:
            print('ERROR:', e)
        return redirect("mainapp:index")
