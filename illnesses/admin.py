from django.contrib import admin
from main.models import Illness, TemplateModel
from herbs.admin import ImageInline



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
    date_hierarchy = 'created'
    ordering = ('title',)
    readonly_fields = ('show_herbs', )
    model = Illness
    inlines = [ImageInline, ]
    fieldsets = [
        ('Basic information', {'fields':
            [
                'title', 'description',
            ]
            }
         ),
        ('Other', {'fields':
            [
                'note',
            ],
            'classes': ['collapse']
        }
         ),
        ('Herbs', {'fields':
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
