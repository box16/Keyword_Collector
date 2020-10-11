from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Hello World!!")

def temp(request):
    context = {"msg":"Hello World!!"}
    return render(request,"main/temp.html",context)

def _list(request):
    books = Book.objects.all()
    return render(request,"main/list.html",{"books":books})