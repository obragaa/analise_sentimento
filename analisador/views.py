from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from textblob import TextBlob
from googletrans import Translator
from .models import Frases

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home(request):
    # Tenta recuperar o sentimento da sessão se disponível
    sentimento = request.session.get('sentimento', "")
    
    if request.method == "POST":

        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            # Redireciona para a página de login ou mostra uma mensagem de erro
            return HttpResponseRedirect(reverse('login'))

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'analisador/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Usuário ou senha inválidos
                # Verifica se o usuário existe
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Senha incorreta. Por favor, tente novamente.")
                else:
                    messages.error(request, "Usuário não encontrado. Você gostaria de se <a href='%s'>cadastrar</a>?" % reverse('signup'), extra_tags='safe')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = CustomLoginForm()
    return render(request, 'analisador/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redireciona o usuário para a página inicial após o logout