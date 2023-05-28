from django.shortcuts import render
# from django.http import HttpResponse 
# from django.template import loader
# from .models import section
from main import models


# def main(request):
#     mysection = section.objects.all().values()
#     template = loader.get_template('index.html')
#     # return HttpResponse(template.render())
#     context = {
#         'section': mysection,
#     }
#     return HttpResponse(template.render(context, request))

def main (request):
    
    mysection = models.section.objects.all()
    
    
    dict = {
        'section': mysection
    }
    
    return render(request,"index.html",dict)