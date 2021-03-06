from django.shortcuts import render,redirect
from myweb.models import Msg
from django.template.context_processors import csrf
import os
    

def home(request):
    context = {}

    if 'submit' in request.POST:
        msg = Msg(name=request.POST['name'], email=request.POST['email'],
                      message=request.POST['message'], subject=request.POST['subject'])
        msg.save()
        context.update({'message': 'Message Received!', 'messagetype': 'success'})

        context.update(csrf(request))
        return redirect('/')
    return render(request, 'myweb/index.html', context)
    
def readmore(request):
        return render(request, 'myweb/readmore.html', {})
      
def error(request):
    context = {'message': "Oops! something went wrong",
               "followup": "Let's take you ",
               'linkword': "Home",
               "link": "/"
               }

    return render(request, 'myweb/error.html', context)
    

