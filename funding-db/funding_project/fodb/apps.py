from django.apps import AppConfig
from django import get_version
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class FodbConfig(AppConfig):
    name = 'fodb'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'  # or 'vertical'
    name = 'suit'
    django_version = get_version()
