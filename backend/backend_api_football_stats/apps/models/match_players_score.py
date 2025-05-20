
from django.db import models

from .basic_position_category import BasicPositionCategory
from .specifics_positions_by_category import SpecificsPositionsByCategory
from .match_statistics import MatchStatistics
from .game_modes import GameMode


class MatchPlayerScore(models.Model):
    match_player_score_id = models.AutoField(primary_key=True, db_column='match_player_score_id')
    match_player_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='match_player_id')
    specific_position_id = models.ForeignKey(SpecificsPositionsByCategory, on_delete=models.SET_NULL, null=True, blank=True, db_column='specific_position_id')
    basic_position_id = models.ForeignKey(BasicPositionCategory, on_delete=models.SET_NULL, null=True, blank=True, db_column='basic_position_id')
    score = models.FloatField()
    game_mode_id = models.ForeignKey(GameMode, on_delete=models.SET_NULL, null=True, blank=True, db_column='game_mode_id')

    class Meta:
        db_table = 'match_players_score'