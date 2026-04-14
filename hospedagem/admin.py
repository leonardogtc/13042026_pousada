from django.contrib import admin
from .models import Quarto, Hospede, Estadia

class AcompanhanteInline(admin.TabularInline):
    model = Hospede
    extra = 1 # Quantidade de linhas em branco que aparecerão por padrão
    fk_name = 'responsavel' # Campo que relaciona o acompanhante ao responsável
    verbose_name = 'Acompanhante'
    verbose_name_plural = 'Acompanhantes'
    
@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    inlines = [AcompanhanteInline]
    list_display = ('nome', 'cpf', 'email', 'telefone', 'eh_principal')
    list_filter = ('eh_principal',)
    search_fields = ('nome', 'cpf', 'email')

admin.site.register(Quarto)
admin.site.register(Estadia)
