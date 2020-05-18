from django.db import models
from main.models import TimeStampModel, ImageModel, AmountModel, Contraindication, Effect, Substance, Illness, Study
from django.utils.html import format_html, mark_safe
from django.utils.translation import gettext_lazy as _

class Herb(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name="Herb")
    alternative_name = models.CharField(max_length=500, blank=True)
    latin_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    video_link = models.URLField(blank=True)
    batching = models.TextField(blank=True)
    planting = models.TextField(blank=True)
    note = models.TextField(blank=True)
    contraindications = models.ManyToManyField(Contraindication, verbose_name='contraindications', blank=True, null=True)
    effects = models.ManyToManyField(Effect, verbose_name='effects', blank=True, null=True)
    substances = models.ManyToManyField(Substance, verbose_name='substances', blank=True, null=True)
    illnesses = models.ManyToManyField(Illness, verbose_name='illnesses', blank=True, null=True, related_name='herb_illnesses')
    studies = models.ManyToManyField(Study, verbose_name='studies', blank=True, null=True, related_name = 'studies')

    class Meta:
        verbose_name = _('Herb')
        verbose_name_plural = _('Herbs')
        ordering = ('title', )

    def __str__(self):
        return self.title

    def show_video_url(self):
        return format_html("<a href={} target='new'>{}</a>", mark_safe(self.video_link), self.video_link)
    show_video_url.allow_tags = True
    show_video_url.short_description = 'Video URL'

    def recipes_count(self):
        return self.templatemodel_set.all().filter(illness__isnull=True).count()
    recipes_count.short_description = 'In recipes'
    recipes_count.admin_order_field = 'id'


    def illnesses_count(self):
        return self.illnesses.all().count()
    illnesses_count.short_description = 'In illnesses'
    illnesses_count.admin_order_field = 'id'

    def substances_count(self):
        return self.substances.all().count()
    substances_count.short_description = 'Substances'
    substances_count.admin_order_field = 'id'

    def contraindications_count(self):
        return self.contraindications.all().count()
    contraindications_count.short_description = 'Contraindications'
    contraindications_count.admin_order_field = 'id'











