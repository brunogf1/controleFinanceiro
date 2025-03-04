from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Recebimento(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class Gasto(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"
    
class Etiqueta(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cor = models.CharField(max_length=7, default='#FFFFFF')  # Cor no formato hexadecimal
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
