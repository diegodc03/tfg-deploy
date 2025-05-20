from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsPassingSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    passes_completed = models.IntegerField(null=True, blank=True)
    passes = models.IntegerField(null=True, blank=True)
    passes_pct = models.FloatField(null=True, blank=True)
    passes_total_distance = models.FloatField(null=True, blank=True)
    passes_progressive_distance = models.FloatField(null=True, blank=True)

    passes_completed_short = models.IntegerField(null=True, blank=True)
    passes_short = models.IntegerField(null=True, blank=True)
    passes_pct_short = models.FloatField(null=True, blank=True)

    passes_completed_medium = models.IntegerField(null=True, blank=True)
    passes_medium = models.IntegerField(null=True, blank=True)
    passes_pct_medium = models.FloatField(null=True, blank=True)

    passes_completed_long = models.IntegerField(null=True, blank=True)
    passes_long = models.IntegerField(null=True, blank=True)
    passes_pct_long = models.FloatField(null=True, blank=True)

    xg_assists = models.FloatField(null=True, blank=True)
    pass_xa = models.FloatField(null=True, blank=True)
    assisted_shots = models.IntegerField(null=True, blank=True)

    passes_into_final_third = models.IntegerField(null=True, blank=True)
    passes_into_penalty_area = models.IntegerField(null=True, blank=True)
    crosses_into_penalty_area = models.IntegerField(null=True, blank=True)
    progressive_passes = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_passing_summary'
