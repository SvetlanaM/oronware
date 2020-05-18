from django.contrib import admin
from .models import Effect, Contraindication, Substance, Study
from django.contrib.auth.models import Group, User


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


admin.site.register(Effect, EffectAdmin)
admin.site.register(Contraindication, ContraindicationAdmin)
admin.site.register(Substance, SubstanceAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
