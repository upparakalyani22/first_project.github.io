from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dicto = {'insert_text':"Django app coming from first_app/index.html file !"}
    return render(request, 'first_app/index.html', context=dicto)
