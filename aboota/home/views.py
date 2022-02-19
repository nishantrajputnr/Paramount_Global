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
def referral(request):
    return render(request,"referral.html")     
def contact(request):
    return render(request,"contact.html")     
def account(request):
    return render(request,"account.html")    