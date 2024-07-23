from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import requests
import json
from .forms import NewsletterForm
from .models import NewsletterSubscriber

#def subscribe(request):
#    if request.method == 'POST':
#        form = NewsletterForm(request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Obrigado por se inscrever na nossa newsletter!')
#            return redirect('newsletter_subscribe')
#    else:
#        form = NewsletterForm()
#
#    return render(request, 'subscribe.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            # Integração com RD Station
            url = f"https://api.rd.services/platform/conversions?api_key=zUxTeLeKRyWEFPtEeAaRUqMFKRVhnKtsyCVt"

            payload = json.dumps({
                "event_type": "CONVERSION",
                "event_family": "CDP",
                "payload": {
                    "conversion_identifier": "Conversão exemplo",
                    "email": subscriber.email,
                    "name": subscriber.nome,
                }
            })
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            }

            print(payload)

            response = requests.post(url, headers=headers, data=payload)
            
            if response.status_code == 200:
                messages.success(request, 'Obrigado por se inscrever na nossa newsletter!')
            else:
                messages.warning(request, 'Sua inscrição foi salva, mas houve um problema ao integrar com o RD Station.')
            return redirect('newsletter_subscribe')
    else:
        form = NewsletterForm()
    return render(request, 'subscribe.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def success(request):
    return render(request, 'success.html')

def unsubscribe(request, email):
    try:
        subscriber = NewsletterSubscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        messages.success(request, 'Você foi desinscrito com sucesso da nossa newsletter.')
        return render(request, 'unsubscribe_success.html')
    except NewsletterSubscriber.DoesNotExist:
        messages.error(request, 'O email fornecido não foi encontrado em nossa lista de assinantes.')
        return render(request, 'unsubscribe_fail.html')