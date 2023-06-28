from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Este es el inicio de mi pagina</h1>")

def about(request):
    return HttpResponse("<h1>Esta es la pagina sobre nosotros de mi pagina</h1>")