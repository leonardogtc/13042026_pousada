from django.db import models


class Produto(models.Model):
    CATEGORIAS = [
        ('BEBIDA', 'Bebida'),
        ('PRATO', 'Prato'),
        ('SOBREMESA', 'Sobremesa'),
        ('OUTRO', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS),
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    # Aqui conectamos com o estoque! Se um prato usa um insumo específico
    insumo_base = models.ForeignKey(
        'estoque.ItemEstoque',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nome} - R${self.preco_venda}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Consumo(models.Model):
    # 'hospedagem.Estadia' ainda não existe, mas o Django aceita a string
    estadia = models.ForeignKey(
        'hospedagem.Estadia',
        on_delete=models.CASCADE,
        related_name='consumos'
    )
    '''
    Relacionamento entre Apps:
    Veja como ligamos o Produto ao ItemEstoque. Isso permite,
    futuramente, que quando a cozinha vender um prato, o sistema dê
    baixa automática no ingrediente lá no estoque.
    '''
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )
    quantidade = models.PositiveIntegerField(default=1)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.produto.nome} - {self.quantidade} unidades em "
            f"{self.data_hora.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    class Meta:
        verbose_name = "Consumo"
        verbose_name_plural = "Consumos"
