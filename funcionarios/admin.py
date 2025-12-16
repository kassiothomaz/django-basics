from django.contrib import admin
from .models import Funcionario, Eduardo, Dominique,Kassiooo
# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')

@admin.register(Kassiooo)
class KassioooAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','end')
  
    
@admin.register(Dominique)
class DominiqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cor')
