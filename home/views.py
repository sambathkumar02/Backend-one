from django.shortcuts import render,HttpResponse
from .models import Customer
# Create your views here.

def index(request):
    return HttpResponse('welcome to home page..')

def login(request):
    if request.method =='POST':
        mail=request.POST['Email']
        password = request.POST['Password']
        result = Customer(email=mail, password=password)
        if not result:
            return HttpResponse('login failed')
        else:
            str='login success..\n Welcome '+result.name
            return HttpResponse(str)


    else:
        return render(request,'login.html')


def signup(request):
    if request.method =='POST':
        name=request.POST['Name']
        mail=request.POST['Email']
        password=request.POST['Password']
        cusotmer=Customer(name=name,email=mail,password=password)
        cusotmer.save()
        return HttpResponse('signup sucessful...')


    else:
        return render(request,'signup.html')


