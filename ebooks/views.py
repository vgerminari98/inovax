from django.shortcuts import render
from .models import Ebook

def ebook_list(request):
    ebooks = Ebook.objects.all()
    print(ebooks)
    return render(request, 'ebook.html', {'ebooks': ebooks})

#def ebook_list(request):
#    ebooks = Ebook.objects.all()
#    return render(request, 'ebooks/ebook.html', {'ebooks': ebooks})
