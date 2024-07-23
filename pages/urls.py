from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.about, name='quem_somos'),
    path('nossas-solucoes/', views.soluction, name='nossas_solucoes'),
    path('nossas-solucoes-detalhes/', views.soluction_detail, name='nossas_solucoes_detalhes'),
    path('newsletter/', include('newsletter.urls')),
   # path('nosso-time/', views.nosso_time, name='nosso_time'),
   # path('conteudos-para-voce/', views.conteudos_para_voce, name='conteudos_para_voce'),
   # path('podcast/', views.podcast, name='podcast'),
   # path('videos/', views.videos, name='videos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)