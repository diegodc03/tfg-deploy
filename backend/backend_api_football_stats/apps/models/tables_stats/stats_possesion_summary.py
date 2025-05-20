from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsPossessionSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    touches = models.IntegerField(null=True, blank=True)
    touches_def_pen_area = models.IntegerField(null=True, blank=True)
    touches_def_3rd = models.IntegerField(null=True, blank=True)
    touches_mid_3rd = models.IntegerField(null=True, blank=True)
    touches_att_3rd = models.IntegerField(null=True, blank=True)
    touches_att_pen_area = models.IntegerField(null=True, blank=True)
    touches_live_ball = models.IntegerField(null=True, blank=True)

    take_ons = models.IntegerField(null=True, blank=True)
    take_ons_won = models.IntegerField(null=True, blank=True)
    take_ons_won_pct = models.FloatField(null=True, blank=True)
    take_ons_tackled = models.IntegerField(null=True, blank=True)
    take_ons_tackled_pct = models.FloatField(null=True, blank=True)

    carries = models.IntegerField(null=True, blank=True)
    carries_distance = models.IntegerField(null=True, blank=True)
    carries_progressive_distance = models.IntegerField(null=True, blank=True)
    progressive_carries = models.IntegerField(null=True, blank=True)
    carries_into_final_third = models.IntegerField(null=True, blank=True)
    carries_into_penalty_area = models.IntegerField(null=True, blank=True)

    miscontrols = models.IntegerField(null=True, blank=True)
    dispossessed = models.IntegerField(null=True, blank=True)

    passes_received = models.IntegerField(null=True, blank=True)
    progressive_passes_received = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_possession_summary'
