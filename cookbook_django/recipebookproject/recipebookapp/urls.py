from django.urls import path
from django.conf.urls.static import static
from . import views
from recipebookproject import settings

app_name = "recipebookapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('logout/', views.user_logout, name='logout'),
    path('cooker/', views.cooker, name='cooker'),
    path('recipe_add/', views.recipe_add, name='recipe_add'),
    path('recipe_edit/<int:recipe_id>/', views.recipe_edit, name='recipe_edit'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe_delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
handler500 = views.handler500
