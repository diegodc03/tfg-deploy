

from .tournament import Tournament  # Importa el modelo Tournament desde el mismo paquete
from django.db import models
from .team import Team  # Importa el modelo Team desde el mismo paquete
from .player import Player  # Importa el modelo Player desde el mismo paquete


class TeamPlayer(models.Model):
    
    team_id = models.ForeignKey(
        Team,  # Referencia al modelo Team
        on_delete=models.CASCADE,
        db_column='team_id',  # Nombre de la columna en la base de datos
    )
    player_id = models.ForeignKey(
        Player,  # Referencia al modelo Player (asegúrate de que Player esté definido)
        on_delete=models.CASCADE,
        db_column='player_id',  # Nombre de la columna en la base de datos
    )

    class Meta:
        managed = False  # No se gestionará automáticamente por Django
        db_table = 'team_player'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre_equipo} ({self.short_name})"