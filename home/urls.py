from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Inicio.as_view(), name="inicio"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    
    path('detail/profile/<int:pk>/', views.DetailProfile.as_view(), name="detail_profile"),
    path('update/profile/<int:pk>/', views.UpdateProfile.as_view(), name="update_profile"),

    path('ubicacion/', views.Ubicacion.as_view(), name="ubicacion"),
    path('nosotros/', views.Nosotros.as_view(), name="nosotros"),
]
