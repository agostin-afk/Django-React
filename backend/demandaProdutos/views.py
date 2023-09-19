from rest_framework import viewsets,generics
from demandaProdutos.models import Unidade,SubUnidade,Carrinho,Categoria,Produto,Arquivo
from demandaProdutos.serializer import CarrinhoSerializer,CategoriaSerializer,ProdutoSerializer,Uparquivoserializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ReceberArquivo(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = Uparquivoserializer
class ListarCategorias(viewsets.ModelViewSet):
    """listar categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListarProdutos(viewsets.ModelViewSet):
    """listar Produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class DetalharProduto(generics.ListAPIView):
    def get_produto(self):
        produto = Produto.objects.filter(id=self.kwargs['id'])
        return produto
    serializer_class = ProdutoSerializer


#carrinho
#remover Item do carrinho
#finalizar pedido
#detalhar pedido
#listar carrinhos por unidade
#Listar pedidos por unidade
#Atualizar Carrinho
#remover Item do carrinho
#adicionar item ao carrinho

class ListaCarrinhosUnidade(generics.ListAPIView):
    """Listando os carrinhos de uma Unidade"""
    def get_queryset(self):
        queryset = Carrinho.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = CarrinhoSerializer

