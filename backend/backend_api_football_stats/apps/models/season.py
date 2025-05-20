# apps/api/models/season.py
from django.db import models

class Season(models.Model):
    season_id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    season_year = models.CharField(max_length=255, null=True, blank=True)  # Año de la temporada (puede ser nulo)

    class Meta:
        managed = False  # No se gestionará automáticamente por Django
        db_table = 'season'
    
    
    def __str__(self):
        return f"Season {self.season_year if self.season_year else 'Unknown'}"
