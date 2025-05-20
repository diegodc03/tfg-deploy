# apps/api/models/tournament.py
from django.db import models
from .season import Season  # Importamos Season desde season.py
from .leagues import Leagues  # Importamos Leagues desde leagues.py

 # CUIDADO CON LOS IDS AL FINAL, --> AÑADE OTRO

class Tournament(models.Model):
    tournament_id = models.AutoField(primary_key=True)  # ID del torneo, AUTO_INCREMENT
    nombre_liga = models.CharField(max_length=255, null=True, blank=True)  # Nombre de la liga
    season_tournament = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)  # FK a Season
    type_of_competition = models.CharField(max_length=255, null=True, blank=True)  # Tipo de competición
    tournament_fbref_id = models.CharField(max_length=255, null=True, blank=True)  # ID de FBref
    league = models.ForeignKey(Leagues, on_delete=models.SET_NULL, null=True, blank=True)  # FK a Leagues 

    class Meta:
        managed = False  # No se gestionará automáticamente por Django
        db_table = 'tournament'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f"{self.nombre_liga} - {self.season_tournament.season_year if self.season_tournament else 'No Season'}"

