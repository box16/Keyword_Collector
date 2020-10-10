from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!!")

def temp(request):
    context = {"msg":"Hello World!!"}
    return render(request,"main/temp.html",context)