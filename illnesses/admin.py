from django.contrib import admin
from main.models import Illness, TemplateModel
from herbs.admin import ImageInline
from django.utils.translation import gettext_lazy as _


class IllnessAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'show_herbs',
    )
    list_filter = (
        'templatemodel__herb__title',
    )
    search_fields = (
        'title',
        'templatemodel__herb__title',
    )
    ordering = ('title',)
    readonly_fields = ('show_herbs', )
    model = Illness
    inlines = [ImageInline, ]
    fieldsets = [
        (_('Basic information'), {'fields':
            [
                'title', 'description',
            ]
            }
         ),
        (_('Other'), {'fields':
            [
                'note',
            ],
            'classes': ['collapse']
        }
         ),
        (_('Herbs'), {'fields':
            [
                'show_herbs',
            ],
        }
         ),
    ]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.illness_images.create(file=afile)


admin.site.register(Illness, IllnessAdmin)
