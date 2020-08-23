from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from first_app.models import Item


def index(request):
    template = loader.get_template('index.html')
    context = {
        'items': Item.objects.all()

    }

    return HttpResponse(template.render(context, request))
