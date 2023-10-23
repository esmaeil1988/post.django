from django.shortcuts import render,HttpResponse
from.models import doctor
from.models import news
from.models import contact as cn
# Create your views here.

def home(request):
    l=doctor.objects.all()
    l2=news.objects.all()
    return render(request,"dent/index.html",context={"doc":l, "khabar":l2})



def showdr(request,adad):
    l=doctor.objects.get(id=adad)
    return render(request,"dent/doctors.html",context={"dcr":l})

def shownews(request,adad):
    l=news.objects.get(id=adad)
    return render(request,"dent/blog-details.html",context={"nw":l})


def contact(request):
    n=request.POST.get("nam")
    o=request.POST.get("onvan")
    e=request.POST.get("email")
    m=request.POST.get("matn")
    i=request.POST.get("img")
    if (n!=None):
        cn.objects.create(nam=n,onvan=o,email=e,matn=m,img=i)
        return render (request,"dent/sabt.html")
    return render(request,"dent/contact.html")


def register(request):
    n=request.GET.get("nam")
    o=request.GET.get("onvan")
    e=request.GET.get("email")
    m=request.GET.get("matn")
    if (n!=None):
        cn.objects.create(nam=n,onvan=o,email=e,matn=m)
        return render (request,"dent/sabt.html")
    return render(request,"dent/register.html")

