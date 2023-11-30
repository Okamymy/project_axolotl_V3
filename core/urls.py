from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('create/recamara/', views.CreateRecamara.as_view(), name="create_recamara"),
    path('list/recamara/', views.ListRecamara.as_view(), name="list_recamara"),
    path('detail/recamara/<int:pk>/', views.DetailRecamara.as_view(), name="detail_recamara"),
    path('update/recamara/<int:pk>/', views.UpdateRecamara.as_view(), name="update_recamara"),
    path('delete/recamara/<int:pk>/', views.DeleteRecamara.as_view(), name="delete_recamara"),

    path('create/bano/', views.CreateBano.as_view(), name="create_bano"),
    path('list/bano/', views.ListBano.as_view(), name="list_bano"),
    path('detail/bano/<int:pk>/', views.DetailBano.as_view(), name="detail_bano"),
    path('update/bano/<int:pk>/', views.UpdateBano.as_view(), name="update_bano"),
    path('delete/bano/<int:pk>/', views.DeleteBano.as_view(), name="delete_bano"),

    path('create/cocina/', views.CreateCocina.as_view(), name="create_cocina"),
    path('list/cocina/', views.ListCocina.as_view(), name="list_cocina"),
    path('detail/cocina/<int:pk>/', views.DetailCocina.as_view(), name="detail_cocina"),
    path('update/cocina/<int:pk>/', views.UpdateCocina.as_view(), name="update_cocina"),
    path('delete/cocina/<int:pk>/', views.DeleteCocina.as_view(), name="delete_cocina"),

    path('create/comedor/', views.CreateComedor.as_view(), name="create_comedor"),
    path('list/comedor/', views.ListComedor.as_view(), name="list_comedor"),
    path('detail/comedor/<int:pk>/', views.DetailComedor.as_view(), name="detail_comedor"),
    path('update/comedor/<int:pk>/', views.UpdateComedor.as_view(), name="update_comedor"),
    path('delete/comedor/<int:pk>/', views.DeleteComedor.as_view(), name="delete_comedor"),

    path('create/sala/', views.CreateSala.as_view(), name="create_sala"),
    path('list/sala/', views.ListSala.as_view(), name="list_sala"),
    path('detail/sala/<int:pk>/', views.DetailSala.as_view(), name="detail_sala"),
    path('update/sala/<int:pk>/', views.UpdateSala.as_view(), name="update_sala"),
    path('delete/sala/<int:pk>/', views.DeleteSala.as_view(), name="delete_sala"),

    path('create/oficina/', views.CreateOficina.as_view(), name="create_oficina"),
    path('list/oficina/', views.ListOficina.as_view(), name="list_oficina"),
    path('detail/oficina/<int:pk>/', views.DetailOficina.as_view(), name="detail_oficina"),
    path('update/oficina/<int:pk>/', views.UpdateOficina.as_view(), name="update_oficina"),
    path('delete/oficina/<int:pk>/', views.DeleteOficina.as_view(), name="delete_oficina"),
]