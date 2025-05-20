


from django.db import models
from .tournament import Tournament  # Importa el modelo Tournament desde el mismo paquete
from .team import Team  # Importa el modelo Team desde el mismo paquete

class FootballMatch(models.Model):


    match_id = models.AutoField(primary_key=True)  # ID del partido, AUTO_INCREMENT
    Home = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, db_column='Home',related_name='Home')  # FK a Team (equipo local)
    Away = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, db_column='Away', related_name='Away')  # FK a Team (equipo visitante)
    Wk = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Semana del partido
    Date = models.DateField(null=True, blank=True)  # Fecha del partido
    Score = models.CharField(max_length=255, null=True, blank=True)  # Resultado del partido
    Attendance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Asistencia al partido
    Venue = models.CharField(max_length=255, null=True, blank=True)  # Lugar del partido
    Referee = models.CharField(max_length=255, null=True, blank=True)  # Árbitro del partido
    Season = models.ForeignKey(Tournament, models.SET_NULL, null=True, blank=True, db_column='Season')  # FK a Tournament
    match_link = models.CharField(max_length=255, null=True, blank=True)  # Enlace al partido
    
    class Meta:
        managed = False
        db_table = 'football_match'
    
 