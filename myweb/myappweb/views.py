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
    data2 = []
    for i in range(0, 99):
        jishu = jishu + 1
        data = {}
        data['name'] = 'wyp'
        data['position'] = str(jishu)+'shanghai'
        data['salary'] = str(jishu*100)
        data['start_date'] = '1'
        data['office'] = 'one-one'
        data['extn'] = '/meida/cjdj/2.docx'
        data2.append(data)
        
    count1 = jishu

    if request.method == "POST":
        draw = request.POST.get('draw') if request.POST.get('draw') else 1
        start = request.POST.get('start') if request.POST.get('start') else 1
        length = request.POST.get('length') if request.POST.get('length') else 1
        search = request.POST.get('args1')
        search2 = request.POST.get('args2')
        order_column1 = request.POST.get('order[0][column]')  # 排序字段索引
        order_column = request.POST.get('order[0][dir]')
#search_key
        print(search+","+search2)
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
