from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))

    class Meta:
        abstract = True


class ImageModel(models.Model):
    file = models.FileField(upload_to='media', blank=True, null=True, verbose_name=_('file'))
    herb_photo = models.ForeignKey('herbs.Herb', verbose_name=_('herb_image'), related_name='herb_images', blank=True, null=True, on_delete=models.CASCADE)
    recipe_photo = models.ForeignKey('main.Recipe', verbose_name=_('recipe_image'), related_name='recipe_images', blank=True, null=True, on_delete=models.CASCADE)
    illness_photo = models.ForeignKey('main.Illness', verbose_name=_('illness_image'), related_name='illness_images', blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')


    def get_name(self):
        index = str(self.file.name).find("/") + 1
        return str(self.file.name[index:])

    def __str__(self):
        return self.get_name()


class AmountModel(models.Model):
    AMOUNT_VALUES = (
        ('kg', _('kilograms')),
        ('g', _('grams')),
        ('ks', _('pieces')),
        ('dg', _('dekagrams')),
    )
    name = models.CharField(max_length=5, choices=AMOUNT_VALUES, blank=True, verbose_name=_('name'))
    value = models.PositiveIntegerField(blank=True, verbose_name=_('value'))

    class Meta:
        verbose_name = _('Amount')
        verbose_name_plural = _('Amounts')
        abstract = True

    def __str__(self):
        return '%s %s' % (self.name, self.value)


class HerbTemplate(TimeStampModel):
    description = models.TextField(blank=True, verbose_name=_('description'))
    note = models.TextField(blank=True, verbose_name=_('note'))

    class Meta:
        abstract = True


    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=[self.pk])

    def __str__(self):
        return self.title

    def show_herbs(self):
        return ", \n".join([
            herb.herb.title for herb in self.templatemodel_set.all()
        ])
    show_herbs.short_description = _('Herbs')



class Illness(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_("Illness"))
    description = models.TextField(blank=True, verbose_name=_('description'))
    note = models.TextField(blank=True, verbose_name=_('note'))

    class Meta:
        verbose_name = _('Illness')
        verbose_name_plural = _('Illnesses')
        ordering = ('title', )

    def __str__(self):
        return self.title

    def show_herbs(self):
        return ", \n".join(query.title for query in self.herb_illnesses.all())
    show_herbs.short_description = _('Use herbs')
    show_herbs.admin_order_field = 'id'



class Recipe(HerbTemplate):
    title = models.CharField(max_length=255, verbose_name=_("Recipe"))
    preparing = models.TextField(blank=True, verbose_name=_('preparing'))

    class Meta:
        verbose_name = _('Recipe')
        verbose_name_plural = _('Recipes')
        ordering = ('title', )


class TemplateModel(AmountModel, TimeStampModel):
    herb = models.ForeignKey('herbs.Herb', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('herb'))
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('illness'))
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('recipe'))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['herb', 'illness'], name="herb-illness"),
            models.UniqueConstraint(fields=['herb', 'recipe'], name="herb-recipe"),
        ]
        verbose_name = _('Combination')
        verbose_name_plural = _('Combinations')

    def validate_unique(self, exclude=None):
        try:
            super(TemplateModel, self).validate_unique()
        except ValidationError as e:
            raise ValidationError(_("You already use this herb"))




class Effect(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_("Effect"))

    class Meta:
        verbose_name = _('Effect')
        verbose_name_plural = _('Effects')

    def __str__(self):
        return self.title


class Contraindication(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_("Contraindication"))

    class Meta:
        verbose_name = _('Contraindication')
        verbose_name_plural = _('Contraindications')

    def __str__(self):
        return self.title


class Substance(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_("Substances"))
    percentage = models.IntegerField(blank=True, verbose_name=_('percentage'), null=True)
    impact = models.TextField(blank=True, verbose_name=_('impact'))

    class Meta:
        verbose_name = _('Substance')
        verbose_name_plural = _('Substances')

    def __str__(self):
        return self.title


class Study(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name=_("Study"))
    link = models.URLField(blank=True, verbose_name=_('link'))

    class Meta:
        verbose_name = _('Study')
        verbose_name_plural = _('Studies')

    def __str__(self):
        return self.title








