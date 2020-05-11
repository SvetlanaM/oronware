from django.db import models
from main.models import TimeStampModel, ImageModel, AmountModel, Contraindication, Effect
from django.utils.html import format_html, mark_safe

class Herb(TimeStampModel, ImageModel):
    title = models.CharField(max_length=255, verbose_name="Herb")
    alternative_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    video_link = models.URLField(blank=True)
    note = models.TextField(blank=True)
    contraindications = models.ManyToManyField(Contraindication, verbose_name='contraindications', blank=True, null=True)
    effects = models.ManyToManyField(Effect, verbose_name='effects', blank=True, null=True)

    class Meta:
        verbose_name = 'Herb'
        verbose_name_plural = 'Herbs'
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
        return self.templatemodel_set.all().filter(recipe__isnull=True).count()
    illnesses_count.short_description = 'In illnesses'
    illnesses_count.admin_order_field = 'id'










