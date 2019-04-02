from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
from .models import User

# Users
def user_index(request):
    users = User.objects.all().values()
    users_list = list(users)
    return JsonResponse(users_list, safe=False)
    

def user_show(request, id):
    user = User.objects.get(id = id)
    data = {}
    data['firstName'] = user.firstName
    data['lastName'] = user.lastName
    data['email'] = user.email
    data['id'] = user.id

    return JsonResponse(data, safe=False)


def user_create(response):
    if request.method == 'POST':
            form = UserForm(request.body)
            if form.is_valid:
                user = form.save()
                return redirect('user')
    else:
        form = UserForm()
        return render({"error": "cannot update"})

