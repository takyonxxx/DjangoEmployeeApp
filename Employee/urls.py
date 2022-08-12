from django.urls import path
from DjangoEmployeeApp.base_view import create_view_paths
from . import views
import itertools


def flatten_list(nested_list):
    return itertools.chain.from_iterable(nested_list)


urlpatterns = [
    path('', views.index),
    *flatten_list(
        create_view_paths(_name, getattr(views, f'{_name}ViewSet'))
        for _name in [
            'Employee',
        ]
    )
]
