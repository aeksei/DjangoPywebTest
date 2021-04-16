from django_filters \
    import rest_framework as drf_filter

from .models import ToDoList


class ToDoListFilter(drf_filter.FilterSet):
    important = drf_filter.BooleanFilter(
        field_name='important',
        help_text="olololo"
    )
    min_view = drf_filter.NumberFilter(
        'views',
        lookup_expr='gte'
    )
    max_view = drf_filter.NumberFilter(
        'views',
        lookup_expr='lte'
    )
    author = drf_filter.NumberFilter(
        'author__pk'
    )
    author_name = drf_filter.CharFilter(
        'author__username',
        lookup_expr='contain'
    )

    class Meta:
        model = ToDoList
        fields = (
            'important',
            'min_view',
            'max_view',
            'author',
            'author_name',
        )

