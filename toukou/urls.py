from django.urls import path, include
from .import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path ('itiran/', views.Listattendview.as_view()),
    path ('report/', views.Listtikokuview.as_view()),
    path ('top/', views.Listtopview.as_view(),name = 'toukou'),
    path ('testpage',views.index,name='index'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('logout/', views.logout_view, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
