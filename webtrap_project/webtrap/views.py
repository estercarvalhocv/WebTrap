from django.shortcuts import render
from .models import RequestLog, HoneypotSubmission
from .forms import HoneypotForm

def honeypot(request):
    log_request(request)
    return render(request, 'webtrap/honeypot.html')

def log_request(request):
    RequestLog.objects.create(
        method=request.method,
        url=request.path,
        headers=dict(request.headers)
    )

def honeypot_form(request):
    if request.method == 'POST':
        form = HoneypotForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            # Salvar no banco de dados
            HoneypotSubmission.objects.create(nome=nome, email=email)
            return render(request, 'webtrap/honeypot.html')
    else:
        form = HoneypotForm()

    return render(request, 'webtrap/honeypot_form.html', {'form': form})
