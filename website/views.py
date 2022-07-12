from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import AuthorRegistration, ReviewerRegistration, FileSubmissionForm, EditAuthorForm, EditReviewerForm,ReviewerSubmissionForm
from django.http import HttpResponseRedirect
from .models import Paper, Reviewer, Author
from django.core.exceptions import *
from django.http import HttpResponse

#Handles homepage
def index(request):
    return render(request, 'index.html', {})

#Handles about us page
def about(request):
    return render(request, 'about.html', {})

################################################################################################################
#Reviewer section of website.																                   #	
################################################################################################################
def reviewerdashboard(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		reviewer_topic = Reviewer.objects.get(user_ref = request.user)	
		file = Paper.objects.filter(Topic = reviewer_topic.Topic, BeingReviewed = False).first()
		return render(request,'reviewerdashboard.html', {'file':file})
	else:
		response = redirect('review')
		return response

def revieweredit(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		return render(request,'revieweredit.html')
	else:
		response = redirect('review')
		return response

def reviewersubmit(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		submitted = False
		if request.method == "POST":
			form = ReviewerSubmissionForm(request.POST)
			if form.is_valid():
				title_of_paper = form.cleaned_data.get("Title")
				instance = form.save(commit = False)
				instance.reviewer_ref = Reviewer.objects.get(user_ref = request.user)
				try:
					instance.paper_ref= Paper.objects.get(Title=title_of_paper)
				except Paper.DoesNotExist:
					return HttpResponse('Exception: Paper not found')

				instance.save()
				return HttpResponseRedirect('/reviewersubmit?submitted=True')
		else:
			form = ReviewerSubmissionForm
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'reviewersubmit.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('review')
		return response

def reviewdownload(request):
	reviewer_topic = Reviewer.objects.get(user_ref = request.user)
	file = Paper.objects.filter(Topic = reviewer_topic.Topic, BeingReviewed = False).first()
	if(file == None):
		response = redirect('reviewdownload')
		return response
	
	print(file.File)
	#if Paper.objects.get(Topic=(hasattr(request.user, "reviewer").Topic)):
		#print("YES")

	return render(request, 'reviewdownload.html', {'file':file})

def revieweredit(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		reviewer_ref = Reviewer.objects.get(user_ref = request.user)
		submitted = False
		if request.method == "POST":
			form = EditReviewerForm(request.POST, instance = reviewer_ref)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/revieweredit?submitted=True')
		else:
			form = EditReviewerForm
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'revieweredit.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('review')
		return response

def review(request):
	if request.user.is_authenticated and hasattr(request.user, "reviewer"):
		response = redirect('reviewerdashboard')
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

################################################################################################################
#Author section of website.	    	  														                   #	
################################################################################################################

def authoredit(request):
	if request.user.is_authenticated and hasattr(request.user, "author"):
		author_ref = Author.objects.get(user_ref = request.user)
		submitted = False
		if request.method == "POST":
			form = EditAuthorForm(request.POST, instance = author_ref)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/authoredit?submitted=True')
		else:
			form = EditAuthorForm
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'authoredit.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('review')
		return response

def authordashboard(request):
	if request.user.is_authenticated and hasattr(request.user, "author"):
		return render(request,'authordashboard.html')
	else:
		response = redirect('review')
		return response

def submission(request):
	
	if request.user.is_authenticated and hasattr(request.user, "author"):
		response = redirect('authordashboard')
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

def submitpaper(request):
	if request.user.is_authenticated and hasattr(request.user, "author"):
		submitted = False
		if request.method == "POST":
			form = FileSubmissionForm(request.POST, request.FILES)
			if form.is_valid():
				author_instance = Author.objects.get(user_ref = request.user)
				instance = form.save(commit = False)
				instance.author_ref = Author.objects.get(user_ref = request.user)
				instance.save()
				return HttpResponseRedirect('/submitpaper?submitted=True')
		else:
			form = FileSubmissionForm
			if 'submitted' in request.GET:
				submitted == True
		return render(request, 'submitpaper.html', {'form':form, 'submitted':submitted})
	else:
		response = redirect('submission')
		return response
	
################################################################################################################
#Login section of website.	    	  														                   #	
################################################################################################################


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
