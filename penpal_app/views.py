from django.shortcuts import render
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

    return JsonResponse(user, safe=False)
