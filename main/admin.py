from django.contrib import admin
from .models import Effect, Contraindication
from django.contrib.auth.models import Group, User


class EffectAdmin(admin.ModelAdmin):
    class Meta:
        model = Effect

class ContraindicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Contraindication


admin.site.register(Effect, EffectAdmin)
admin.site.register(Contraindication, ContraindicationAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
