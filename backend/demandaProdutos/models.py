from django.db import models
from django.contrib.auth.models import User
from Unidades.models import SubUnidade,Unidade



class Arquivo(models.Model):
    nome = models.CharField(max_length=100)
    dataUP = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='midia/')
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    #imagem = models.ImageField(upload_to='categorias/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    subunidade = models.OneToOneField('Unidades.SubUnidade', on_delete=models.CASCADE,related_name='subUnidade_carrinho')
    produtos = models.ManyToManyField(Produto, through='ItemCarrinho')
    #total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.subunidade.usuario.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE,related_name='item_carrinho')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    #subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.quantidade}"
class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('aceito como demanda pelo supervisor', 'aceito como demanda pelo supervisor'),
        ('demanda solicitada', 'demanda solicitada'),
        ('em apreciação', 'em apreciação'),
        ('cancelado', 'Cancelado')
    )

    carrinho = models.OneToOneField(Carrinho, on_delete=models.CASCADE, related_name='carrinho_pedido')
    #total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendente')
    #endereco_entrega = models.TextField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    unidade_autorizadora = models.ForeignKey('Unidades.Unidade', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"
    
