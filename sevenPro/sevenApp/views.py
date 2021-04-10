from django.shortcuts import render
from sevenApp.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def f_index(request):
    return render(request, 'sevenAppTemp/index.html')

def gro_gree(request):
    return render(request, 'sevenAppTemp/temp2.html')

# For Registration of New User
def register_fun(request):
    u_registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        userProfile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and userProfile_form.is_valid():
            r_user = user_form.save()
            r_user.set_password(r_user.password)
            r_user.save()

            r_prof = userProfile_form.save(commit = False)
            r_prof.tuser = r_user

            if 'prof_pict' in request.FILES:
                r_prof.prof_pict = request.FILES['prof_pict']

            r_prof.save()
            u_registered = True

        else:
            print(user_form.errors, userProfile_form.errors)

    else:
        user_form = UserForm()
        userProfile_form = UserProfileInfoForm()

    return render(request, 'sevenAppTemp/temp1.html', {'u_registered':u_registered,
                                                    'user_form':user_form,
                                                    'userProfile_form':userProfile_form})


# LogIn View
def user_login_fun(request):
    if request.method == 'POST':
        usr_name = request.POST.get('bro_name')             # these are getting from login form---login.html
        passwrd = request.POST.get('bro_password')

        user = authenticate(username = usr_name, password = passwrd)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('f_ind'))
            else:
                return HttpResponse(" Your account is not active ")
        else:
            print(" Someone tried to login and failed...")
            print("UserName : {}  Password : {} ".format(usr_name, passwrd))
            return HttpResponse(" Invalid Login Supplied ...")
    else:
        return render(request, 'sevenAppTemp/login.html', {})


# Logout purpose
@login_required
def user_logout_fun(request):
    logout(request)
    return HttpResponseRedirect(reverse('f_ind'))

# Cart Function
@login_required
def cart_fun(request):
    return render(request, 'sevenAppTemp/temp3.html', {})

