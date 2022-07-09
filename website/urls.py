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
    path('editmember', views.editmember, name='editmember'),
]