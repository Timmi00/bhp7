from django.urls import path
from .views import index


urlpatterns = [
    path('category/<int:category_id>', index),
]



# class YearConverter:
#     regex = '[0-9]{4}'
#
#     def to_python(self, value):
#         return int(value)
#
#     def to_url(self, value):
#         return str(value)
#
#
# register_converter(YearConverter, 'year')