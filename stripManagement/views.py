from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import stripManagement.models


def index(request):
    return render(request, 'index.html', {})


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lasttname = request.POST['first_name']
        email = request.POST['email']
        matricule = request.POST['matricule']
        # phone_number = request.POST['tel']
        service = request.POST['service']
        password = request.POST['password']

        user = stripManagement.models.users.objects.create(username=username, password=password, first_name=firstname,
                                                           last_name=lasttname,
                                                            email=email, matricule=matricule,

                                                           )
        print(user.save())
        if user is not None:
            user.save()
            return redirect('register')
        else:
            return render(request, 'authenticate/register.html', {'error': 'matricule or password is incorrect'})

    return render(request, 'authenticate/register.html')


def login_user(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        password = request.POST['password']

        user = auth.authenticate(password=password, matricule=matricule)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            # messages.success(request, 'There was an error logging in, Try Again...')
            return render(request, 'authenticate/login.html', {'error': 'matricule or password is incorrect'})
    else:
        return render(request, 'authenticate/login.html', {})


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
