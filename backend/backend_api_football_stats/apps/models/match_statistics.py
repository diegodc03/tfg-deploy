
from django.db import models

from .football_match import FootballMatch
from .player import Player


class MatchStatistics(models.Model):
    
    estadistica_id = models.AutoField(primary_key=True, db_column='estadistica_id')  
    match_id = models.ForeignKey(FootballMatch, on_delete=models.SET_NULL, null=True, blank=True, db_column='match_id')
    player_id = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, db_column='player_id')
    minutes = models.IntegerField(null=True, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        managed = False
        db_table = 'match_statistics'
    
    
    
    
    
    