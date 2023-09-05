from django.contrib import admin
from demandaProdutos.models import Categoria,Produto,Carrinho,ItemCarrinho,Pedido

class Categorias(admin.ModelAdmin):
    list_diplay = ('nome','descricao')
    list_display_link = ('nome','descricao')
    search_field=('nome',)
admin.site.register(Categoria,Categorias)
   
class Produtos(admin.ModelAdmin):
    list_diplay = ('nome','descricao','preco','categoria','data_criacao','ativo')
    list_display_link = ('nome','descricao','preco','ativo')
    search_field=('nome',)
    list_per_page=10
    #verificar a questão do estoque

admin.site.register(Produto,Produtos)

class Carrinhos(admin.ModelAdmin):
    list_diplay = ('subunidade','produtos','crieado_em')
    list_display_link = ('subunidade','produtos')
    search_field=('subunidade',)
    list_per_page=10
    #verificar o preço total
admin.site.register(Carrinho,Carrinhos)

class ItensCarrinho(admin.ModelAdmin):
    list_diplay = ('carrinho','produto','quantidade')
    list_display_link = ('carrinho','produto')
    list_per_page=10
admin.site.register(ItemCarrinho,ItensCarrinho)

class Pedidos(admin.ModelAdmin):
    list_diplay = ('carrinho','status','unidade_autorizadora')
    list_display_link=('carrinho','status','unidade_autorizadora')
    list_per_page = 20
    #olhar se total,endereço de entrega são relevantes
admin.site.register(Pedido,Pedidos)
'''
class InfoProdutos(admin.ModelAdmin):
    list_display = ('preco','ano','produto')
    list_display_link = ('id','preco','ano','produto')
    search_field = ('ano')
admin.site.register(infoProduto,InfoProdutos)

class Produtos(admin.ModelAdmin):
    list_diplay = ('id','nome','descricao','tipo_categoria','visivel')
    list_display_link = ('id','nome',)
    search_fields = ('nome',)
    list_per_page=20

admin.site.register(Produto,Produtos)
'''