from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages,auth 
from .helpers import dictfetchall
from .models import Employee
from django.db import  connection
from django.shortcuts import redirect
from .forms import *
from django.shortcuts import redirect, render
from django.contrib import auth, messages

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            error = "Incorrect username or password!"
            messages.add_message(request, messages.ERROR, error)
            return redirect('signin')
    return render(request, 'signin.html')
    








def signup(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        if password==password2:
            if User.objects.filter(email=email, username=username).exists():
                errorm="User already taken"
                messages.add_message(request, messages.ERROR, errorm)
                return redirect("signup")
            

            else:
                user=User.objects.create_user(username=username,email=email,password=password)

                user.save()
                # with connection.cursor() as cursor:
                #     cursor.execute("INSERT INTO  auth_user(first_name,last_name,email,username,password,is_superuser,is_staff,is_active,date_joined) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fname,lname,email,username,password,False,False,True,'2022-12-18'))
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                user_model=User.objects.get(username=username)
              
                return redirect('signin')
        else:
            messages.add_message(request,"Password not matched")
            return redirect('signup')


    return render(request,'signup.html')
# from django.http import HttpResponse
def home(request):
 if request.method == 'POST':
     fm=EmpReg(request.POST,request.FILES)
     

     if fm.is_valid():
        print(fm)
        emname=fm.cleaned_data.get('emname')
        designation=fm.cleaned_data.get('designation')
        ememail=fm.cleaned_data.get('ememail')
        photo=fm.cleaned_data.get('photo')
        salary=fm.cleaned_data.get('salary')

        obj=Employee.objects.create(emname=emname,salary=salary,designation=designation,photo=photo,ememail=ememail)
        obj.save()
        # with connection.cursor() as cursor:
        #             cursor.execute("INSERT INTO  det_employee(emname,designation,ememail,photo,salary) VALUES(%s,%s,%s,%s,%s)",(emname,designation,ememail,photo,salary))
        success= "New Employee Record Successfully created"
        messages.add_message(request, messages.SUCCESS, success)
     return HttpResponseRedirect('/details')

 else:
    fm = EmpReg() 
    sh = Employee.objects.all() 
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
        obj=Employee.objects.create(emname=emname,designation=designation, salary=salary, photo=photo,ememail=ememail)
        obj.save()
        success= "New Employee Record Successfully created"
        messages.add_message(request, messages.SUCCESS, success)

    else:
        fm = EmpReg() 
    # sh = Employee.objects.all() 
    with connection.cursor() as cursor:
                    cursor.execute("SELECT * from det_employee")
                    sh=dictfetchall(cursor)
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
        pi = Employee.objects.get(pk=id,)
        fm = EmpReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            success=f"record successfully updated"
            messages.add_message(request, messages.SUCCESS, success)

            
            return HttpResponseRedirect('/details')
    else:
        pi=Employee.objects.get(pk=id,)
        fm= EmpReg(instance=pi)
    return render(request, 'update.html', {'form':fm})          

def delete_data(request, id):
    if request.method== 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        success= "Employee Record deleted"
        messages.add_message(request, messages.SUCCESS, success)
        return HttpResponseRedirect('/details')


