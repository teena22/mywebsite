from django.shortcuts import render

def Art(request):
    return render(request,'myweb/art.html',{})
    
def Index(request):
    return render(request,'myweb/index.html',{})
