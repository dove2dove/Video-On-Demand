from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('genres/', views.Genres_List.as_view(), name='GenreList'),
    path('genres/<int:pk>/', views.Genres_Details.as_view(), name='GenreDetails'),
    path('general/', views.General_List.as_view()),
    path('general/<int:pk>/', views.General_Details.as_view()),
    path('subscriptionplan/', views.SubscriptionPlan_List.as_view()),
    path('subscriptionplan/<int:pk>/', views.SubscriptionPlan_Details.as_view()),
    path('accounts/', views.Account_List.as_view()),
    path('accounts/<int:pk>/', views.Account_Details.as_view()),
    path('category/', views.Category_List.as_view()),
    path('category/<int:pk>/', views.Category_Details.as_view()),
    path('movies/', views.Movies_List.as_view()),
    path('movies/<int:pk>/', views.Movies_Details.as_view()),
    path('subscription/', views.Subscriptions_List.as_view()),
    path('subscription/<int:pk>/', views.Subscriptions_Details.as_view()),
    path('watchlist/', views.WatchList_List.as_view()),
    path('watchlist/<int:pk>/', views.WatchList_Details.as_view()),
    path('watchlog/', views.WatchLog_List.as_view()),
    path('watchlog/<int:pk>/', views.WatchLog_Details.as_view()),
    path('adverts/', views.Adverts_List.as_view()),
    path('adverts/<int:pk>/', views.Adverts_Details.as_view()),
    path('actors/', views.Actors_List.as_view()),
    path('actors/<int:pk>/', views.Actors_Details.as_view()),
    path('moviegenreMap/', views.MovieGenreMap_List.as_view()),
    path('moviegenreMap/<int:pk>/', views.MovieGenreMap_Details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
