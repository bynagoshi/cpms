from django import forms
from django.forms import ModelForm
from .models import Author, Reviewer, Paper, Review
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
         'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email','Topic','OtherDescription')

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

class EditAuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = ('Affliation', 'Department', 'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email')

        exclude = ('FName', 'MiddleInitial', 'LName',)

        
        labels = {
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
            'Affliation': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Affliation'}),
            'Department': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'City': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'State': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),
            'Zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ZipCode'}),
            'PhoneNumber': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter PhoneNumber'}),
            'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
        }

class EditReviewerForm(ModelForm):

    class Meta:
        model = Reviewer
        fields = ('Affliation', 'Department', 'Address', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Email', 'Topic', 'OtherDescription')

        exclude = ('FName', 'MiddleInitial', 'LName',)

        
        labels = {
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

class ReviewerSubmissionForm(ModelForm):
   Title = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Paper'}))

   class Meta:
       model = Review
       fields = ('AppropriatenessOfTopic', 'TimelinessOfTopic', 'SupportiveEvidence', 'TechnicalQuality', 'ScopeOfCoverage',
        'CitationOfPreviousWork', 'Originality', 'ContentComments', 'ClarityOfMainMessage', 'OrganizationOfPaper', 'Mechanics', 'WrittenDocumentComments',
         'SuitabilityForPresentation', 'PotentialInterestInTopic', 'PotentialForOralPresentationComments', 'OverallRating', 'OverallRatingComments', 'ComfortLevelTopic', 'ComfortLevelAcceptability')
    
       labels = {
           'AppropriatenessOfTopic':'',
           'TimelinessOfTopic':'',
           'SupportiveEvidence':'',
           'TechnicalQuality':'',
           'ScopeOfCoverage':'',
           'CitationOfPreviousWork':'',
           'Originality':'',
           'ContentComments':'',
           'ClarityOfMainMessage':'',
           'OrganizationOfPaper':'',
           'Mechanics':'',
           'WrittenDocumentComments':'',
           'SuitabilityForPresentation':'',
           'PotentialInterestInTopic':'',
           'PotentialForOralPresentationComments':'',
           'OverallRating':'',
           'OverallRatingComments':'',
           'ComfortLevelTopic':'',
           'ComfortLevelAcceptability':'',
       }

       widgets = {
            'AppropriatenessOfTopic': forms.NumberInput(attrs={'class':'form-control','placeholder':'AppropriatenessOfTopic'}),
            'TimelinessOfTopic': forms.NumberInput(attrs={'class':'form-control','placeholder':'TimelinessOfTopic'}),
            'SupportiveEvidence': forms.NumberInput(attrs={'class':'form-control','placeholder':'SupportiveEvidence'}),
            'TechnicalQuality': forms.NumberInput(attrs={'class':'form-control','placeholder':'AppropriatenessOfTopic'}),
            'ScopeOfCoverage': forms.NumberInput(attrs={'class':'form-control','placeholder':'TechnicalQuality'}),
            'CitationOfPreviousWork': forms.NumberInput(attrs={'class':'form-control','placeholder':'CitationOfPreviousWork'}),
            'Originality': forms.NumberInput(attrs={'class':'form-control','placeholder':'Originality'}),
            'ContentComments': forms.Textarea(attrs={'class':'form-control','placeholder':'ContentComments'}),
            'ClarityOfMainMessage': forms.NumberInput(attrs={'class':'form-control','placeholder':'ClarityOfMainMessage'}),
            'OrganizationOfPaper': forms.NumberInput(attrs={'class':'form-control','placeholder':'OrganizationOfPaper'}),
            'Mechanics': forms.NumberInput(attrs={'class':'form-control','placeholder':'Mechanics'}),
            'WrittenDocumentComments': forms.Textarea(attrs={'class':'form-control','placeholder':'WrittenDocumentComments'}),
            'SuitabilityForPresentation': forms.NumberInput(attrs={'class':'form-control','placeholder':'SuitabilityForPresentation'}),
            'PotentialInterestInTopic': forms.NumberInput(attrs={'class':'form-control','placeholder':'PotentialInterestInTopic'}),
            'PotentialForOralPresentationComments': forms.Textarea(attrs={'class':'form-control','placeholder':'PotentialForOralPresentationComments'}),
            'OverallRating': forms.NumberInput(attrs={'class':'form-control','placeholder':'OverallRating'}),
            'OverallRatingComments': forms.Textarea(attrs={'class':'form-control','placeholder':'OverallRatingComments'}),
            'ComfortLevelTopic': forms.NumberInput(attrs={'class':'form-control','placeholder':'ComfortLevelTopic'}),
            'ComfortLevelAcceptability': forms.NumberInput(attrs={'class':'form-control','placeholder':'ComfortLevelAcceptability'}),
       }