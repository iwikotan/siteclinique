from django.shortcuts import render
from .donnees import info

def index(request):
     contenue=info.all()
     return render(request,'clinique/index.html',{'patients':contenue})

def details(request,id):
    id=info.find(id)
    return render ( request,'details.html',{'id':id})
