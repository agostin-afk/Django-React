from rest_framework import viewsets,generics
from Unidades.models import Unidade,SubUnidade
from Unidades.serializer import SubUnidadeSerializer,UnidadeSerializer


class ListarUnidades(viewsets.ModelViewSet):
    """listando as unidades"""
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class DetalharSubUnidade(generics.ListAPIView):
    """Detalhar uma unidade"""
    def get_Subunidade(self):
        subUnidade = SubUnidade.objects.filter(id=self.kwargs['id'])
        return subUnidade
    serializer_class = UnidadeSerializer

class ListarSubUnidades(viewsets.ModelViewSet):
    """Exibindo as subunidades"""
    queryset = SubUnidade.objects.all()
    serializer_class = SubUnidadeSerializer

class DetalharUnidade(generics.ListAPIView):
    """Detalhar uma unidade"""
    def get_unidade(self):
        unidade = Unidade.objects.filter(id=self.kwargs['id'])
        return unidade
    serializer_class = UnidadeSerializer

class DetalharSubUnidade(generics.ListAPIView):
    """detalhes de subunidade"""
    def get_unidade(self):
        subUnidade = SubUnidade.objects.filter(id=self.kwargs['id'])
        return subUnidade
    serializer_class = SubUnidadeSerializer
