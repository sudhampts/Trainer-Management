from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Trainer.models import City, Trainer_reg, Course, Trainer_Assign


def home(request):
    return render(request,'html\login.html')


def log_read(request):
    username = request.POST['txtUserName']
    pswd = request.POST['txtPswd']
    user = authenticate(username = username,password =pswd)
    res = ''
    if user is not None:
        if user.is_superuser:
            res = render(request,'html\\admin_home.html')
    else:
        id = Trainer_reg.objects.get(tname=username)
        request.session['name'] = id.id
        res = render(request, 'html\\TrainerHtml\\trainer_home.html',{'data':id})
    return res

#--------------------------------------------
# Trainer registeration page
#-----------------------------------------------
def reg_home(request):
    city = City.objects.all()
    return render(request,'html\\trainer_registration.html',{'City':city})


def reg_data(request):
    t1 = Trainer_reg()
    t1.tname=  request.POST['txtName']
    t1.tage = request.POST['txtAge']
    t1.tphno = request.POST['txtPhno']
    t1.password = request.POST['txtPswd']
    t1.city =City.objects.get(city_name = request.POST['ddlCity'])
    t1.save()
    return redirect('home')


def trainer_home(request):
    return render(request, 'html\\TrainerHtml\\trainer_home.html')

def batch_details(request):
    assign = Trainer_Assign.objects.filter(t_name=request.session['name'])
    return render(request, 'html\\TrainerHtml\\Showing_batch_details.html', {'Assign': assign})



#------------------------------------
# Admin will assign batch for trainer
#-------------------------------------
def admin_home(request):
    return render(request,'html\\admin_home.html')

def assign_page(request):
    course = Course.objects.all()
    trainer = Trainer_reg.objects.all()
    res = render(request,'html\\trainer_assign.html',{'Course':course,'Trainer':trainer})
    return res

def trainer_assign(request):
    t1 = Trainer_Assign()
    t1.t_name = Trainer_reg.objects.get(tname = request.POST['ddlTname'])
    t1.batch_no = request.POST['txtBatchNum']
    t1.course =Course.objects.get(course_name = request.POST['ddlCourse'])
    t1.date = request.POST['txtDate']
    t1.save()
    return redirect('assigned')


def trainer_details(request):        # Trainer details
    t1 = Trainer_reg.objects.all()
    return render(request,'html\\trainer_details.html',{'data':t1})


def assigned_batch(request):    # assigned batch details
    assign = Trainer_Assign.objects.all()
    return render(request,'html\\assigned_batch_details.html',{'Assign': assign})


def update_batch(request,id):    # update the batch details
    t1 = Trainer_Assign.objects.get(id=id)
    course = Course.objects.all()
    trainer = Trainer_reg.objects.all()
    if request.method == 'POST':
        t1.t_name = Trainer_reg.objects.get(tname=request.POST['ddlTname'])
        t1.batch_no = request.POST['txtBatchNum']
        t1.course = Course.objects.get(course_name=request.POST['ddlCourse'])
        t1.date = request.POST['txtDate']
        t1.save()
        assign = Trainer_Assign.objects.all()
        return render(request, 'html\\assigned_batch_details.html', {'Assign': assign})
    return render(request,'html\\update_batch.html',{'data':t1,'Course':course,'Trainer':trainer})


def delete_batch(request,id):
    t1 = Trainer_Assign.objects.get(id=id)
    t1.delete()
    return redirect('assigned')