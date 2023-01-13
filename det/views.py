from django.shortcuts import render
from .forms import EmpReg
from django.http import HttpResponse
def ShowDetails(request):
    if request.method=='POST':
        fm=EmpReg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['password']
            print (nm)
            print (em)
            print (pm)
        else:
            fm=EmpReg()

            return render(request,'det/reg.html',{'form':fm})  
            # return HttpResponse('Views is workin')
# def AddShow(request):
#     return render(request, 'det/addandshow.html')
            

# Create your views here.

