from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from textblob import TextBlob
from googletrans import Translator
from .models import Frases

def home(request):
    # Tenta recuperar o sentimento da sessão se disponível
    sentimento = request.session.get('sentimento', "")
    
    if request.method == "POST":
        texto = request.POST.get('texto', '')
        translator = Translator()
        try:
            texto_en = translator.translate(texto, src='pt', dest='en').text
            blob = TextBlob(texto_en)
            polaridade = blob.sentiment.polarity
            if polaridade > 0:
                sentimento = "Positivo"
            elif polaridade < 0:
                sentimento = "Negativo"
            else:
                sentimento = "Neutro"
            
            Frases.objects.create(texto=texto, resposta=sentimento, data_e_hora=timezone.now())
            
            # Armazena o sentimento na sessão
            request.session['sentimento'] = sentimento
            
        except Exception as e:
            sentimento = f"Erro ao traduzir o texto: {e}"
            request.session['sentimento'] = sentimento
        
        return redirect(reverse('home'))
    
    # Limpa o sentimento da sessão após ser recuperado para não persistir entre refreshes
    request.session.pop('sentimento', None)

    ultimas_frases = Frases.objects.filter(publicada=True).order_by('-data_e_hora')[:3]
    return render(request, 'home.html', {'ultimas_frases': ultimas_frases, 'sentimento': sentimento})

def buscar(request):
    return render(request, "buscar.html")