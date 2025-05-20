from django.db import models
from ..football_match import FootballMatch
from ..player import Player
from ..body_part import BodyPart
from ..event_shots import EventShots
from ..outcome_stats import OutcomeStats
from ..football_match import FootballMatch
from ..team import Team

class StatsShotsSummary(models.Model):
    estatistic_id = models.AutoField(primary_key=True, db_column='estatistic_id')
    match_id = models.ForeignKey(FootballMatch, on_delete=models.CASCADE, db_column='match_id')
    shot_minute = models.CharField(max_length=255, null=True, blank=True)
    player_shot = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_shot')
    team_shot = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='team_shot')
    xg = models.FloatField(null=True, blank=True)
    psxg = models.FloatField(null=True, blank=True)
    outcome = models.ForeignKey(OutcomeStats, on_delete=models.CASCADE, db_column='outcome', null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE, db_column='body_part', null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    player_assisted_1 = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_assisted_1', null=True, blank=True)
    event_type = models.ForeignKey(EventShots, on_delete=models.CASCADE, db_column='event_type', null=True, blank=True)
    player_assisted_2 = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player_assisted_2', null=True, blank=True)
    event_type_2 = models.ForeignKey(EventShots, on_delete=models.CASCADE, db_column='event_type_2', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'stats_shots_summary'  # Ajusta el nombre según el real en tu DB
