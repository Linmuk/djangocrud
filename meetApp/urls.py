from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.list_emp,name='emp_list'),
    path('create/',views.create_emp,name='create_emp'),
    path('edit/<int:id>/',views.edit_emp,name='edit_emp'),
    path('delete/<int:id>/',views.delete_emp,name='delete_emp')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)