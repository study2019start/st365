from django.shortcuts import render
from django.contrib import messages
from django import forms
from myappweb.models import user
from django.forms import widgets


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
# Create your views here.
