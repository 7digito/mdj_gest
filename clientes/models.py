from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # ID não incrementável
    nome = models.CharField(max_length=100)
    nif = models.CharField(max_length=15, verbose_name="Número de Identificação Fiscal")  # NIF
    morada = models.CharField(max_length=255)  # Morada
    codigo_postal = models.CharField(max_length=10, verbose_name="Código Postal")  # Código Postal
    localidade = models.CharField(max_length=100)  # Localidade
    telefone = models.CharField(max_length=15)  # Telefone
    email = models.EmailField()  # Email
    website = models.URLField(blank=True, null=True)  # Website (opcional)

    def __str__(self):
        return self.nome