from django.urls import path, re_path, register_converter

from . import views
from extensions import converters


register_converter(converters.FourDigitYearConverter, 'yyyy')


app_name = 'blog_urls'
urlpatterns = [
    # examp: hostname/blog
    path('',views.index,name='index'),

    # examp: hostname/blog/5
    path('<int:post_id>',views.detail,name='ditail'),

    # examp: hostname/blog/archive/2023
    # path('archive/<int:year>', views.archive_year, name='archive'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/$', views.archive_year, name='archive'),
    path('archive/<yyyy:year>/', views.archive_year, name='archive'),
]
