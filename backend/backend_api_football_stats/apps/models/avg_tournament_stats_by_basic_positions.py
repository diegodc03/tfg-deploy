    
        
from django.db import models
from .team import Team
from .leagues import Leagues
from .basic_position_category import BasicPositionCategory

class AvgTournamentStatsByBasicPositions(models.Model):
    
    id = models.AutoField(primary_key=True, db_column='id')
    league_id = models.IntegerField(Leagues, null=True, blank=True, db_column='league_id')
    #team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, db_column='team_id')
    
    
    position_player = models.ForeignKey(BasicPositionCategory, on_delete=models.CASCADE, null=True, blank=True, db_column='position_player')
        
    TYPE_OF_STATS_CHOICES = [
        ('desv', 'Desviación'),
        ('mode', 'Moda'),
        ('avg', 'Promedio')
    ]

    type_of_stats = models.CharField(
        max_length=10,
        choices=TYPE_OF_STATS_CHOICES,
        null=True,
        blank=True
    )
    
    
    
    STARTER_STATUS_CHOICES = [
        ('starter', 'Starter'),
        ('substitute', 'Substitute')
    ]
    starter_status = models.CharField(
        max_length=10,
        choices=STARTER_STATUS_CHOICES,
        null=True,
        blank=True
    )
    
    # GK Stats
    gk_shots_on_target_against = models.FloatField(null=True, blank=True)
    gk_goals_against = models.FloatField(null=True, blank=True)
    gk_saves = models.FloatField(null=True, blank=True)
    gk_save_pct = models.FloatField(null=True, blank=True)
    gk_psxg = models.FloatField(null=True, blank=True)
    gk_passes_completed_launched = models.FloatField(null=True, blank=True)
    gk_passes_launched = models.FloatField(null=True, blank=True)
    gk_passes_pct_launched = models.FloatField(null=True, blank=True)
    gk_passes = models.FloatField(null=True, blank=True)
    gk_passes_throws = models.FloatField(null=True, blank=True)
    gk_pct_passes_launched = models.FloatField(null=True, blank=True)
    gk_passes_length_avg = models.FloatField(null=True, blank=True)
    gk_goal_kicks = models.FloatField(null=True, blank=True)
    gk_pct_goal_kicks_launched = models.FloatField(null=True, blank=True)
    gk_goal_kick_length_avg = models.FloatField(null=True, blank=True)
    gk_crosses = models.FloatField(null=True, blank=True)
    gk_crosses_stopped = models.FloatField(null=True, blank=True)
    gk_crosses_stopped_pct = models.FloatField(null=True, blank=True)
    gk_def_actions_outside_pen_area = models.FloatField(null=True, blank=True)
    gk_avg_distance_def_actions = models.FloatField(null=True, blank=True)

    # Offensive Stats
    goals = models.FloatField(null=True, blank=True)
    assists = models.FloatField(null=True, blank=True)
    pens_made = models.FloatField(null=True, blank=True)
    pens_att = models.FloatField(null=True, blank=True)
    shots = models.FloatField(null=True, blank=True)
    shots_on_target = models.FloatField(null=True, blank=True)
    
    # Cards
    cards_yellow = models.FloatField(null=True, blank=True)
    cards_red = models.FloatField(null=True, blank=True)
    cards_yellow_red = models.FloatField(null=True, blank=True)

    # Defensive Stats
    tackles = models.FloatField(null=True, blank=True)
    interceptions = models.FloatField(null=True, blank=True)
    blocks = models.FloatField(null=True, blank=True)
    tackles_interceptions = models.FloatField(null=True, blank=True)
    clearances = models.FloatField(null=True, blank=True)
    errors = models.FloatField(null=True, blank=True)

    # Advanced Stats
    xg = models.FloatField(null=True, blank=True)
    npxg = models.FloatField(null=True, blank=True)
    xg_assist = models.FloatField(null=True, blank=True)
    sca = models.FloatField(null=True, blank=True)
    gca = models.FloatField(null=True, blank=True)

    # Passing Stats
    passes_completed = models.FloatField(null=True, blank=True)
    passes = models.FloatField(null=True, blank=True)
    passes_pct = models.FloatField(null=True, blank=True)
    progressive_passes = models.FloatField(null=True, blank=True)
    passes_total_distance = models.FloatField(null=True, blank=True)
    passes_progressive_distance = models.FloatField(null=True, blank=True)
    
    # Carries and Take-ons
    carries = models.FloatField(null=True, blank=True)
    progressive_carries = models.FloatField(null=True, blank=True)
    carries_distance = models.FloatField(null=True, blank=True)
    carries_progressive_distance = models.FloatField(null=True, blank=True)
    carries_into_final_third = models.FloatField(null=True, blank=True)
    carries_into_penalty_area = models.FloatField(null=True, blank=True)
    take_ons = models.FloatField(null=True, blank=True)
    take_ons_won = models.FloatField(null=True, blank=True)
    take_ons_won_pct = models.FloatField(null=True, blank=True)
    take_ons_tackled = models.FloatField(null=True, blank=True)
    take_ons_tackled_pct = models.FloatField(null=True, blank=True)

    # Additional Stats (Grouped for brevity)
    passes_short = models.FloatField(null=True, blank=True)
    passes_completed_short = models.FloatField(null=True, blank=True)
    passes_pct_short = models.FloatField(null=True, blank=True)
    passes_medium = models.FloatField(null=True, blank=True)
    passes_completed_medium = models.FloatField(null=True, blank=True)
    passes_pct_medium = models.FloatField(null=True, blank=True)
    passes_long = models.FloatField(null=True, blank=True)
    passes_completed_long = models.FloatField(null=True, blank=True)
    passes_pct_long = models.FloatField(null=True, blank=True)
    pass_xa = models.FloatField(null=True, blank=True)
    assisted_shots = models.FloatField(null=True, blank=True)
    passes_into_final_third = models.FloatField(null=True, blank=True)
    passes_into_penalty_area = models.FloatField(null=True, blank=True)
    crosses_into_penalty_area = models.FloatField(null=True, blank=True)
    passes_live = models.FloatField(null=True, blank=True)
    passes_dead = models.FloatField(null=True, blank=True)
    passes_free_kicks = models.FloatField(null=True, blank=True)
    through_balls = models.FloatField(null=True, blank=True)
    passes_switches = models.FloatField(null=True, blank=True)
    crosses = models.FloatField(null=True, blank=True)
    throw_ins = models.FloatField(null=True, blank=True)
    corner_kicks = models.FloatField(null=True, blank=True)
    corner_kicks_in = models.FloatField(null=True, blank=True)
    corner_kicks_out = models.FloatField(null=True, blank=True)
    corner_kicks_straight = models.FloatField(null=True, blank=True)
    passes_offsides = models.FloatField(null=True, blank=True)
    passes_blocked = models.FloatField(null=True, blank=True)

    # Tackles by zone
    tackles_won = models.FloatField(null=True, blank=True)
    tackles_def_3rd = models.FloatField(null=True, blank=True)
    tackles_mid_3rd = models.FloatField(null=True, blank=True)
    tackles_att_3rd = models.FloatField(null=True, blank=True)

    # Challenges
    challenge_tackles = models.FloatField(null=True, blank=True)
    challenges = models.FloatField(null=True, blank=True)
    challenge_tackles_pct = models.FloatField(null=True, blank=True)
    challenged_lost = models.FloatField(null=True, blank=True)

    # Blocks
    blocked_shots = models.FloatField(null=True, blank=True)
    blocked_passes = models.FloatField(null=True, blank=True)

    # Touches by zone
    touches = models.FloatField(null=True, blank=True)
    touches_def_pen_area = models.FloatField(null=True, blank=True)
    touches_def_3rd = models.FloatField(null=True, blank=True)
    touches_mid_3rd = models.FloatField(null=True, blank=True)
    touches_att_3rd = models.FloatField(null=True, blank=True)
    touches_att_pen_area = models.FloatField(null=True, blank=True)
    touches_live_ball = models.FloatField(null=True, blank=True)

    # Other
    miscontrols = models.FloatField(null=True, blank=True)
    dispossessed = models.FloatField(null=True, blank=True)
    passes_received = models.FloatField(null=True, blank=True)
    progressive_passes_received = models.FloatField(null=True, blank=True)
    fouls = models.FloatField(null=True, blank=True)
    fouled = models.FloatField(null=True, blank=True)
    offsides = models.FloatField(null=True, blank=True)
    pens_won = models.FloatField(null=True, blank=True)
    pens_conceded = models.FloatField(null=True, blank=True)
    own_goals = models.FloatField(null=True, blank=True)
    ball_recoveries = models.FloatField(null=True, blank=True)
    aerials_won = models.FloatField(null=True, blank=True)
    aerials_lost = models.FloatField(null=True, blank=True)
    aerials_won_pct = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Stats for Team {self.team_id} - League {self.league_id}"

    
    class Meta:
        managed = False
        db_table = 'avg_player_stats_by_basic_positions'