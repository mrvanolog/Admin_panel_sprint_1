from django.contrib import admin
from .models import Movie, Series, Director, Actor, Writer, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("title", "creation_date", "rating")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "title",
        "description",
        "creation_date",
        "age_restriction",
        "rating",
        "directors",
        "actors",
        "writers",
        "genres",
        "file_path"
    )

    # поиск по полям
    search_fields = ('title', 'description', 'id')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("title", "creation_date", "rating")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "title",
        "description",
        "creation_date",
        "age_restriction",
        "rating",
        "directors",
        "actors",
        "writers",
        "genres",
        "file_path"
    )

    # поиск по полям
    search_fields = ('title', 'description', 'id')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("first_name", "last_name")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "first_name",
        "last_name"
    )

    # поиск по полям
    search_fields = ("first_name", "last_name")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("first_name", "last_name")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "first_name",
        "last_name"
    )

    # поиск по полям
    search_fields = ("first_name", "last_name")


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("first_name", "last_name")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "first_name",
        "last_name"
    )

    # поиск по полям
    search_fields = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("name", "description")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "name",
        "description"
    )

    # поиск по полям
    search_fields = ("name", "description")
