
from django.shortcuts import render
from .models import place
from .models import team
# Create your views here
def home(request):
    obj=place.objects.all()
    objj=team.objects.all()
    return render(request,'index.html',{'result':obj,'report':objj})



