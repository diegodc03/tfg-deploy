from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsDefenseSummary(models.Model):
    
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    tackles = models.IntegerField(null=True, blank=True)
    tackles_won = models.IntegerField(null=True, blank=True)
    tackles_def_3rd = models.IntegerField(null=True, blank=True)
    tackles_mid_3rd = models.IntegerField(null=True, blank=True)
    tackles_att_3rd = models.IntegerField(null=True, blank=True)
    challenge_tackles = models.IntegerField(null=True, blank=True)
    challenges = models.IntegerField(null=True, blank=True)
    challenge_tackles_pct = models.FloatField(null=True, blank=True)
    challenged_lost = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    blocked_shots = models.IntegerField(null=True, blank=True)
    blocked_passes = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    tackles_interceptions = models.IntegerField(null=True, blank=True)
    clearances = models.IntegerField(null=True, blank=True)
    errors = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'stats_defensiveactions_summary'
