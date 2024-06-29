from django.shortcuts import render
from .models import Funcionario

def home(request):

    return render(request, 'home.html')

def about(request):

    funcionarios = Funcionario.objects.all()
    return render(request, 'about.html', {'funcionarios': funcionarios})


#def quem_somos(request):
#    """Render the 'Quem Somos' page."""
#    return render(request, 'pages/quem_somos.html')
#
#
#def nossas_solucoes(request):
#    """Render the 'Nossas Soluções' page."""
#    return render(request, 'pages/nossas_solucoes.html')
#
#
#def nosso_time(request):
#    """Render the 'Nosso Time' page."""
#    return render(request, 'pages/nosso_time.html')
#
#
#def conteudos_para_voce(request):
#    """Render the 'Conteúdos para Você' page."""
#    return render(request, 'pages/conteudos_para_voce.html')
#
#
#def podcast(request):
#    """Render the 'Podcast' page."""
#    return render(request, 'pages/podcast.html')
#
#
#def videos(request):
#    """Render the 'Vídeos' page."""
#    return render(request, 'pages/videos.html')