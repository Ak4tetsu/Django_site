from django.urls import path

from . import views

urlpatterns = [
    # examp: hostname/blog/
    path('',views.index,name='index'),

    # examp: hostname/blog/5
    path('<int:post_id>',views.detail,name='ditail')
]
