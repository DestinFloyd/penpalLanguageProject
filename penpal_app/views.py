from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
import json 
from penpal_app.forms import UserForm, MessageForm, ProficiencyForm, LanguageForm 

# Create your views here.
from .models import User

# Users
def user_index(request):
    users = User.objects.all().values()
    return HttpResponse(users)
    
def user_show(request, id):
    user = User.objects.get(id = id)
    data = {}
    data['firstName'] = user.firstName
    data['lastName'] = user.lastName
    data['email'] = user.email
    data['id'] = user.id
    data2 = json.dumps(data)
    return HttpResponse(data2)

def user_create(response):
    if request.method == 'POST':
            form = UserForm(request.body)
            if form.is_valid:
                user = form.save()
                return redirect('user')
    else:
        form = UserForm()
        return render({"error": "cannot update"})

def user_delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/user')

def user_edit(request, id):  
    user = User.objects.get(id=id)  
    return render(request)  

def user_update(request, id):  
    user = User.objects.get(id=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/user")  
    return render(request, 'edit.html', {'employee': employee})  



