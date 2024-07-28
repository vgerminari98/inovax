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
            try:
                subscriber = form.save()
                # Integração com RD Station
                url = f"https://api.rd.services/platform/conversions?api_key=zUxTeLeKRyWEFPtEeAaRUqMFKRVhnKtsyCVt"

                payload = json.dumps({
                    "event_type": "CONVERSION",
                    "event_family": "CDP",
                    "payload": {
                        "conversion_identifier": "news_letter",
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
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados e tente novamente.')
           
    else:
        form = NewsletterForm()
    return render(request, 'subscribe.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def unsubscribe(request, email):
    RD_STATION_API_URL = 'https://api.rd.services/platform/contacts/email:{email}'
    RD_STATION_API_TOKEN = 'zUxTeLeKRyWEFPtEeAaRUqMFKRVhnKtsyCVt'

    try:
        subscriber = NewsletterSubscriber.objects.get(email=email)
        subscriber.is_active = False
        subscriber.save()
        response = requests.delete(
            RD_STATION_API_URL.format(email=email),
            headers={'Authorization': f'Bearer {RD_STATION_API_TOKEN}'}
        )
        
        if response.status_code == 204:  # 204 No Content indicates success
            print('204')
            messages.success(request, 'Você foi desinscrito com sucesso da nossa newsletter.')
            return render(request, 'unsubscribe_success.html')
        else:
            print('qualquer erro', response)
            messages.error(request, 'Não foi possível desinscrever do RD Station. Tente novamente mais tarde.')
            return render(request, 'unsubscribe_fail.html')
    except NewsletterSubscriber.DoesNotExist:
        print('qualquer erro 2')
        messages.error(request, 'O email fornecido não foi encontrado em nossa lista de assinantes.')
        return render(request, 'unsubscribe_fail.html')