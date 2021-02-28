from django.urls import path
from . import views

urlpatterns = [
    path("<str:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("", views.MoviesView.as_view(), name='home'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review')
]
