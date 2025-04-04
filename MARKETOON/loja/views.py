from django.shortcuts import render,redirect
from loja.models import func_registrar_produto

# Create your views here.
def cadastro_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        data=request.POST.get('data')
        func_registrar_produto.objects.create(nome=nome,
                                              email=email,
                                              telefone=telefone,
                                              descricao=descricao,
                                              preco=preco,
                                              data=data
                                              )
