from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movies/categorytype/', views.MovieByCategoryAndType.as_view(), name='Movie_Category_Type_List'),
]

urlpatterns = format_suffix_patterns(urlpatterns)