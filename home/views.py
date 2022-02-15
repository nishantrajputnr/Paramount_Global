from django.shortcuts import render

def checking(request):
    return render(request,"index.html")

def template3d(request):
    return render(request,"template-3d-animation-classic.html")
def template(request):
    return render(request,"template-3d-graphic-particle.html")    