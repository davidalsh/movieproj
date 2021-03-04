from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Category
from .forms import ReviewForm


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
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
