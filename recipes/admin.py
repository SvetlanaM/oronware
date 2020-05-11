from django.contrib import admin
from main.models import Recipe, TemplateModel

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
    inlines = [RecipeModel,]
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


admin.site.register(Recipe, RecipeAdmin)
