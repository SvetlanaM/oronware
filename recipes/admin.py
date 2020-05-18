from django.contrib import admin
from main.models import Recipe, TemplateModel
from herbs.admin import ImageInline

class RecipeModel(admin.TabularInline):
    model = TemplateModel
    extra = 1
    fields = (
        'value',
        'name',
        'herb'
    )
    raw_id_fields = ['herb', ]


class RecipeAdmin(admin.ModelAdmin):
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
    inlines = [RecipeModel, ImageInline, ]
    model = Recipe
    fieldsets = [
        ('Basic information', {'fields':
            [
                'title', 'description', 'preparing'
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
    ]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.recipe_images.create(file=afile)


admin.site.register(Recipe, RecipeAdmin)
