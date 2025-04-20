from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# LANGUAGE_CODE = 'en-us'
def trial(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    