from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def home(request):
	sn=[{'name':'s','age':21},
	{'name':'n','age':20}
	]
	return render(request,"index.html",context={'sn':sn,'page':'HOME'})
	
