from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsMiscellaneousSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    cards_yellow = models.IntegerField(null=True, blank=True)
    cards_red = models.IntegerField(null=True, blank=True)
    cards_yellow_red = models.IntegerField(null=True, blank=True)

    fouls = models.IntegerField(null=True, blank=True)
    fouled = models.IntegerField(null=True, blank=True)
    offsides = models.IntegerField(null=True, blank=True)

    crosses = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    tackles_won = models.IntegerField(null=True, blank=True)

    pens_won = models.IntegerField(null=True, blank=True)
    pens_conceded = models.IntegerField(null=True, blank=True)
    own_goals = models.IntegerField(null=True, blank=True)

    ball_recoveries = models.IntegerField(null=True, blank=True)

    aerials_won = models.IntegerField(null=True, blank=True)
    aerials_lost = models.IntegerField(null=True, blank=True)
    aerials_won_pct = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_miscellaneous_summary'
