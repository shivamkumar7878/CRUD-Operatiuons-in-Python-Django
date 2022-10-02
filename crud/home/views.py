# import email
# import imp

from errno import ENETRESET
from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Entry

# Create your views here.
def home(request):
    
    return render(request,"Home.html");

def show(request):
    data=Entry.objects.all()
    return render(request ,"show.html",{'data':data});

def send(request):
    if request.method=='POST':
        id=request.POST['id'] 
        name=request.POST['name'] 
        email=request.POST['email'] 
        mobile=request.POST['mobile'] 
        Entry(id=id,name=name,email=email,mobile=mobile).save()
        msg="Data Stored Successfully"
        return render(request,"Home.html",{'msg':msg})

    else:
        return HttpResponse("<h1>404 - Not found </h1>")


def Delete(request):
    id=request.GET['id']
    Entry.objects.filter(id=id).delete()
    return HttpResponseRedirect("show") 

def edit(request):
    ID=request.GET['id'] 
    name=email=mobile="Not_Available"
    for data in Entry.objects.filter(id=ID):
        name=data.name 
        email=data.email
        mobile=data.mobile

    return render(request,"edit.html",{'id':ID,'name':name,'email':email,'mobile':mobile})

def RecordEdited(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        Entry.objects.filter(id=id).update(name=name,email=email,mobile=mobile)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse('404 Page Not Fount')
