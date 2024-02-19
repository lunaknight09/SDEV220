from django.shortcuts import render
from django.http import HttpResponse



#Monday tip calc follow video 

#name of function will go to urls.py

def homePage(request):
    page = "<!DOCTYPE html><html><head></head>"
    page += "<body>"
    page += "<h3>Hello World!!!</h3>"
    page += "<p>this is our first django example</p>"
    page += "</body><html>"
    return HttpResponse(page)
