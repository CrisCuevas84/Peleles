from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("El Pancho se la come doblada")

def otro_metodo(request):                # no se pasan valores a través de URL
    pass    