from django.contrib import admin
from .models import FilmWork, Person, Genre


class PersonInLineAdmin(admin.TabularInline):
    model = FilmWork.persons.through


class GenreInLineAdmin(admin.TabularInline):
    model = FilmWork.genres.through


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("title", "type", "creation_date", "rating")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "id",
        "title",
        "type",
        "description",
        "creation_date",
        "rating",
        "certificate",
        "file_path"
    )

    inlines = (PersonInLineAdmin, GenreInLineAdmin)

    # поиск по полям
    search_fields = ('title', 'description', 'type', "genres")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("full_name", "birth_date")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "id",
        "full_name",
        "birth_date"
    )

    # поиск по полям
    search_fields = ('full_name', 'birth_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ("name", "description")
    # порядок следования полей в форме создания/редактирования
    fields = (
        "id",
        "name",
        "description"
    )

    # поиск по полям
    search_fields = ("name", "description")
