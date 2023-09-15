from django.shortcuts import render
from django.http import *
from .forms import UserForm, NameForm
from django.template.response import TemplateResponse

# Create your views here.

#def index(request):
#    return TemplateResponse(request, "firstapp/home.html")

def index(request):
    if request.method == "POST":
        userform = NameForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Имя введено корректно - {0}</h2>".format(name))
        else:
            return HttpResponse("Ошибка ввода данных")

        #name = request.POST.get("name")
        #age = request.POST.get("age")
        #output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name, age)
        #return HttpResponse(output)
    else:
        userform = NameForm()
        return render(request, "firstapp/index.html", {"form":userform})

def personal_data(request):
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]
    user = {"name": "Максим", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "firstapp/personal_data.html", context=data)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

# def contact(request):
#    return HttpResponse("<h2>Контакты</h2>")

def m404(request):
    return HttpResponseNotFound("<h1>Ниче не найдено<\h1>")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0}, Категория: {1} </h2>".format(productid, category)
    return  HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Макс")
    output = "<h2>Пользователь </h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)

#def products(request, productid = 1):
#    output = "<h2>Продукт № {0}</h2>".format(productid)
#    return HttpResponse(output)

#def users(request, id=1, name='Максим'):
#    output = "<h2>Пользователь </h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
#    return HttpResponse(output)