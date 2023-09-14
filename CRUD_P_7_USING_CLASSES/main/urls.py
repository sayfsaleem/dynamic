from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home.as_view(),name="addshow"),
    path('delete/<int:id>/',views.Delete.as_view(),name="delete"),
    path('update/<int:id>',views.Update.as_view(),name='update'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/<str:name>/', views.ProfileView.as_view(), name='profile'),
    path('register/',views.register,name='register'),
]
