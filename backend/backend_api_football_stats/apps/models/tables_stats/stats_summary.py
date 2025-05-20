from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    pens_made = models.IntegerField(null=True, blank=True)
    pens_att = models.IntegerField(null=True, blank=True)
    shots = models.IntegerField(null=True, blank=True)
    shots_on_target = models.IntegerField(null=True, blank=True)
    cards_yellow = models.IntegerField(null=True, blank=True)
    cards_red = models.IntegerField(null=True, blank=True)
    touches = models.IntegerField(null=True, blank=True)
    tackles = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)

    xg = models.FloatField(null=True, blank=True)
    npxg = models.FloatField(null=True, blank=True)
    xg_assist = models.FloatField(null=True, blank=True)

    sca = models.IntegerField(null=True, blank=True)
    gca = models.IntegerField(null=True, blank=True)

    passes_completed = models.IntegerField(null=True, blank=True)
    passes = models.IntegerField(null=True, blank=True)
    passes_pct = models.FloatField(null=True, blank=True)
    progressive_passes = models.IntegerField(null=True, blank=True)

    carries = models.IntegerField(null=True, blank=True)
    progressive_carries = models.IntegerField(null=True, blank=True)
    take_ons = models.IntegerField(null=True, blank=True)
    take_ons_won = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_summary'
