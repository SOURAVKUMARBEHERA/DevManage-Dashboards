from django.shortcuts import render,redirect
from defects.models import defectsData,defect_screenshot,Testers
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,logout,login
from defects.forms import DefectEditForm,AddDefectForm
from django.core.paginator import Paginator



# Create your views here.


@login_required(login_url='login')
def descriptions(request ,id=0):
    defects=defectsData.objects.get(id=id)
    screenshots = defect_screenshot.objects.filter(defect=defects)


   

    context={
        'defects': defects,
        'screenshots': screenshots,
        
    }

  
    return render(request,'defects/descriptions.html',context)

@login_required(login_url='login')
def listofdefects(request):

    list_defects=defectsData.objects.all()
    defects_count=len(list_defects)


    paginator=Paginator(list_defects,4)
    page_num=request.GET.get('pg')
    list_defects=paginator.get_page(page_num)

# loging user details
    user=request.user
    show_button=False
    can_edit = False
    can_delete = False
    try:
        tester=Testers.objects.get(tester_name=user)
        if tester.is_admin:
            show_button=True
            can_edit = True
            can_delete = True
    except Testers.DoesNotExist:
        pass

    context={

        'list_defects':list_defects,
        'defects_count':defects_count,
        'show_button':show_button,
        'can_edit': can_edit,
        'can_delete': can_delete,
    }
    return render(request,'defects/alldefects.html',context)

@login_required(login_url='login')
def edit_defect(request ,id=0):
    defect=defectsData.objects.get(id=id)
    if request.method =='POST':
        form=DefectEditForm(request.POST,instance=defect)
        if form.is_valid():
            form.save()
            return redirect('alldefects')
    else:
         form=DefectEditForm(instance=defect)



    return render(request,'defects/defectedit.html',{'form':form})

@login_required(login_url='login')
def add_defect(request):
    if request.method=='POST':
        form=AddDefectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alldefects')
    else:
        form= AddDefectForm()
    return render(request,'defects/adddefects.html',{'form':form})

