from django.contrib import admin
<<<<<<< HEAD
from .models import Funcionario,Kassiooo
=======
from .models import Funcionario, Eduardo, Dominique
>>>>>>> 2f73b115f3de6e5fa20f1e029d30e2217bb414e9
# Register your models here.


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','email', 'data_cadastro')
<<<<<<< HEAD

@admin.register(Kassiooo)
class KassioooAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf', 'meta', 'cargo','end')
=======
  
    
@admin.register(Dominique)
class DominiqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cor')
>>>>>>> 2f73b115f3de6e5fa20f1e029d30e2217bb414e9
