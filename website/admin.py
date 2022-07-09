from django.contrib import admin
from .models import Author, Review, Reviewer, Paper

admin.site.register(Author)
admin.site.register(Reviewer)
admin.site.register(Paper)
admin.site.register(Review)
# Register your models here.
