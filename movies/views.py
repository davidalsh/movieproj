from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Category, Actor, Genre
from .forms import ReviewForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False)


class MoviesView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/moviesingle.html"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        mov = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = mov
            form.save()
        return redirect(mov.get_absolute_url())


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):
    template_name = 'movies/movies.html'

    def get_queryset(self):
        queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist("year")) |
                                        Q(genres__in=self.request.GET.getlist("genre")))
        return queryset


class JsonFilterMoviesView(ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist("year")) |
                                        Q(genres__in=self.request.GET.getlist("genre"))).distinct().values("title", "tagline", "url", "poster")

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
