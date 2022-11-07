from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=200, null=False)
  email = models.EmailField()

  def __str__(self):
    return self.nome

class Produto(models.Model):
  titulo = models.CharField(max_length=300, null=False)
  preço = models.FloatField()

  def __str__(self):
    return self.titulo

class Pedido(models.Model):

  status = (
    ('Em andamento','Em andamento'),
    ('Entregue','Entregue')
  )

  valor = models.FloatField()
  cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  status = models.CharField(max_length=100, choices=status)
  produtos = models.ManyToManyField("Produto")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.status}, {self.cliente_id}'






