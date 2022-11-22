from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Emp
from django.contrib import messages
def index(request):
    return render(request,'index.html')

def feedback(request):
    if request.method=='POST':
        e=Emp()
        e.name=request.POST['name']
        e.email=request.POST['email']
        e.subject=request.POST['subject']
        e.message=request.POST['message']
        e.save()
        messages.warning(request,"Thanks for your Message Response soon")
        return redirect("/")
    else:
        return render(request,'index.html')
def page_not_found(request,exception):
    return render(request,'pagenotfound.html')
