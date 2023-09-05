from django.contrib import admin
from Unidades.models import SubUnidade,Unidade

class SubUnidades(admin.ModelAdmin):
    list_diplay = ('endereco','telefone','carrinho')
    #list_display_link = ('usuario')
    list_per_page = 20
    #verificar o campo telefone
admin.site.register(SubUnidade,SubUnidades)

class Unidades(admin.ModelAdmin):
    list_diplay = ('departamento','subunidades')
    #list_display_link = ('usuario')
    list_per_page = 20
    #verifcar o campo departamento aqui
admin.site.register(Unidade,Unidades)
