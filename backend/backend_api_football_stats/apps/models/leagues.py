from django.db import models

class Leagues(models.Model):
    
    id = models.AutoField(primary_key=True)  # ID del equipo, AUTO_INCREMENT
    name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del equipo
    
    class Meta:
        db_table = 'leagues'
        managed = False
    