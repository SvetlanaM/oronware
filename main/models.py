from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ImageModel(models.Model):
    image = models.ImageField(upload_to='media', blank=True, null=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        abstract = True

    def __str__(self):
        return self.image


class AmountModel(models.Model):
    AMOUNT_VALUES = (
        ('kg', 'kilograms'),
        ('g', 'grams'),
        ('ks', 'pieces'),
        ('dg', 'dekagrams'),
    )
    name = models.CharField(max_length=5, choices=AMOUNT_VALUES, blank=True)
    value = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = 'Amount'
        verbose_name_plural = 'Amounts'
        abstract = True

    def __str__(self):
        return '%s %s' % (self.name, self.value)


class HerbTemplate(TimeStampModel):
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True


    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=[self.pk])

    def __str__(self):
        return self.title

    def show_herbs(self):
        return "\n, ".join([
            herb.herb.title for herb in self.templatemodel_set.all()
        ])
    show_herbs.short_description = 'Herbs'



class Illness(HerbTemplate):
    title = models.CharField(max_length=255, verbose_name="Illness")

    class Meta:
        verbose_name = 'Illness'
        verbose_name_plural = 'Illnesses'
        ordering = ('title', )



class Recipe(HerbTemplate):
    title = models.CharField(max_length=255, verbose_name="Recipe")
    preparing = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ('title', )


class TemplateModel(AmountModel, TimeStampModel):
    herb = models.ForeignKey('herbs.Herb', on_delete=models.CASCADE, blank=True, null=True)
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['herb', 'illness'], name="herb-illness"),
            models.UniqueConstraint(fields=['herb', 'recipe'], name="herb-recipe"),
        ]
        verbose_name = 'Combination'
        verbose_name_plural = 'Combinations'

    def validate_unique(self, exclude=None):
        try:
            super(TemplateModel, self).validate_unique()
        except ValidationError as e:
            raise ValidationError("You already use this herb")




class Effect(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name="Effect")

    class Meta:
        verbose_name = 'Effect'
        verbose_name_plural = 'Effects'

    def __str__(self):
        return self.title


class Contraindication(TimeStampModel):
    title = models.CharField(max_length=255, verbose_name="Contraindication")

    class Meta:
        verbose_name = 'Contraindication'
        verbose_name_plural = 'Contraindications'

    def __str__(self):
        return self.title






