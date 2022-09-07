from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:pk>',views.post,name="post"),
   path('<str:pk>',views.movies,name="movies"),
    path('movie/stream',views.Stream.as_view(),name="stream"),
]
