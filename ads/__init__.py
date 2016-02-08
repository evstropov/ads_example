from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'ads.Config'


class Config(AppConfig):
    name = 'ads'
    verbose_name = _('Ads')
    label = 'ads'
