from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
from .models import Book
from .script.morphological_analyser import KeyWordCollector
from .forms import NounCollectForm
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

def index(request):
    form = NounCollectForm()
    return render(request,"main/index.html",{"form":form})

@require_POST
def index_to_noun_result(request):
    form = NounCollectForm(request.POST)
    print(request.POST["text"])
    if form.is_valid():
        return render(request,"main/noun_result.html",{"form":form})
    else:
        return render(request,"main/index.html",{"form":form})
