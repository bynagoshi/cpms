from django import forms
from django.forms import ModelForm
from .models import Author, Reviewer, Paper
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
  


class AuthorRegistration(ModelForm):
    class Meta:
        model = Author

        fields = ('FName', 'MiddleInitial', 'LName', 'Affliation', 'Department',
         'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')
        
        labels = {
            'FName': '',
            'MiddleInitial': '',
            'LName': '',
            'Affliation': '',
            'Department': '',
            'Address': '',
            'City': '',
            'State': '',
            'Zipcode': '',
            'PhoneNumber': '',
            'Email': '',
        }

        widgets = {
            'FName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name'}),
            'MiddleInitial': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Middle Initial'}),
            'LName': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'Affliation': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Affliation'}),
            'Department': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'City': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'State': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
            'Zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ZipCode'}),
            'PhoneNumber': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PhoneNumber'}),
            'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
        }



class ReviewerRegistration(ModelForm):
    class Meta:
        model = Reviewer
        fields = ('FName', 'MiddleInitial', 'LName', 'Affliation', 'Department',
         'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email', 'Topic', 'OtherDescription')

        labels = {
            'FName': '',
            'MiddleInitial': '',
            'LName': '',
            'Affliation': '',
            'Department': '',
            'Address': '',
            'City': '',
            'State': '',
            'Zipcode': '',
            'PhoneNumber': '',
            'Email': '',
            'Topic':'',
            'OtherDescription':'',
        }

        widgets = {
            'FName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name'}),
            'MiddleInitial': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Middle Initial'}),
            'LName': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'Affliation': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Affliation'}),
            'Department': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'City': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'State': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
            'Zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ZipCode'}),
            'PhoneNumber': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PhoneNumber'}),
            'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'Topic': forms.Select(attrs={'class':'form-control','placeholder':'Select Topic'}),
            'OtherDescription': forms.TextInput(attrs={'class':'form-control','placeholder':'Other'}),
        }

class FileSubmissionForm(ModelForm):
    class Meta:
        model = Paper
        fields = (
            'File', 'Title','Topic','OtherDescription', 'Certification','NotesToReviewers'
        )

        labels = {
            'File':'',
            'Title':'',
            'Certification':'',
            'NotesToReviewers':'',
            'Topic':'',
            'OtherDescription':'',
        }

        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'Certification': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Certification'}),
            'Topic': forms.Select(attrs={'class':'form-control','placeholder':'Select Topic'}),
            'OtherDescription': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Other'}),
            'NotesToReviewers': forms.Textarea(attrs={'class':'form-control','placeholder':'Note to reviewer'}),  
        }