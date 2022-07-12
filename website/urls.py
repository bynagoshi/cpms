from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name='about'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('submission', views.submission, name='submission'),
    path('review', views.review, name='review'),
    path('submitpaper', views.submitpaper, name='submitpaper'),
    path('reviewdownload', views.reviewdownload, name='reviewdownload'),
    path('reviewerdashboard', views.reviewerdashboard, name='reviewerdashboard'),
    path('reviewersubmit', views.reviewersubmit, name='reviewersubmit'),
    path('revieweredit', views.revieweredit, name='revieweredit'),
    path('authoredit', views.authoredit, name='authoredit'),
    path('authordashboard', views.authordashboard, name='authordashboard'),
]