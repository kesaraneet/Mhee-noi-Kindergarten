from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return HttpResponse('Report page1 หน้าจอ Dastboard')

def search(request):
    return HttpResponse('Report page2 หน้าจอ Search')

