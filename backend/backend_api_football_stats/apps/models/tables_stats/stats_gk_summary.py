from django.db import models
from ..match_statistics import MatchStatistics
from ..player import Player

class StatsGoalkeeperSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    stat_id = models.ForeignKey(MatchStatistics, on_delete=models.CASCADE, db_column='stat_id')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_id')

    gk_shots_on_target_against = models.IntegerField(null=True, blank=True)
    gk_goals_against = models.IntegerField(null=True, blank=True)
    gk_saves = models.IntegerField(null=True, blank=True)
    gk_save_pct = models.FloatField(null=True, blank=True)
    gk_psxg = models.FloatField(null=True, blank=True)

    gk_passes_completed_launched = models.IntegerField(null=True, blank=True)
    gk_passes_launched = models.IntegerField(null=True, blank=True)
    gk_passes_pct_launched = models.FloatField(null=True, blank=True)

    gk_passes = models.IntegerField(null=True, blank=True)
    gk_passes_throws = models.IntegerField(null=True, blank=True)
    gk_pct_passes_launched = models.FloatField(null=True, blank=True)
    gk_passes_length_avg = models.FloatField(null=True, blank=True)

    gk_goal_kicks = models.IntegerField(null=True, blank=True)
    gk_pct_goal_kicks_launched = models.FloatField(null=True, blank=True)
    gk_goal_kick_length_avg = models.FloatField(null=True, blank=True)

    gk_crosses = models.IntegerField(null=True, blank=True)
    gk_crosses_stopped = models.IntegerField(null=True, blank=True)
    gk_crosses_stopped_pct = models.FloatField(null=True, blank=True)

    gk_def_actions_outside_pen_area = models.IntegerField(null=True, blank=True)
    gk_avg_distance_def_actions = models.FloatField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_gk_summary'
