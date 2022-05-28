from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models

# Mug
class MugListView(ListView):
	model = models.Mug

class MugDetailView(DetailView):
	model = models.Mug

class MugUpdateView(UpdateView):
	model = models.Mug
	fields = "__all__"
	success_url = "/moominmugs"

class MugDeleteView(DeleteView):
	model = models.Mug
	success_url = "/moominmugs"

class MugCreateView(CreateView):
	model = models.Mug
	fields = "__all__"
	success_url = "/moominmugs"

# Figure
class FigureListView(ListView):
	model = models.Figure

class FigureUpdateView(UpdateView):
	model = models.Figure
	fields = ["name"]
	success_url = "/figures"

class FigureDeleteView(DeleteView):
	model = models.Figure
	success_url = "/figures"

class FigureCreateView(CreateView):
	model = models.Figure
	fields = ["name"]
	success_url = "/figures"

# Color
class ColorListView(ListView):
	model = models.Color

class ColorUpdateView(UpdateView):
	model = models.Color
	fields = ["name"]
	success_url = "/colors"

class ColorDeleteView(DeleteView):
	model = models.Color
	success_url = "/colors"

class ColorCreateView(CreateView):
	model = models.Color
	fields = ["name"]
	success_url = "/colors"

# Theme
class ThemeListView(ListView):
	model = models.Theme

class ThemeUpdateView(UpdateView):
	model = models.Theme
	fields = ["name"]
	success_url = "/themes"

class ThemeDeleteView(DeleteView):
	model = models.Theme
	success_url = "/themes"

class ThemeCreateView(CreateView):
	model = models.Theme
	fields = ["name"]
	success_url = "/themes"
