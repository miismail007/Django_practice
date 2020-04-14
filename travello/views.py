from django.shortcuts import render
from .models import Description
# Create your views here.
def index(request):
    desc1 = Description()
    desc1.name = "mumbai"
    desc1.price = "850"
    desc1.desc = "Somthing"
    desc1.image = "https://www.planetware.com/wpimages/2019/11/india-best-places-to-visit-agra.jpg"
    return render(request,'index.html',{'desc1':desc1})