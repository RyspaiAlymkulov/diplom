from django.urls import path
from users import views

#Остальные урлы касательно Юзера
urlpatterns = [
    path('login/', views.LoginAPIview.as_view()),
    path('register/', views.RegisterAPIview.as_view()),
    # path('userprofile/', views.ProfileCreateListAPIview.as_view()),
]