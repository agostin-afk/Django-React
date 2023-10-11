from rest_framework import viewsets,generics
from demandaProdutos.models import Unidade,SubUnidade,Carrinho,Categoria,Produto,Imagem,Usuarios
from demandaProdutos.serializer import CarrinhoSerializer,CategoriaSerializer,ProdutoSerializer,ImagemSerializer,UsuariosSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets

class UsuariosViewsSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
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

class ListaCarrinhosUnidade(generics.ListAPIView):
    """Listando os carrinhos de uma Unidade"""
    def get_queryset(self):
        queryset = Carrinho.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = CarrinhoSerializer

