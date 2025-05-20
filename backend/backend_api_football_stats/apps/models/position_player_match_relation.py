from . import FootballMatch
from . import Player
from . import SpecificsPositionsByCategory
from django.db import models


class PositionMatchPlayerRelation(models.Model):


    position_id = models.ForeignKey(
        SpecificsPositionsByCategory,
        on_delete=models.CASCADE,
        db_column='position_id',
    )
    
    player_id = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        db_column='player_id',
    )
    
    match_id = models.ForeignKey(
        FootballMatch,
        on_delete=models.CASCADE,
        db_column='match_id',
    )
    
    class Meta:
        managed = False
        db_table = 'position_player'
