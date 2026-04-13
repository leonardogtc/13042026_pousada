from django.db import models


class ItemEstoque(models.Model):
    UNIDADES_MEDIDA = [
        ('UN', 'Unidade'),
        ('KG', 'Quilograma'),
        ('GR', 'Gramas'),
        ('LT', 'Litro'),
        ('ML', 'Mililitro'),
        ('CX', 'Caixa'),
        ('PC', 'Peça'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade_atual = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    quantidade_minima = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=5.00
    )
    unidade = models.CharField(
        max_length=10,
        choices=UNIDADES_MEDIDA,
        default='un')
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.quantidade_atual} {self.unidade}"

    class Meta:
        verbose_name = "Item de Estoque"
        verbose_name_plural = "Itens de Estoque"
