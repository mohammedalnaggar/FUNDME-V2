from django.urls import path
from userProfile import views

# SET THE NAMESPACE!
app_name = 'userProfile'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('create_project/', views.register, name='create_project')

]
