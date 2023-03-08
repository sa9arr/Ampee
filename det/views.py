from django.shortcuts import render,HttpResponseRedirect
from .forms import EmpReg
from .models import User
from django.contrib import messages
# from django.http import HttpResponse
def home(request):
 if request.method == 'POST':
     fm=EmpReg(request.POST,request.FILES)
     

     if fm.is_valid():
        emname=fm.cleaned_data.get('emname')
        designation=fm.cleaned_data.get('designation')
        ememail=fm.cleaned_data.get('ememail')
        photo=fm.cleaned_data.get('photo')
        obj=User.objects.create(emname=emname,designation=designation,photo=photo,ememail=ememail)
        obj.save()
        success= "New Employee Record Successfully created"
        messages.add_message(request, messages.SUCCESS, success)
     return HttpResponseRedirect('/a/details')

 else:
    fm = EmpReg() 
    sh = User.objects.all() 
    context = {
    'form': fm,
    'show': sh

    }   
    return render (request, 'reg.html', context )  
 
 
def ShowDetails(request):
    if request.method == 'POST':
     fm=EmpReg(request.POST,request.FILES)
     

     if fm.is_valid():
        emname=fm.cleaned_data.get('emname')
        designation=fm.cleaned_data.get('designation')
        ememail=fm.cleaned_data.get('ememail')
        photo=fm.cleaned_data.get('photo')
        obj=User.objects.create(emname=emname,designation=designation,photo=photo,ememail=ememail)
        obj.save()
        success= "New Employee Record Successfully created"
        messages.add_message(request, messages.SUCCESS, success)

    else:
        fm = EmpReg() 
    sh = User.objects.all() 
    context = {
    'form': fm,
    'show': sh

    }   
    return render (request, 'details.html', context )      
#     # fm=EmpReg()
#     # return render(request,'/home/sagar/Bulb/Pen/P/det/templates/reg.html',{'form':fm})
#     # 
# #  if request.method =='POST':
# #         fm=EmpReg(request.POST)
# #     #     if fm.is_valid():
# #     #         nm=fm.cleaned_data['name']
# #     #         em=fm.cleaned_data['email']
# #     #         pm=fm.cleaned_data['password']
# #  else:
#             fm=EmpReg()
#             return render(request,'/home/sagar/Bulb/Pen/P/det/templates/reg.html',{'form':fm})  
#             # return HttpResponse('Views is workin')
# # def AddShow(request):
# #     return render(request, 'det/addandshow.html')
            

# # Create your views here.

def update_data(request, id,):
    if request.method == 'POST':
        pi = User.objects.get(pk=id,)
        fm = EmpReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            success=f"record successfully updated"
            messages.add_message(request, messages.SUCCESS, success)

            
            return HttpResponseRedirect('/a/details')
    else:
        pi=User.objects.get(pk=id,)
        fm= EmpReg(instance=pi)
    return render(request, 'update.html', {'form':fm})          

def delete_data(request, id):
    if request.method== 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        success= "Employee Record deleted"
        messages.add_message(request, messages.SUCCESS, success)
        return HttpResponseRedirect('/a/details')


