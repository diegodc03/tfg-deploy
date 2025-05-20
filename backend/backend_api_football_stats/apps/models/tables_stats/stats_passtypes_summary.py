from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsPassTypesSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    passes = models.IntegerField(null=True, blank=True)
    passes_live = models.IntegerField(null=True, blank=True)
    passes_dead = models.IntegerField(null=True, blank=True)
    passes_free_kicks = models.IntegerField(null=True, blank=True)
    through_balls = models.IntegerField(null=True, blank=True)
    passes_switches = models.IntegerField(null=True, blank=True)
    crosses = models.IntegerField(null=True, blank=True)
    throw_ins = models.IntegerField(null=True, blank=True)

    corner_kicks = models.IntegerField(null=True, blank=True)
    corner_kicks_in = models.IntegerField(null=True, blank=True)
    corner_kicks_out = models.IntegerField(null=True, blank=True)
    corner_kicks_straight = models.IntegerField(null=True, blank=True)

    passes_completed = models.IntegerField(null=True, blank=True)
    passes_offsides = models.IntegerField(null=True, blank=True)
    passes_blocked = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_passtypes_summary'
