from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('people', views.PeopleView.as_view(),name='people'),
    path('ccourse', views.CCourseView.as_view(),name='ccourse'),
    path('acourse', views.ACourseView.as_view(),name='acourse'),
    path('research', views.ResearchView.as_view(),name='research'),
    path('partner', views.PartnerView.as_view(),name='partner'),
    path('join', views.JoinView.as_view(),name='joinUs'),
    path('event', views.EventView.as_view(),name='event'),
    path('apply', views.ApplyView.as_view(),name='apply'),
    path('applyResponse', views.ApplyResponseView.as_view(),name='applyResponse'),
    re_path(r'^[.]*/$', views.errorPage,name='err')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
