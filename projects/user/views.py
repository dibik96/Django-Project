from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			# After created account we logged in to same account
			login(request,form.save())
			# For no need to logged in after account follow below code 
			# we can create user from the admin login page
			# form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has beed created {username} and logged in successfully')
			return redirect('blogs:blog-post')
	else:
		#to load empty form
		form = UserRegisterForm()

	return render(request,'users/register.html', {'form':form,'title':'Signup'})



#TODO: This is another method of login custom
#currently this method is not using only for testing purpose
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# Pass request & user as a param into the login function
			login(request,form.get_user())
			messages.success(request,f'Your login successfully')
			# If user directly wants to open other page then
			# then we can leave them to their desired page once logged In.
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('profile')
	else:
		form = AuthenticationForm()

	return render(request,'users/login.html', {'form':form,'title':'Signup'})



def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html',{'title':'Logout'})


# @login_required(login_url="login")
@login_required
def profile(request):
	return render(request,'users/profile.html',{'title':'Profile'})






