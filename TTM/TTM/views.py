from django.shortcuts import render

def loginPage(request):
    return render(request,"login.html")


def homepage(request):
    return render(request,"index.html")
def aboutuspage(request):
    return render(request,"aboutus.html")
def registrationpage(request):
    return render(request,"register.html")