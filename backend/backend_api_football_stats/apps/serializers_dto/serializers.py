from rest_framework import serializers

from ..models.tables_stats.stats_summary import StatsSummary

from ..models.leagues import Leagues
from ..models.season import Season
from ..models.tournament import Tournament
from ..models.team import Team
from ..models.football_match import FootballMatch
from ..models.general_comparator_match_stats import GeneralComparatorMatchStats
from ..models.match_players_score import MatchPlayerScore
from ..models.game_modes import GameMode
from ..models.basic_position_category import BasicPositionCategory
from ..models.specifics_positions_by_category import SpecificsPositionsByCategory
from ..models.match_statistics import MatchStatistics
from ..models.player import Player
# serializers.py


class SeasonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Season
        fields = ['season_id', 'season_year']



class SeasonTournamentSerializer(serializers.ModelSerializer):
    
    season_tournament = SeasonSerializer(read_only=True)  # Aquí anidamos la info de la temporada
    class Meta:
        model = Tournament
        fields = ['tournament_id', 'nombre_liga', 'season_tournament']
       
        
        
class TournamentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tournament
        fields = ['tournament_id', 'nombre_liga']  # Aquí puedes agregar otros campos que necesites
        
        
class TournamentOnlyNameSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Tournament
            fields = ['tournament_id', 'nombre_liga']  # Aquí puedes agregar otros campos que necesites
        
        
class SeasonOnlySeasonYearSerializer(serializers.ModelSerializer):
    
    
    class Meta:    
        model = Season
        fields = ['season_year']
        
        
class SeasonTournamentOnlySeasonYearSerializer(serializers.ModelSerializer):
    
    season_tournament = SeasonOnlySeasonYearSerializer(read_only=True)  # Aquí anidamos la info de la temporada
    class Meta:
        model = Tournament
        fields = ['tournament_id', 'nombre_liga', 'season_tournament']
        
        

######## Team serializers ###########

class TeamSerializer(serializers.ModelSerializer):
    
    tournament_team_id = TournamentSerializer(read_only=True)  # Aquí anidamos la info del torneo
    class Meta:
        model = Team
        fields = ['team_id', 'team_name', 'tournament_team_id']  # Aquí puedes agregar otros campos que necesites
        
        
class TeamOnlyNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = ['team_id', 'team_name']  # Aquí puedes agregar otros campos que necesites

        
        
######## Football match serializers ###########


class FootballMatchSerializer(serializers.ModelSerializer):
    
    Home = TeamOnlyNameSerializer(read_only=True)  # Aquí anidamos la info del equipo local
    Away = TeamOnlyNameSerializer(read_only=True)  # Aquí anidamos la info del equipo visitante
    Season = TournamentOnlyNameSerializer(read_only=True)  # Aquí anidamos la info de la temporada del torneo
    class Meta:
        model = FootballMatch
        fields = ['match_id', 'Home', 'Away', 'Score', 'Wk', 'Date', 'Season']
     
     
     

class FootballMatchAllDataSerializer(serializers.ModelSerializer):
    
    Home = TeamOnlyNameSerializer(read_only=True)  # Aquí anidamos la info del equipo local
    Away = TeamOnlyNameSerializer(read_only=True)  # Aquí anidamos la info del equipo visitante
    Season = TournamentOnlyNameSerializer(read_only=True)  # Aquí anidamos la info de la temporada del torneo
    class Meta:
        model = FootballMatch
        fields = ['match_id', 'Home', 'Away', 'Score', 'Wk', 'Date', 'Attendance', 'Venue', 'Referee', 'Season']   
        
        
class FootballMatchWithIdsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FootballMatch
        fields = ['match_id', 'Season', 'Home', 'Away', 'Score', 'Date']
        
        
######## Leagues serializers ###########

class LeaguesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leagues
        fields = ['id', 'name']  # Aquí puedes agregar otros campos que necesites
        
        
        
######## General comparator match stats serializers ###########

class GeneralComparatorMatchStatsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GeneralComparatorMatchStats
        fields = ['estadistica_id', 'match_id', 'local_aerials_won', 'visitor_aerials_won', 'local_cards', 'visitor_cards',
                  'local_clearances', 'visitor_clearances', 'local_corners', 'visitor_corners',
                  'local_crosses', 'visitor_crosses', 'local_fouls', 'visitor_fouls',
                  'local_goal_kicks', 'visitor_goal_kicks', 'local_interceptions', 'visitor_interceptions',
                  'local_long_balls', 'visitor_long_balls', 'local_offsides', 'visitor_offsides',
                  'local_passing_accuracy', 'visitor_passing_accuracy', 'local_possession', 
                  'visitor_possession', 'local_saves', 'visitor_saves',
                  'local_shots_on_target', 'visitor_shots_on_target',
                  'local_tackles', 'visitor_tackles',
                  'local_throw_ins', 'visitor_throw_ins',
                  'local_touches', 'visitor_touches']
        
        

        
######### Basic Positions ###########
class BasicPositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BasicPositionCategory
        fields = ['category_id', 'category_name']
        
        
######## Specific Positions ###########

class SpecificPositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpecificsPositionsByCategory
        fields = ['specific_position_id', 'specific_position_name']
        
        
        
######## Game Mode ###########

class GameModeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameMode
        fields = ['game_mode_id', 'game_mode_name']
        
        
       
######## Player ###########       

class PlayerSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Player
            fields = ['player_id', 'player_name', 'nacionality']  # Aquí puedes agregar otros campos que necesites
        
    
        
######### Match Statistics ###########

class MatchStatisticsSerializer(serializers.ModelSerializer):
    
    
    match_id = FootballMatchSerializer(read_only=True)  # Aquí anidamos la info del partido
    player_id = PlayerSerializer(read_only=True)  # Aquí anidamos la info del jugador
    class Meta:
        model = MatchStatistics
        fields = ['estadistica_id', 'match_id', 'player_id', 'minutes', 'goals', 'assists']
        

######## Match Player Score ###########
class MatchPlayersScoreSerializer(serializers.ModelSerializer):
    
    
    specific_position_id = SpecificPositionSerializer(read_only=True)  # Aquí anidamos la info de la posición específica
    basic_position_id = BasicPositionSerializer(read_only=True)  # Aquí anidamos la info de la posición básica
    game_mode_id = GameModeSerializer(read_only=True)  # Aquí anidamos la info del modo de juego
    match_player_id = MatchStatisticsSerializer(read_only=True)  # Aquí anidamos la info del partido
    class Meta:
        model = MatchPlayerScore
        fields = ['match_player_score_id', 'match_player_id', 'specific_position_id', 'basic_position_id', 'score', 'game_mode_id']
        
        
        
        
class BasicStatSerializer(serializers.Serializer):
    local = serializers.IntegerField()
    visitor = serializers.IntegerField()
    type_stat_pct = serializers.BooleanField()

class BasicMatchStatsSerializer(serializers.Serializer):
    match_id = serializers.IntegerField()

    aerials_won = BasicStatSerializer()
    cards = BasicStatSerializer()
    clearances = BasicStatSerializer()
    corners = BasicStatSerializer()
    crosses = BasicStatSerializer()
    fouls = BasicStatSerializer()
    goal_kicks = BasicStatSerializer()
    interceptions = BasicStatSerializer()
    long_balls = BasicStatSerializer()
    offsides = BasicStatSerializer()
    passing_accuracy = BasicStatSerializer()
    possession = BasicStatSerializer()
    saves = BasicStatSerializer()
    shots_on_target = BasicStatSerializer()
    tackles = BasicStatSerializer()
    throw_ins = BasicStatSerializer()
    touches = BasicStatSerializer()

    class Meta:
        fields = (
            'match_id',
            'aerials_won',
            'cards',
            'clearances',
            'corners',
            'crosses',
            'fouls',
            'goal_kicks',
            'interceptions',
            'long_balls',
            'offsides',
            'passing_accuracy',
            'possession',
            'saves',
            'shots_on_target',
            'tackles',
            'throw_ins',
            'touches',
        )
        
        
        

        

