from django.contrib import admin
from .models import Herb
from django.utils.html import mark_safe





class HerbAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'alternative_name',
        'show_image',
        'show_video_url',
        'recipes_count',
        'illnesses_count',
    )
    search_fields = (
        'title',
        'alternative_name',
        'templatemodel__recipe__title',
        'templatemodel__illness__title',
        'contraindications__title',
        'effects__title',
    )
    list_filter = (
        'templatemodel__recipe__title',
        'templatemodel__illness__title',
        'contraindications__title',
        'effects__title',
    )
    date_hierarchy = 'created'
    ordering = ('title', )
    filter_horizontal = ['contraindications', 'effects']
    list_max_show_all = 50
    list_editable = ('alternative_name', )

    class Meta:
        model = Herb


    readonly_fields = ('illnesses_title', 'recipes_title', 'show_image', )
    fieldsets = [
        ('Basic information', {'fields':
                                   [
                                       'title', 'alternative_name', 'description', 'video_link',
                                   ]
                               }
         ),
        ('Image', {'fields':
                        [('image', 'show_image') ]
                    }
         ),
        ('Others', {'fields':
                        ['contraindications', 'effects'],
                        'classes': ['collapse']
                    }
         ),
        ('Recipes', {'fields':
                        ['recipes_title']
                    }
         ),
        ('Illnesses', {'fields':
                         ['illnesses_title']
                     }
         ),
    ]

    def illnesses_title(self, obj):
        result = obj.templatemodel_set.all().filter(recipe__isnull = True)
        temp_arr = []
        if result:
            for query in result:
                temp_arr.append(mark_safe('<a href={url} target="new" style="text-decoration: underline">{text}</a>'.format(
                    url = query.illness.get_admin_url(),
                    text = query.illness,
                )))
            return mark_safe("\n<br />".join(temp_arr))
        else:
            return "Herb in 0 illnesses"
    illnesses_title.short_description = 'Illnesses'

    def recipes_title(self, obj):
        result = obj.templatemodel_set.all().filter(illness__isnull=True)
        temp_arr = []
        if result:
            for query in result:
                temp_arr.append(mark_safe('<a href={url} target="new" style="text-decoration: underline">{text}</a>'.format(
                    url=query.recipe.get_admin_url(),
                    text=query.recipe,
                )))
            return mark_safe("\n<br />".join(temp_arr))
        else:
            return "Herb in 0 recipes"
    recipes_title.short_description = 'Recipes'


    def show_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.image.url,
                width=100,
                height="auto"
                ))
    show_image.short_description = 'Image'
    show_image.admin_ordering_field = 'Image'


    """
    def show_youtube_video(self, obj):
        return mark_safe('<iframe src="{url}" width="{width}" height="{height}" frameborder="0"></iframe>'.format(
                url = obj.video_link,
                width = 200,
                height="auto"
            ))
    """



admin.site.register(Herb, HerbAdmin)
