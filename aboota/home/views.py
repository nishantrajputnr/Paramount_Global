from django.shortcuts import render

def checking(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about-us.html")
def product(request):
    return render(request,"products.html")    
def education(request):
    return render(request,"education.html") 
def trading(request):
    return render(request,"trading.html")     
def terminal(request):
    return render(request,"terminal.html")     
def referal(request):
    return render(request,"referal.html")     
def contact(request):
    return render(request,"contact.html")     