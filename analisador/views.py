from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from textblob import TextBlob
from googletrans import Translator
from .models import Frases, CustomUser
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, CustomLoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.functions import TruncHour
from django.db.models import Count
from django.contrib.auth.models import Group

def home(request):
    sentimento = request.session.get('sentimento', "")
    if request.method == "POST":
        if not request.user.is_authenticated:
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
            request.session['sentimento'] = sentimento
        except Exception as e:
            sentimento = f"Erro ao traduzir o texto: {e}"
            request.session['sentimento'] = sentimento
        return redirect(reverse('home'))
    request.session.pop('sentimento', None)
    ultimas_frases = Frases.objects.filter(publicada=True).order_by('-data_e_hora')[:3]
    return render(request, 'home.html', {'ultimas_frases': ultimas_frases, 'sentimento': sentimento})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
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
                if Group.objects.get(name='AdminGroup') in user.groups.all():
                    return redirect('admin_dashboard')
                return redirect('home')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = CustomLoginForm()
    return render(request, 'analisador/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def admin_dashboard(request):
    if not request.user.groups.filter(name='AdminGroup').exists():
        return redirect('home')

    # Determinar o intervalo de 24 horas a partir do momento atual
    current_time = timezone.now()
    start_time = current_time - timedelta(hours=24)

    # Número de usuários online
    num_users_online = CustomUser.objects.filter(last_login__gte=start_time).count()
    
    # Análises totais no período
    total_analyses = Frases.objects.filter(data_e_hora__range=[start_time, current_time]).count()

    # Análises por hora
    analyses_per_hour = Frases.objects.filter(data_e_hora__range=[start_time, current_time])
    analyses_per_hour = analyses_per_hour.annotate(hour=TruncHour('data_e_hora')).values('hour').annotate(count=Count('id')).order_by('hour')

    hours = [data['hour'].strftime('%Y-%m-%d %H:%M') for data in analyses_per_hour]
    counts = [data['count'] for data in analyses_per_hour]

    context = {
        'num_users_online': num_users_online,
        'total_analyses': total_analyses,
        'hours': hours,
        'counts': counts
    }
    return render(request, 'analisador/admin_dashboard.html', context)

def group_admin_check(user):
    return user.groups.filter(name='AdminGroup').exists()

@login_required
@user_passes_test(group_admin_check)
def manage_users(request):
    return render(request, 'analisador/manage_users.html', {})

def other_admin_action(request):
    return render(request, 'analisador/other_admin_action.html')

