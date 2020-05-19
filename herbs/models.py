from django.db import models
from main.models import TimeStampModel, ImageModel, AmountModel, Contraindication, Effect, Substance, Illness, Study
from django.utils.html import format_html, mark_safe
from django.utils.translation import gettext_lazy as _

class Herb(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_('Herb'))
    alternative_name = models.CharField(max_length=500, blank=True, verbose_name=_('alernative_name'))
    latin_name = models.CharField(max_length=255, blank=True, verbose_name=_('latin_name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    video_link = models.URLField(blank=True, verbose_name=_('video_link'))
    batching = models.TextField(blank=True, verbose_name=_('batching'))
    planting = models.TextField(blank=True, verbose_name=_('planting'))
    note = models.TextField(blank=True, verbose_name=_('note'))
    contraindications = models.ManyToManyField(Contraindication, blank=True, null=True, verbose_name=_('contraindications'))
    effects = models.ManyToManyField(Effect, blank=True, null=True, verbose_name=_('effects'))
    substances = models.ManyToManyField(Substance, blank=True, null=True, verbose_name=_('substances'))
    illnesses = models.ManyToManyField(Illness, blank=True, null=True, related_name='herb_illnesses', verbose_name=_('illnesses'))
    studies = models.ManyToManyField(Study, blank=True, null=True, related_name='studies', verbose_name=_('studies'))

    class Meta:
        verbose_name = _('Herb')
        verbose_name_plural = _('Herbs')
        ordering = ('title', )

    def __str__(self):
        return self.title

    def show_video_url(self):
        return format_html("<a href={} target='new'>{}</a>", mark_safe(self.video_link), self.video_link)
    show_video_url.allow_tags = True
    show_video_url.short_description = _('Video URL')

    def recipes_count(self):
        return self.templatemodel_set.all().filter(illness__isnull=True).count()
    recipes_count.short_description = _('In recipes')
    recipes_count.admin_order_field = 'id'


    def illnesses_count(self):
        return self.illnesses.all().count()
    illnesses_count.short_description = _('In illnesses')
    illnesses_count.admin_order_field = 'id'

    def substances_count(self):
        return self.substances.all().count()
    substances_count.short_description = _('Substances')
    substances_count.admin_order_field = 'id'

    def contraindications_count(self):
        return self.contraindications.all().count()
    contraindications_count.short_description = _('Contraindications')
    contraindications_count.admin_order_field = 'id'











