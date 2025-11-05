from django.db import models

class CampoSasFoco(models.Model):
    """
    Armazena o mapeamento entre os campos do SAS antigo e os campos
    correspondentes no FOCO (Salesforce).
    """
    # Campos SAS
    NomeSAS = models.CharField(max_length=255, verbose_name="Nome do campo no SAS")
    DescricaoSAS = models.TextField(blank=True, null=True, verbose_name="Descrição do campo no SAS")
    TipoSAS = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de dado no SAS")
    ObrigatorioSAS = models.CharField(max_length=10, blank=True, null=True, verbose_name="Obrigatório no SAS")

    # Campos FOCO (Salesforce)
    ObjetoFOCO = models.CharField(max_length=255, verbose_name="Nome do objeto no FOCO")
    RotuloFOCO = models.CharField(max_length=255, blank=True, null=True, verbose_name="Rótulo do campo no FOCO")
    NomeFOCO = models.CharField(max_length=255, verbose_name="Nome do campo no FOCO")
    DescricaoFOCO = models.TextField(blank=True, null=True, verbose_name="Descrição do campo no FOCO")
    TipoFOCO = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de dado no FOCO")
    ObrigatorioFOCO = models.CharField(max_length=10, blank=True, null=True, verbose_name="Obrigatório no FOCO")

    # Metadados
    Observacoes = models.TextField(blank=True, null=True, verbose_name="Observações adicionais")
    Descontinuado = models.BooleanField(default=False, verbose_name="Campo do SAS foi descontinuado")

    class Meta:
        verbose_name = "Mapeamento Campo SAS x FOCO"
        verbose_name_plural = "Mapeamentos Campos SAS x FOCO"
        # unique index em (ObjetoFOCO, NomeFOCO)
        constraints = [
            models.UniqueConstraint(fields=['ObjetoFOCO', 'NomeFOCO'], name='unique_objeto_nome_foco')
        ]

    def __str__(self):
        return f"{self.NomeSAS} -> {self.ObjetoFOCO}.{self.NomeFOCO}"


class EndpointSasFoco(models.Model):
    """
    Armazena os endpoints do SAS que serão mapeados.
    """
    NomeEndpointSAS = models.CharField(max_length=255, unique=True, verbose_name="Nome do endpoint no SAS")
    DescricaoEndpointSAS = models.TextField(blank=True, null=True, verbose_name="Descrição do endpoint no SAS")

    # Relacionamento muitos-para-muitos com CampoSasFoco
    campos = models.ManyToManyField(
        CampoSasFoco,
        through='MapeamentoEndpointCampo',  # Usando a tabela 'through' customizada
        related_name='endpoints'
    )

    class Meta:
        verbose_name = "Endpoint SAS"
        verbose_name_plural = "Endpoints SAS"

    def __str__(self):
        return self.NomeEndpointSAS


class MapeamentoEndpointCampo(models.Model):
    """
    Tabela de junção (through table) que liga Endpoints aos Campos.
    """
    IdEndpointSAS = models.ForeignKey(
        EndpointSasFoco,
        on_delete=models.CASCADE,
        verbose_name="Endpoint SAS"
    )
    IdCampoSASFoco = models.ForeignKey(
        CampoSasFoco,
        on_delete=models.CASCADE,
        verbose_name="Campo SAS/FOCO"
    )

    class Meta:
        verbose_name = "Mapeamento Endpoint x Campo"
        verbose_name_plural = "Mapeamentos Endpoint x Campo"
        # Garante que cada par endpoint-campo seja único
        unique_together = ('IdEndpointSAS', 'IdCampoSASFoco')

    def __str__(self):
        return f"{self.IdEndpointSAS} usa {self.IdCampoSASFoco}"