
from django.contrib import admin
from django.urls import path,include
from demandaProdutos.views import ListarCategorias,ListarProdutos,DetalharProduto,ListaCarrinhosUnidade
from Unidades.views import ListarUnidades,DetalharSubUnidade,ListarSubUnidades,DetalharUnidade,DetalharSubUnidade
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subUnidades',ListarSubUnidades,basename='SubUnidades')
router.register('unidades',ListarUnidades,basename='Unidades')
router.register('categorias',ListarCategorias,basename='Categorias')
router.register('produtos',ListarProdutos,basename='Produtos')
#router.register('carrinhos',ListaCarrinhosUnidade,basename='Carrinhos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('unidade/<int:pk>/', DetalharUnidade.as_view()),
    path('subUnidade/<int:pk>/', DetalharSubUnidade.as_view()),
    path('produtos/<int:pk>/', DetalharProduto.as_view()),
   # path('unidade/<int:pk>/carrinhos/', ListaCarrinhosUnidade.as_view())
 
]
