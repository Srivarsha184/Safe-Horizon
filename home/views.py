'''
from django.shortcuts import render,HttpResponse
from home import models
'''

'''
from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from .models import Report
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Report
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method=="POST":
        email_id=request.POST('email_id')
        password=request.POST('password')
        ins=login(email_id=email_id,password=password)
        ins.save()
        print("data written")
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

def signup(request):
    return HttpResponse("Signup")

def main(request):
    return render(request,'main.html')

def login(request):
    return render(request,'login.html')


def dashboard(request):
    return render(request,'dashboard.html')
'''

from django.shortcuts import render


def main(request):
    return render(request,'main.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

# Custom login logic
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if (username == 'Siri0111' and password == 'Siri0111') or (username == 'Varsha05' and password == 'srivarsha05'):
            request.session['admin_authenticated'] = True
            return redirect('admindashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'adminlogin.html')

# Custom decorator for authentication
def admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.session.get('admin_authenticated'):
            return redirect('adminlogin')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

@admin_required

def admindashboard(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'admindashboard.html', {'user_profiles': user_profiles})



# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def delete_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.delete()
            return redirect('delete_user')
        except User.DoesNotExist:
            return render(request, 'delete_user.html', {'error_message': 'User not found.'})
    return render(request, 'delete_user.html')


def logout(request):
    request.session.flush()
    return redirect('main')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Adjust the 'home' redirect to your desired page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, UserProfileForm

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # username = user_form.cleaned_data.get('username')
            # raw_password = user_form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('user_login')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def dashboard(request):
    return render(request,'dashboard.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import UserProfile
# from .forms import UserProfileForm

# @login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm








# from django.shortcuts import render, redirect
# from .models import UserProfile
# from .forms import UserProfileForm

# def profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_profile)
#     return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})


from .models import Incident

def yourreports(request):
    incidents = Incident.objects.filter(reported_by=request.user)
    return render(request, 'yourreports.html', {'incidents': incidents})


# def adminreports(request):
#     return render(request,'adminreports.html')

from django.shortcuts import render
from .models import Incident, UserProfile

def adminreports(request):
    incidents = Incident.objects.all()
    return render(request, 'adminreports.html', {'incidents': incidents})


# def analysis(request):
#     return render(request,'analysis.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentForm
from .models import Incident

@login_required
def report(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            new_incident = form.save(commit=False)
            new_incident.user = request.user
            new_incident.reported_by = request.user

            new_incident.save()
            messages.success(request, 'Incident report submitted successfully.')
            return redirect('dashboard')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = IncidentForm()
    
    return render(request, 'report.html', {'form': form})




import json
from .models import Incident
from django.db.models import Count
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    
    # Generate a list of graduation years
    grad_years = range(2024, 2030)
    
    return render(request, 'profile.html', {
        'form': form,
        'user_profile': user_profile,
        'grad_years': grad_years
    })
