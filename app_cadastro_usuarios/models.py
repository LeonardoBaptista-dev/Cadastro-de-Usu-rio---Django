from django.db import models


class Usuario(models.Model):

    # Criar id sequencial não duplicavel para cada usuario cadastrado no banco de dados
    id_usuario = models.AutoField(primary_key=True)  
    
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
