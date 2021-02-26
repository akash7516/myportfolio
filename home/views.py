from django.shortcuts import render,HttpResponse
from home.models import contactme

# Create your views here.
def home(request):
    # return HttpResponse('this is my home page (/)')
    context={'name':'akash','course':'Django'}
    return render(request,'home.html',context)
def about(request):
    # return HttpResponse('this is my about page (/)')
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        contact=contactme(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("the data has been inserted into db")
    return render(request,'contact.html')    
    #return HttpResponse('this is my contact page (/)')
    
def projects(request):
    #return HttpResponse('this is my projects page (/)') 
     return render(request,'projects.html')             