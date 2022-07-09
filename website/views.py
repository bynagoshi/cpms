from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import AuthorRegistration, ReviewerRegistration, FileSubmissionForm
from django.http import HttpResponseRedirect
from .models import Paper, Reviewer

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def reviewdownload(request):
	reviewer_topic = Reviewer.objects.get(user_id = request.user)
	file = Paper.objects.get(Topic = reviewer_topic.Topic, BeingReviewed = False)
	if(file == None):
		response = redirect('reviewdownload')
		return response
	
	print(file.File)
	#if Paper.objects.get(Topic=(hasattr(request.user, "reviewer").Topic)):
		#print("YES")

	return render(request, 'reviewdownload.html', {'file':file})
#hasattr(request.user, "reviewer").Topic
def submission(request):
	
	if request.user.is_authenticated and hasattr(request.user, "author"):
		response = redirect('submitpaper')
		return response
	if request.user.is_authenticated:
		submitted = False
		if request.method == "POST":
			form = AuthorRegistration(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/submission?submitted=True')
		else:
			form = AuthorRegistration
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'submission.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('register')
		return response

def review(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		response = redirect('reviewdownload')
		return response
	if request.user.is_authenticated:
		submitted = False
		if request.method == "POST":
			form = ReviewerRegistration(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/review?submitted=True')
		else:
			form = ReviewerRegistration
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'review.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('register')
		return response

def submitpaper(request):
	submitted = False
	if request.method == "POST":
		form = FileSubmissionForm(request.POST, request.FILES)
		if form.is_valid():
			author_instance = author.objects.get(user = request.user)
			instance = form.save(commit=False)
			instance.author_ref = author_instance.user
			instance.save
			return HttpResponseRedirect('/submitpaper?submitted=True')
	else:
		form = FileSubmissionForm
		if 'submitted' in request.GET:
			submitted == True
	return render(request, 'submitpaper.html', {'form':form, 'submitted':submitted})
	
def editmember(request):
	return render(request, 'editmember.html', {})

def register_request(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password= password)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
	else:
		form = RegisterUserForm()
		messages.error(request, "Unsuccessful registration. Invalid information.")

	return render (request, "register.html", {"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
