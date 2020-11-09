from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from model_utils.models import TimeStampedModel


class Genre(TimeStampedModel):
    name = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)

    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')

    def __str__(self):
        return self.name


# class FilmworkType(models.TextChoices):
#     MOVIE = 'movie', _('фильм')
#     TV_SHOW = 'tv_show', _('шоу')

class FilmworkType(TimeStampedModel):
    name = models.CharField(_('название'), max_length=255)

    class Meta:
        verbose_name = _('тип кинопроизведения')
        verbose_name_plural = _('типы кинопроизведений')

    def __str__(self):
        return self.name


class Filmwork(TimeStampedModel):
    type = models.ForeignKey(
        FilmworkType,
        verbose_name=_("тип кинопроизведения"),
        related_name='films',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    title = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)
    creation_date = models.DateField(_('дата создания фильма'), blank=True)
    certificate = models.TextField(_('сертификат'), blank=True)
    file_path = models.FileField(_('файл'), upload_to='film_works/', blank=True)
    rating = models.FloatField(_('рейтинг'), validators=[MinValueValidator(0)], blank=True)
    # type = models.CharField(_('тип'), max_length=20, choices=FilmworkType.choices)
    genres = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = _('кинопроизведение')
        verbose_name_plural = _('кинопроизведения')

    def __str__(self):
        return self.title
