from django.shortcuts import render,redirect
from accounts.forms import UserForm,UserprofileForm,UpdateForm,UpdateDetail,ForgotPasswordForm
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from defects.models import defectsData,Developers
from django.contrib.auth.models import User




# Create your views here.
def register(request):
    registered=False
    if request.method=='POST':
        form=UserForm(request.POST)
        form1=UserprofileForm(request.POST,request.FILES)

        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            
            profile=form1.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
            
        
          
    else:
            form=UserForm()
            form1=UserprofileForm()
    context={
            'form':form,
            'form1':form1,
            'registered':registered

     }
    return render(request,'accounts/registeration.html',context)


def user_login(request):
      if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
             if user.is_active:
                  login(request, user)
                  return redirect('home')
             else:
                  return HttpResponse('user is not active')
        else:
             return HttpResponse('please check your credential')
        
  
        
      return render(request,'accounts/login.html',)
@login_required(login_url='login')
def home(request):
      return render(request,'accounts/home.html',)

@login_required(login_url='login')
def user_logout(request):
     logout(request)
     return redirect('login')


@login_required(login_url='login')
def profile(request):
     user=request.user
     show_card=False
     total_defects = 0
     completed_defects = 0
     pending_defects = 0
     try:
        devloper=Developers.objects.get(dev_name=user)
        total_defects=defectsData.objects.filter(assigned_to=devloper).count()
  
        completed_defects=defectsData.objects.filter(assigned_to=devloper,defect_status='completed').count()
        pending_defects=defectsData.objects.filter(assigned_to=devloper,defect_status='Not completed').count()
        if devloper:
            
            show_card=True
          
     except Developers.DoesNotExist:
        pass

     context={
         'show_card':show_card,
         'total_defects':total_defects,
         'completed_defects':completed_defects,
         'pending_defects':pending_defects


        
    }
     return render(request,'accounts/profile.html',context)

@login_required(login_url='login')
def update(request):
     if request.method=='POST':
          form=UpdateForm(request.POST,instance=request.user)
          form1=UpdateDetail(request.POST,request.FILES,instance=request.user.userdata)
          if form.is_valid() and form1.is_valid():
               user=form.save()
               user.save()
               profile=form1.save(commit=False)
               profile.user=user
               profile.save()
               return redirect('profile')
     else:     
          form=UpdateForm(instance=request.user)
          form1=UpdateDetail(instance=request.user.userdata)
     return render(request,'accounts/update.html',{'form':form ,'form1':form1})



def forget_password(request):
     pasw=False
     if request.method=='POST':
          form=ForgotPasswordForm(request.POST)
          if form.is_valid():
               username=form.cleaned_data['username']
               password=form.cleaned_data['password']
               user=User.objects.get(username=username)
               user.set_password(password)
               user.save()
               pasw=True

               
     else:
               form=ForgotPasswordForm()
     return render(request,'accounts/forgetpassword.html',{'form':form,'pasw':pasw})






