from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Mug
class MugListView(ListView):
	paginate_by = 5
	model = models.Mug

class MugDetailView(DetailView):
	model = models.Mug

class MugUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Mug
	fields = "__all__"
	success_url = "/moominmugs"

class MugDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Mug
	success_url = "/moominmugs"

class MugCreateView(LoginRequiredMixin, CreateView):
	model = models.Mug
	fields = "__all__"
	success_url = "/moominmugs"

# Figure
class FigureListView(ListView):
	paginate_by = 10
	model = models.Figure

class FigureUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Figure
	fields = ["name"]
	success_url = "/figures"

class FigureDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Figure
	success_url = "/figures"

class FigureCreateView(LoginRequiredMixin, CreateView):
	model = models.Figure
	fields = ["name"]
	success_url = "/figures"

# Color
class ColorListView(ListView):
	paginate_by = 10
	model = models.Color

class ColorUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Color
	fields = ["name"]
	success_url = "/colors"

class ColorDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Color
	success_url = "/colors"

class ColorCreateView(LoginRequiredMixin, CreateView):
	model = models.Color
	fields = ["name"]
	success_url = "/colors"

# Theme
class ThemeListView(ListView):
	paginate_by = 10
	model = models.Theme

class ThemeUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Theme
	fields = ["name"]
	success_url = "/themes"

class ThemeDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Theme
	success_url = "/themes"

class ThemeCreateView(LoginRequiredMixin, CreateView):
	model = models.Theme
	fields = ["name"]
	success_url = "/themes"
