from django.contrib import admin
from django.urls import path
from moominmugs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moominmugs/', views.MugListView.as_view()),
    path('moominmugs/<int:pk>', views.MugDetailView.as_view()),
    path('moominmugs/<int:pk>/update', views.MugUpdateView.as_view()),
    path('moominmugs/<int:pk>/delete', views.MugDeleteView.as_view()),
    path('moominmugs/new', views.MugCreateView.as_view()),

    path('colors/', views.ColorListView.as_view()),
    path('colors/<int:pk>/update', views.ColorUpdateView.as_view()),
    path('colors/<int:pk>/delete', views.ColorDeleteView.as_view()),
    path('colors/new', views.ColorCreateView.as_view()),
    
    path('figures/', views.FigureListView.as_view()),
    path('figures/<int:pk>/update', views.FigureUpdateView.as_view()),
    path('figures/<int:pk>/delete', views.FigureDeleteView.as_view()),
    path('figures/new', views.FigureCreateView.as_view()),
    
    path('themes/', views.ThemeListView.as_view()),
    path('themes/<int:pk>/update', views.ThemeUpdateView.as_view()),
    path('themes/<int:pk>/delete', views.ThemeDeleteView.as_view()),
    path('themes/new', views.ThemeCreateView.as_view()),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
