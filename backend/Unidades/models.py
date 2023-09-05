from django.db import models
from django.contrib.auth.models import User



class SubUnidade(models.Model):
    nome = models.CharField(max_length=100)
    gestorSubUnidade = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField(unique=False, default="")
    endereco = models.TextField() #importante para gráficos futuros, mas podemos remover
    telefone = models.CharField(max_length=20)
    carrinho = models.ForeignKey('demandaProdutos.Carrinho', on_delete=models.SET_NULL, blank=True, null=True, related_name='subUnidade_carrinho')
    pedido = models.ForeignKey('demandaProdutos.Pedido', on_delete=models.SET_NULL, blank=True, null=True, related_name='subUnidade_pedido')
   
    def __str__(self):
        return "mokado"


class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    GestorUnidade = models.ManyToManyField(User,blank=True)
    email = models.EmailField(unique=False,default="")
    departamento = models.CharField(max_length=100)
    subunidades = models.ManyToManyField(SubUnidade,blank=True)

    def __str__(self):
        return "mocado"
