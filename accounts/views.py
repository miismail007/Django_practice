from django.shortcuts import render
from django.http import HttpResponse
from . models import Users 
# Create your views here.


def register(request):
	return render(request,'register.html')


def registerpost(request):
	username = request.POST['username']
	password = request.POST['password']
	post = Users()
	post.username = username
	post.password = password
	post.save()
	return render(request,'register.html',{'status':'success'})