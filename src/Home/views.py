from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"pages/index.html",{'user':request.user})