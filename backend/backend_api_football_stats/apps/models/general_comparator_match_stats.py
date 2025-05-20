from django.db import models


class GeneralComparatorMatchStats(models.Model):
    
    
    estadistica_id = models.AutoField(primary_key=True, db_column='estadistica_id')  # Clave primaria auto incremental

    local_aerials_won = models.FloatField(null=True, blank=True)
    visitor_aerials_won = models.FloatField(null=True, blank=True)
    local_cards = models.FloatField(null=True, blank=True)
    visitor_cards = models.FloatField(null=True, blank=True)
    local_clearances = models.FloatField(null=True, blank=True)
    visitor_clearances = models.FloatField(null=True, blank=True)
    local_corners = models.FloatField(null=True, blank=True)
    visitor_corners = models.FloatField(null=True, blank=True)
    local_crosses = models.FloatField(null=True, blank=True)
    visitor_crosses = models.FloatField(null=True, blank=True)
    local_fouls = models.FloatField(null=True, blank=True)
    visitor_fouls = models.FloatField(null=True, blank=True)
    local_goal_kicks = models.FloatField(null=True, blank=True)
    visitor_goal_kicks = models.FloatField(null=True, blank=True)
    local_interceptions = models.FloatField(null=True, blank=True)
    visitor_interceptions = models.FloatField(null=True, blank=True)
    local_long_balls = models.FloatField(null=True, blank=True)
    visitor_long_balls = models.FloatField(null=True, blank=True)
    local_offsides = models.FloatField(null=True, blank=True)
    visitor_offsides = models.FloatField(null=True, blank=True)
    local_passing_accuracy = models.FloatField(null=True, blank=True)
    visitor_passing_accuracy = models.FloatField(null=True, blank=True)
    local_possession = models.FloatField(null=True, blank=True)
    visitor_possession = models.FloatField(null=True, blank=True)
    local_saves = models.FloatField(null=True, blank=True)
    visitor_saves = models.FloatField(null=True, blank=True)
    local_shots_on_target = models.FloatField(null=True, blank=True)
    visitor_shots_on_target = models.FloatField(null=True, blank=True)
    local_tackles = models.FloatField(null=True, blank=True)
    visitor_tackles = models.FloatField(null=True, blank=True)
    local_throw_ins = models.FloatField(null=True, blank=True)
    visitor_throw_ins = models.FloatField(null=True, blank=True)
    local_touches = models.FloatField(null=True, blank=True)
    visitor_touches = models.FloatField(null=True, blank=True)
    
    match_id = models.ForeignKey('FootballMatch', on_delete=models.CASCADE, db_column='match_id', related_name='general_comparator_match_stats')
    
    
    class Meta:
        managed = False
        db_table = 'estadisticas_partido_gen'