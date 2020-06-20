from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>hello hell</em>")

def help(request):
    my_dic = {'ask_help':"hey there, I am here, happy to help you"}
    return render(request,'AppTwo/help.html',context=my_dic)
