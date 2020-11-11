from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from model_utils.models import TimeStampedModel


class Director(TimeStampedModel):
    first_name = models.CharField(_("имя"), max_length=255)
    last_name = models.CharField(_("фамилия"), max_length=255)
    # movies = models.ManyToManyField("Movie", blank=True)
    # series = models.ManyToManyField("Series", blank=True)

    class Meta:
        verbose_name = _("режиссер")
        verbose_name_plural = _("режиссеры")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Actor(TimeStampedModel):
    first_name = models.CharField(_("имя"), max_length=255)
    last_name = models.CharField(_("фамилия"), max_length=255)
    # movies = models.ManyToManyField("Movie", blank=True)
    # series = models.ManyToManyField("Series", blank=True)

    class Meta:
        verbose_name = _("актер")
        verbose_name_plural = _("актеры")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Writer(TimeStampedModel):
    first_name = models.CharField(_("имя"), max_length=255)
    last_name = models.CharField(_("фамилия"), max_length=255)
    # movies = models.ManyToManyField("Movie", blank=True)
    # series = models.ManyToManyField("Series", blank=True)

    class Meta:
        verbose_name = _("сценарист")
        verbose_name_plural = _("сценаристы")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(TimeStampedModel):
    name = models.CharField(_("название"), max_length=255)
    description = models.TextField(_("описание"), blank=True)

    class Meta:
        verbose_name = _("жанр")
        verbose_name_plural = _("жанры")

    def __str__(self):
        return self.name


class Movie(TimeStampedModel):
    title = models.CharField(_("название"), max_length=255)
    description = models.TextField(_("описание"), blank=True)
    creation_date = models.DateField(_("дата создания фильма"), blank=True)
    age_restriction = models.IntegerField(
        _("возрастной ценз"), validators=[MinValueValidator(0)], blank=True
    )
    rating = models.FloatField(_("рейтинг"), validators=[MinValueValidator(0)], blank=True)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    writers = models.ManyToManyField(Writer)
    genres = models.ManyToManyField(Genre)
    file_path = models.FileField(_("файл"), upload_to="film_works/", blank=True)

    class Meta:
        verbose_name = _("фильм")
        verbose_name_plural = _("фильмы")

    def __str__(self):
        return self.title


class Series(TimeStampedModel):
    title = models.CharField(_("название"), max_length=255)
    description = models.TextField(_("описание"), blank=True)
    creation_date = models.DateField(_("дата создания фильма"), blank=True)
    age_restriction = models.IntegerField(
        _("возрастной ценз"), validators=[MinValueValidator(0)], blank=True
    )
    rating = models.FloatField(_("рейтинг"), validators=[MinValueValidator(0)], blank=True)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    writers = models.ManyToManyField(Writer)
    genres = models.ManyToManyField(Genre)
    file_path = models.FileField(_("файл"), upload_to="film_works/", blank=True)

    class Meta:
        verbose_name = _("сериал")
        verbose_name_plural = _("сериалы")

    def __str__(self):
        return self.title
