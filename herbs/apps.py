from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HerbsConfig(AppConfig):
    name = 'herbs'
    verbose_name = _('herbs')
