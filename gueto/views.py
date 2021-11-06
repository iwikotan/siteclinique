
from django.http import HttpResponse
#from django.Shortcuts import render

from django.shortcuts import render
def home_view(request):
    #return HttpResponse('bonjour landry')
    return render(request,'home.html')

 
def contact_view(request):
    #return HttpResponse('bonjour landry')
    return render(request,'contact.html')