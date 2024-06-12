from django.shortcuts import render, HttpResponse

def home(request):
    if request.method=='POST':
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operacao = request.POST.get('operacao')

        resultado = operacoes(numero1, numero2, operacao)
        return render(request, 'home.html', {'resultado': resultado})
    
    return render(request, 'home.html')

def calcular(request):
    if request.method=='POST':
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operacao = request.POST.get('operacao')

        resultado = operacoes(numero1, numero2, operacao)
        return render(request, 'home.html', {'resultado': resultado})
    
    return HttpResponse('Requisição Inválida')

def operacoes(numero1, numero2, operacao):
    if operacao == 'somar':
        return numero1 + numero2
    elif operacao == 'subtrair':
        return numero1 - numero2
    elif operacao == 'multiplicar':
        return numero1 * numero2
    elif operacao == 'dividir':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return 'Não podemos dividir por 0!'
    else:
        return 'Erro! Operação inválida.'
    