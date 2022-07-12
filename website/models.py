from django.db import models
from django.contrib.auth.models import User

#Database for website

class Author(models.Model):
    user_ref = models.OneToOneField(User, on_delete=models.CASCADE, default=None,primary_key=True)
    FName = models.CharField(max_length = 50)
    MiddleInitial = models.CharField(max_length=1)
    LName = models.CharField(max_length= 50)
    Affliation = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 2)
    Zipcode = models.CharField(max_length = 10)
    PhoneNumber = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 100)



CHOICES = (
    ('AnalysisOfAlgorithms','AnalysisOfAlgorithms'),
    ('Application','Application'),
    ('Architecture','Architecture'),
    ('ArtificialIntelligence','ArtificialIntelligence'),
    ('ComputerEngineering','ComputerEngineering'),
    ('Curriculum','Curriculum'),
    ('DataStructures','DataStructures'),
    ('Databases','Databases'),
    ('DistanceLearning','DistanceLearning'),
    ('DistributedSystems','DistributedSystems'),
    ('EthicalSocietalIssues','EthicalSocietalIssues'),
    ('FirstYearComputing','FirstYearComputing'),
    ('GenderIssues','GenderIssues'),
    ('GrantWriting','GrantWriting'),
    ('GraphicsImageProcessing','GraphicsImageProcessing'),
    ('HumanComputerInteraction','HumanComputerInteraction'),
    ('LaboratoryEnvironments','LaboratoryEnvironments'),
    ('Literacy','Literacy'),
    ('MathematicsInComputing','MathematicsInComputing'),
    ('Multimedia','Multimedia'),
    ('NetworkingDataCommunications','NetworkingDataCommunications'),
    ('NonMajorCourses','NonMajorCourses'),
    ('ObjectOrientedIssues','ObjectOrientedIssues'),
    ('OperatingSystems','OperatingSystems'),
    ('ParallelProcessing','ParallelProcessing'),
    ('Pedagogy','Pedagogy'),
    ('ProgrammingLanguages','ProgrammingLanguages'),
    ('Research','Research'),
    ('Security','Security'),
    ('SoftwareEngineering','SoftwareEngineering'),
    ('SystemsAnalysisAndDesign','SystemsAnalysisAndDesign'),
    ('UsingTechnologyInTheClassroom','UsingTechnologyInTheClassroom'),
    ('WebAndInternetProgramming','WebAndInternetProgramming'),
    ('Other','Other'),)

class Reviewer(models.Model):
    user_ref = models.OneToOneField(User, on_delete=models.CASCADE, default=None,primary_key=True)
    Active = models.BooleanField(null=True,default=True)
    FName = models.CharField(max_length = 50)
    MiddleInitial = models.CharField(max_length=1)
    LName = models.CharField(max_length= 50)
    Affliation = models.CharField(max_length = 50)
    Department = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 2)
    Zipcode = models.CharField(max_length = 10)
    PhoneNumber = models.CharField(max_length = 50)
    Email = models.CharField(max_length = 100)
    Topic = models.CharField(max_length = 50, choices=CHOICES, default=None)
    OtherDescription = models.CharField(max_length=50, null=True, default = None, blank = True)
    ReviewsAcknowledged = models.BooleanField(null=True, default=False)

class Paper(models.Model):
    author_ref = models.ForeignKey(Author,null=True,on_delete=models.CASCADE,)
    File = models.FileField(default=None)
    Title = models.CharField(max_length=50)
    Certification = models.CharField(max_length=3)
    NotesToReviewers = models.TextField()
    BeingReviewed = models.BooleanField(null=True, default = False)
    Topic = models.CharField(max_length = 50, choices=CHOICES, default=None)
    OtherDescription = models.CharField(max_length=50, null=True, default = None, blank = True)

class Review(models.Model):
    paper_ref = models.ForeignKey(Paper,null=True,on_delete=models.CASCADE)
    reviewer_ref = models.ForeignKey(Reviewer,null=True,on_delete=models.CASCADE)
    AppropriatenessOfTopic = models.DecimalField(max_digits = 3, decimal_places = 2)
    TimelinessOfTopic = models.DecimalField(max_digits = 3, decimal_places = 2)
    SupportiveEvidence = models.DecimalField(max_digits = 3, decimal_places = 2)
    TechnicalQuality = models.DecimalField(max_digits = 3, decimal_places = 2)
    ScopeOfCoverage = models.DecimalField(max_digits = 3, decimal_places = 2)
    CitationOfPreviousWork = models.DecimalField(max_digits = 3, decimal_places = 2)
    Originality = models.DecimalField(max_digits = 3, decimal_places = 2)
    ContentComments = models.TextField()
    ClarityOfMainMessage = models.DecimalField(max_digits = 3, decimal_places = 2)
    OrganizationOfPaper = models.DecimalField(max_digits = 3, decimal_places = 2)
    Mechanics = models.DecimalField(max_digits = 3, decimal_places = 2)
    WrittenDocumentComments = models.TextField()
    SuitabilityForPresentation = models.DecimalField(max_digits = 3, decimal_places = 2)
    PotentialInterestInTopic = models.DecimalField(max_digits = 3, decimal_places = 2)
    PotentialForOralPresentationComments = models.TextField()
    OverallRating = models.DecimalField(max_digits = 3, decimal_places = 2)
    OverallRatingComments = models.TextField()
    ComfortLevelTopic = models.DecimalField(max_digits = 3, decimal_places = 2)
    ComfortLevelAcceptability = models.DecimalField(max_digits = 3, decimal_places = 2)
    Complete = models.BooleanField(null=True, default=True)


    

# Create your models here.
