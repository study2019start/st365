from django.shortcuts import render
from django.contrib import messages
from django import forms
from myappweb.models import user
from django.forms import widgets
from django.http import HttpResponse
import json 


class UserForm(forms.Form):   # 必须继承forms.Form
    name = forms.CharField(label="用户名  ", required=True, error_messages={"required": "不能为空"},
                           widget=widgets.TextInput())
    pwd = forms.CharField(label="密    码  ", required=True, error_messages={"required": "不能为空"},
                          widget=widgets.PasswordInput())


def login(request):
    form = UserForm() 
    if request.method == "POST":
        form1 = UserForm(request.POST)
        if form1.is_valid():
            data1 = form1.clean()
            result = user.objects.filter(loginname=data1["name"], password=data1["pwd"],)
            print(data1["name"])
            if result.exists():
                return render(request, 'myappweb/index.html', {'name': data1["name"]})
            else:
                messages.success(request, "错误")
                return render(request, 'myappweb/login.html')
        else:
            
            errors = form1.errors
            return render(request, 'myappweb/login.html', {"form": form, "errors": errors})
    else:
        return render(request, 'myappweb/login.html', {"form": form})


def index(request):
    return render(request, 'myappweb/index.html')


def vtable(request):
    return render(request, 'myappweb/datatable.html')


def down(request, id):
    print(request.GET)
    return HttpResponse('id = %s' % (id))


def cdatatable(request):
    jishu = 0

        
    count1 = jishu

    if request.method == "POST":
        sts=""
        draw = request.POST.get('draw') if request.POST.get('draw') else 0
        start = request.POST.get('start') if request.POST.get('start') else 1
        length = request.POST.get('length') if request.POST.get('length') else 10
        qu = request.POST.get('args1')
        dis = request.POST.get('args2')
        lx = request.POST.get('args3')
        startd = request.POST.get('args4')
        endd = request.POST.get('args5')
        mindj = request.POST.get('args6')
        maxdj = request.POST.get('args7')
        order_column1 = request.POST.get('order[0][column]')  # 排序字段索引
        order_column = request.POST.get('order[0][dir]')
        searc=dict()
        if qu:
            searc['area'] = qu
        if dis:
            searc['dizhi']=dis
        
        data2 = Cjdj_info.objects.filter(dizhi)


#search_key
        
        if draw:
            dic = {
                'draw': draw,
                'recordsTotal': count1,
                'recordsFiltered': count1,
                'data': data2
            } 
            print(start)
        else:
            dic = {'data': data2}
    
        return HttpResponse(json.dumps(dic), content_type='application/json')
    else:
        dic = {
            'draw': 1,
            'recordsTotal': count1,
            'recordsFiltered': count1,
            'data': data2
        } 
        
        return HttpResponse(json.dumps(dic), content_type='application/json')
        


# Create your views here.
