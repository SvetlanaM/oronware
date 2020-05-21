from django.contrib import admin
from .models import Effect, Contraindication, Substance, Study
from django.contrib.auth.models import Group, User
from herbs.admin import ImageInline

class EffectAdmin(admin.ModelAdmin):
    class Meta:
        model = Effect

class ContraindicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Contraindication

class SubstanceAdmin(admin.ModelAdmin):
    class Meta:
        model = Substance

class StudyAdmin(admin.ModelAdmin):
    class Meta:
        model = Study

    inlines = [ImageInline, ]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.study_images.create(file=afile)


admin.site.register(Effect, EffectAdmin)
admin.site.register(Contraindication, ContraindicationAdmin)
admin.site.register(Substance, SubstanceAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
