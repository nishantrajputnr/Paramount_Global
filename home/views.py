from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    if request.method=="GET":
        a = request.GET['first']
        b = request.GET["second"]
        a=int(a)
        b=int(b)
        return HttpResponse(a+b)
    return HttpResponse("asdfasdf")
def fun1(request):
    return render(request,"index.html")