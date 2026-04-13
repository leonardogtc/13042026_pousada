from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Quarto(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    capacidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    esta_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"Quarto {self.numero} - (Capacidade: {self.capacidade})"

    class Meta:
        verbose_name = "Quarto"
        verbose_name_plural = "Quartos"


class Hospede(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    eh_principal = models.BooleanField(default=False)
    # Relacionamento para acompanhantes
    responsavel = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='acompanhantes'
    )

    def __str__(self):
        return f"{self.nome} {'- Principal' if self.eh_principal else ''}"

    class Meta:
        verbose_name = "Hóspede"
        verbose_name_plural = "Hóspedes"


class Estadia(models.Model):
    CLASSIFICACAO = [
        ("PERNOITE", "Pernoite"),
        ("DIARIA", "Diária"),
        ("MENSAL", "Mensal"),
    ]
    hospede_principal = models.ForeignKey(
        Hospede,
        on_delete=models.CASCADE,
        limit_choices_to={'eh_principal': True},
        related_name='estadia_principal'
    )
    quarto = models.ForeignKey(
        Quarto,
        on_delete=models.CASCADE,
    )
    tipo_hospede = models.CharField(max_length=20, choices=CLASSIFICACAO)
    data_saida_prevista = models.DateTimeField()
    data_saida_real = models.DateTimeField(blank=True, null=True)

    # Avaliação (Uma única vez por estaria)
    nota = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"Estadia de {self.hospede_principal.nome} "
            f"no Quarto {self.quarto.numero}"
        )
