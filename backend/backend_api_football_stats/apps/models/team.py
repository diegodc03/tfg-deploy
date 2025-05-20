


from .tournament import Tournament  # Importa el modelo Tournament desde el mismo paquete
from django.db import models

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)  # ID del equipo, AUTO_INCREMENT
    team_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del equipo
    tournament_team_id = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True, blank=True, db_column='tournament_team_id')  # FK a Tournament

    class Meta:
        managed = False  # No se gestionará automáticamente por Django
        db_table = 'team'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre_equipo} ({self.short_name})"