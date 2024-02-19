from django.shortcuts import render
from django.http import HttpResponse



#Monday tip calc follow video 

#name of function will go to urls.py

def homePage(request):
    page = "<!DOCTYPE html><html><head></head>"
    page += "<body>"
    page += "<h3>Hello World!!!</h3>"
    page += "<p>this is our first django example</p>"
    page += "<p> <a href=\"tipper\">the actual app</a></p>"
    page += "<p> <a href=\"payroll\">simple example</a></p>"
    page += "</body><html>"
    return HttpResponse(page)



def simple(request):
    data = {"title": "Simple Template", "message": "Hello World"}
    return render(request, "payroll.html", data)

def inputs(request):
    return render(request, "payroll.html")

def calculateTip(request):
    price = float(request.GET.get("price"))
    satisfaction = float(request.GET.get("satisfaction"))/100
    tip_amount = price * satisfaction
    total = price + tip_amount
    return render(request, "results.html", {"tip_amount": format(tip_amount, ".2f") "total": format(total, ".2f")})


#bug report 
#localhost:8000 never worked but followed the video fully 