from django.shortcuts import render,HttpResponseRedirect
from .forms import EmpReg
from .models import User
# from django.http import HttpResponse
def ShowDetails(request):
    if request.method == 'POST':
     fm=EmpReg(request.POST)
     if fm.is_valid():
        fm.save()
        fm=EmpReg()
    else:
        fm = EmpReg() 
    sh = User.objects.all() 
    context = {
    'form': fm,
    'show': sh

    }   
    return render (request, 'reg.html', context )      

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

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmpReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            
            return HttpResponseRedirect('/a')
    else:
        pi=User.objects.get(pk=id)
        fm= EmpReg(instance=pi)
    return render(request, '/home/sagar/Bulb/Pen/P/det/templates/update.html', {'form':fm})          

def delete_data(request, id):
    if request.method== 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/a')


