from django.contrib import admin
from .models import Genre, Movie

@admin.register(Genre)
class AdminModelGanre(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Movie)
class AdminModelMovie(admin.ModelAdmin):
    list_display = ["id", "title", 'number_in_stock', 'daily_rate']
    search_fields = ["name"]


