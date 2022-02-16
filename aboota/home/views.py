from django.shortcuts import render

def checking(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about-us.html")
def product(request):
    return render(request,"products.html")    