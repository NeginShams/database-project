from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
from datetime import date



def homepage(request):
    #return HttpResponse("<h1>Hello, world. You're at the polls index.<h1>")
    return render(request, 'db_app/index.html')

def register_page(request):
    return render(request, 'db_app/register.html')

#@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        phone_number = request.POST['phone']
        birth_date = request.POST['birth_date']
        address = request.POST['address']
        gender = request.POST['gender']

        new_user = models.MyUser(name = first_name, last_name= last_name, phone_number = phone_number, address = address, birth_date=birth_date, gender=gender)
        new_user.save()
        return render(request, 'db_app/register_success.html')
    else:
        return HttpResponse('not post')

def user_list(request):
    users = models.MyUser.objects.all()

    return render(request, 'db_app/userlist.html', {'users':users})


def details(request):
    print(date.today())
    user_id = request.GET.get('id')
    user = models.MyUser.objects.get(id = user_id)
    return render(request, 'db_app/userdetail.html', {'user':user})
    # return HttpResponse(user)

    # user = request.GET.get('user')

def edit(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        #return HttpResponse(user_id)
        user = models.MyUser.objects.get(id = user_id)
        return render(request, 'db_app/edituser.html', {'user':user})

        # user = request.POST['user']
        # return HttpResponse(user)
        # return HttpResponse(user)

def edit_status(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        phone_number = request.POST['phone']
        birth_date = request.POST['birth_date']
        address = request.POST['address']
        gender = request.POST['gender']

        user_id = request.POST['user_id']
        user = models.MyUser.objects.get(id = user_id)

        user.name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.birth_date = birth_date
        user.address = address
        user.gender = gender

        user.save()
        #return HttpResponse("ok!!!")
        return render(request, 'db_app/edit_success.html')

