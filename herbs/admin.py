from django.contrib import admin
from .models import Herb
from django.utils.html import mark_safe
from main.models import ImageModel
from django.utils.translation import gettext_lazy as _


class ImageInline(admin.TabularInline):
    model = ImageModel
    extra = 0
    classes = ['collapse']

    readonly_fields = ('show_image', )

    fieldsets = [
        ('', {'fields':
            [
                ('file', 'show_image'),
            ],
        }
         )
    ]

    def show_image(self, obj):
        if obj.file:
            type = obj.file.name[-3:]
            if type in ('jpg', 'png', 'svg', 'jpeg', 'gif'):
                return mark_safe('<a href="{url}" target="new"><img src="{url}" width="{width}" height={height} /></a>'.format(
                    url = obj.file.url,
                    width=200,
                    height="auto"
                    ))
            if type in ('doc', 'docx', 'pdf', 'csv', 'xls', 'xlxs'):
                return mark_safe(
                    '<a href="{url}" target="new">File {name}</a>'.format(
                        url=obj.file.url,
                        name=obj.get_name()
                    ))
    show_image.short_description = _('File')
    show_image.admin_ordering_field = 'File'




class HerbAdmin(admin.ModelAdmin):
    class Media:
        pass
    list_display = (
        'title',
        'latin_name',
        'alternative_name',
        'recipes_count',
        'illnesses_count',
        'substances_count',
        'contraindications_count',
    )
    search_fields = (
        'title',
        'alternative_name',
        'latin_name',
        'templatemodel__recipe__title',
        'illnesses__title',
        'contraindications__title',
        'substances__title',
        'effects__title',
    )
    list_filter = [
        'substances__title',
        'effects__title',
        'contraindications__title',
        'illnesses__title',
        'templatemodel__recipe__title',
    ]
    inlines = [ImageInline]
    date_hierarchy = 'created'
    ordering = ('title', )
    filter_horizontal = ['contraindications', 'effects', 'substances', 'illnesses', 'studies',]
    list_max_show_all = 50
    list_editable = ('alternative_name', )

    class Meta:
        model = Herb


    readonly_fields = ('illnesses_title', 'recipes_title', 'show_links',)
    fieldsets = [
        (_('Basic information'), {'fields':
                                   [
                                       ('title', 'latin_name',),
                                       'alternative_name',
                                       'video_link', 'description',
                                       'batching',
                                       'planting',
                                   ]
                               }
         ),
        (_('Effects'), {'fields':
                        [
                            'effects',
                        ],
                        'classes': ['collapse']
                    }
         ),
        (_('Substances and contraindications'), {'fields':
            [
                'substances',
                'contraindications',
            ],
            'classes': ['collapse']
        }
         ),
        (_('Illnesses'), {'fields':
            [
                'illnesses',
            ],
            'classes': ['collapse']
        }
         ),
        (_('Studies'), {'fields':
            [
                'studies',
                'show_links',
            ],
            'classes': ['collapse']
        }
         ),
        (_('Others'), {'fields':
            [
                'note',
            ],
        }
         ),
        (_('Recipes'), {'fields':
                        ['recipes_title']
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
            return _("Herb in 0 illnesses")
    illnesses_title.short_description = _('Illnesses')

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
            return _("Herb in 0 recipes")
    recipes_title.short_description = _('Recipes')

    def show_links(self, obj):
        studies = obj.studies.all()
        temp_arr = []
        if studies:
            for query in studies:
                temp_arr.append(mark_safe('<a href="{url}" target="new">{url}</a>'.format(
                    url=query.link,
                    )))
            return mark_safe("\n<br />".join(temp_arr))
        else:
            return _("No links")
    show_links.short_description = _('Studies links')
    show_links.admin_ordering_field = 'Studies links'


    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.herb_images.create(file=afile)




admin.site.register(Herb, HerbAdmin)
