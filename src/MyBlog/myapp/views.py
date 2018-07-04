from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import HttpResponse


# Create your views here.
def homepage(request):

    template =get_template('index.html')
    
    html     =template.render(locals())
    return HttpResponse(html)