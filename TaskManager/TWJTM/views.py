from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import tmUsersForm,taskForm
from .models import tmUsersData
from sqlalchemy import create_engine
import pandas as pd

# Create your views here.
def firstpageView(request):
    template_name='firstpage.html'
    context={}
    return render(request,template_name,context)

def baseView(request,company):
    template_name='base.html'
    global com
    com=company
    if company=='infra':
        context = {'company':'TWJ INFRASTRUCTURE PVT.LTD.'}
        return render(request,template_name,context)
    if company=='tbc':
        context = {'company':'TWJ BUSINESS CONSULTING PVT.LTD.'}
        return render(request,template_name,context)

    context={}
    return render(request,template_name,context)

def loginView(request):
    form = tmUsersForm()
    template_name='TWJTM/login.html'
    global company
    company=''
    if com=='infra':
        company='TWJ INFRASTRUCTURE PVT.LTD.'
    if com=='tbc':
        company='TWJ BUSINESS CONSULTING PVT.LTD.'
    context={'form':form,'company':company}

    if request.method=="POST":
        global un
        un = request.POST.get('un')
        my_conn = create_engine("mysql+mysqldb://root:new123@localhost/twjtm")
        conn = my_conn.connect()
        query = "select * from twjtm_tmusersdata where username='" + un + "' and company='" + company + "'"
        my_data = pd.read_sql(query, conn)
        conn.close()
        if len(my_data)==1:
            data=tmUsersData.objects.filter(username=un,company=company)
            context={'data':data,'username':un,'msg':'Login Successful','company':company}
            return render(request,'tasksystem.html',context)
        else:
            template_name = 'TWJTM/login.html'
            context = {'form':form,'msg':'Invalid Login','company':company}
            return render(request,template_name,context)
    return render(request,template_name,context)

def signupView(request):
    form=tmUsersForm()
    template_name='TWJTM/signup.html'
    company=''
    if com=='infra':
        company='TWJ INFRASTRUCTURE PVT.LTD.'
    if com=='tbc':
        company='TWJ BUSINESS CONSULTING PVT.LTD.'
    context={'form':form,'company':company}
    form.initial['company']=company
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        emailid = request.POST['emailid']
        mobile = request.POST['mobile']
        caption = request.POST['caption']
        Image = request.FILES['image']
        company=request.POST['company']

        image=tmUsersData.objects.create(username=username,password=password,emailid=emailid,mobile=mobile,caption=caption,image=Image,company=company)
        context={'msg':'Record Added Sucessfully!!!!!!!'}
        return render(request,template_name,context)
    return render(request,template_name,context)

def msgView(request):
    template_name='TWJTM/Tasks.html'
    context={}
    return  render(request,template_name,context)


def addtaskView(request):
    # print(un,company)
    form=taskForm()
    template_name='TWJTM/addtask.html'
    data = tmUsersData.objects.filter(username=un, company=company)
    context = {'data': data, 'username': un, 'msg': 'Login Successful', 'form':form,'com':com,'company':company}
    if request.method=="POST":
        location=request.POST.get('location')
        task=request.POST.get('task')
        desc=request.POST.get('desc')
        stdt=request.POST.get('start_date')
        estdt=request.POST.get('estimated_date')
        endt=request.POST.get('end_date')
        comme=request.POST.get('comments')
        comp=request.POST.get('company')
        print(location,task,desc,stdt,estdt,endt,comme,comp)
        form.initial['id']=1
        form.initial['username']='admin'

        my_conn = create_engine("mysql+mysqldb://root:new123@localhost/twjtm")
        conn = my_conn.connect()
        query = "select id from twjtm_taskdata"
        my_data = pd.read_sql(query, conn)
        conn.close()
        max_count = 0
        for i in my_data.index:
            count = my_data['id'][i]
            if count > max_count:
                max_count = count
        form.initial['id'] = max_count + 1
        query="insert into twjtm_taskdata values(" + str(id) + ",'" + location + "','" + task + "','" + desc + "','" + stdt +"','" + estdt + "','"

        return redirect('addtask_url')


    return render(request, template_name, context)

