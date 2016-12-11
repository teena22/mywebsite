from django.shortcuts import render
from myweb.models import Msg
from django.template.context_processors import csrf
import os
    

def home(request):
    context = {}

    if 'submit' in request.POST:
        msg = Message(name=request.POST['name'], email=request.POST['email'],
                      message=request.POST['message'], subject=request.POST['subject'])
        msg.save()
        context.update({'message': 'Message Received!', 'messagetype': 'success'})

    context.update(csrf(request))
    return render(request, 'myweb/index.html', context)
