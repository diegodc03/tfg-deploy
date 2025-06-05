
from rest_framework import serializers

from ..models.tables_stats.stats_defensiveactions_summary import StatsDefenseSummary
from ..models.tables_stats.stats_gk_summary import StatsGoalkeeperSummary
from ..models.tables_stats.stats_miscellaneous_summary import StatsMiscellaneousSummary
from ..models.tables_stats.stats_passing_summary import StatsPassingSummary
from ..models.tables_stats.stats_passtypes_summary import StatsPassTypesSummary
from ..models.tables_stats.stats_possesion_summary import StatsPossessionSummary
from ..models.tables_stats.stats_summary import StatsSummary

from ..serializers_dto.serializers import PlayerNameSerializer, PlayerSerializer




class StatsSummarySerializer(serializers.ModelSerializer):
    
    player_id = PlayerSerializer()
    
    class Meta:
        model = StatsSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'pens_made',
            'pens_att',
            'shots',
            'shots_on_target',
            'cards_yellow',
            'cards_red',
            'touches',
            'tackles',
            'interceptions',
            'blocks',
            'xg',
            'npxg',
            'xg_assist',
            'sca',
            'gca',
            'passes_completed',
            'passes',
            'passes_pct',
            'progressive_passes',
            'carries',
            'progressive_carries',
            'take_ons',
            'take_ons_won',
        ]
        
        
class StatsDefensiveActionsSerializer(serializers.ModelSerializer):
    
    player_id = PlayerSerializer()
    
    class Meta:
        model = StatsDefenseSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'tackles',
            'tackles_won',
            'tackles_def_3rd',
            'tackles_mid_3rd',
            'tackles_att_3rd',
            'challenge_tackles',
            'challenges',
            'challenge_tackles_pct',
            'challenged_lost',
            'blocks',
            'blocked_shots',
            'blocked_passes',
            'interceptions',
            'tackles_interceptions',
            'clearances',
            'errors',
            
        ]
        
        
        
class StatsGKSerializer(serializers.ModelSerializer):
    
    player_id = PlayerSerializer()
    
    class Meta:
        model = StatsGoalkeeperSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'gk_shots_on_target_against',
            'gk_goals_against',
            'gk_saves',
            'gk_save_pct',
            'gk_psxg',
            'gk_passes_completed_launched',
            'gk_passes_launched',
            'gk_passes_pct_launched',
            'gk_passes',
            'gk_passes_throws',
            'gk_pct_passes_launched',
            'gk_passes_length_avg',
            'gk_goal_kicks',
            'gk_pct_goal_kicks_launched',
            'gk_goal_kick_length_avg',
            'gk_crosses',
            'gk_crosses_stopped',
            'gk_crosses_stopped_pct',
            'gk_def_actions_outside_pen_area',
            'gk_avg_distance_def_actions',
            
        ]




class StatsMiscellaneousSerializer(serializers.ModelSerializer):
    
    player_id = PlayerSerializer()
    
    class Meta:
        model = StatsMiscellaneousSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'cards_yellow',
            'cards_red',
            'cards_yellow_red',
            'fouls',
            'fouled',
            'offsides',
            'crosses',
            'interceptions',
            'tackles_won',
            'pens_won',
            'pens_conceded',
            'own_goals',
            'ball_recoveries',
            'aerials_won',
            'aerials_lost',
            'aerials_won_pct',
        ]
        
        
class StatsPassingSerializer(serializers.ModelSerializer):
    
    player_id = PlayerSerializer()
    
    class Meta:
        model = StatsPassingSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'passes_completed',
            'passes',
            'passes_pct',
            'passes_total_distance',
            'passes_progressive_distance',
            'passes_completed_short',
            'passes_short',
            'passes_pct_short',
            'passes_completed_medium',
            'passes_medium',
            'passes_pct_medium',
            'passes_completed_long',
            'passes_long',
            'passes_pct_long',
            'xg_assists',
            'pass_xa',
            'assisted_shots',
            'passes_into_final_third',
            'passes_into_penalty_area',
            'crosses_into_penalty_area',
            'progressive_passes',
        ]
        

class StatsPassTypesSerializer(serializers.ModelSerializer):
    player_id = PlayerSerializer()

    class Meta:
        model = StatsPassTypesSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            'passes',
            'passes_live',
            'passes_dead',
            'passes_free_kicks',
            'through_balls',
            'passes_switches',
            'crosses',
            'throw_ins',
            'corner_kicks',
            'corner_kicks_in',
            'corner_kicks_out',
            'corner_kicks_straight',
            'passes_completed',
            'passes_offsides',
            'passes_blocked'
        ]



class StatsPossessionSerializer(serializers.ModelSerializer):
    player_id = PlayerSerializer()

    class Meta:
        model = StatsPossessionSummary
        fields = [
            'estatistic_id',
            'stat_id',
            'player_id',
            
            'touches',
            'touches_def_pen_area',
            'touches_def_3rd',
            'touches_mid_3rd',
            'touches_att_3rd',
            'touches_att_pen_area',
            'touches_live_ball',
            
            'take_ons',
            'take_ons_won',
            'take_ons_won_pct',
            'take_ons_tackled',
            'take_ons_tackled_pct',
            
            'carries',
            'carries_distance',
            'carries_progressive_distance',
            'progressive_carries',
            'carries_into_final_third',
            'carries_into_penalty_area',
            
            'miscontrols',
            'dispossessed',
            'passes_received',
            'progressive_passes_received'
        ]


