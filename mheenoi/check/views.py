from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('check page1')

def course(request, id):
    return HttpResponse('check page2 หน้าจอรายละเอียดของแต่ละวิชา (id:%d)' %id)

def qrcode(request):
    return HttpResponse('check page3 QR code')