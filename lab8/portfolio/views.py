import datetime

from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    now = datetime.datetime.now()

    context = {'hora': now.hour}
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')
