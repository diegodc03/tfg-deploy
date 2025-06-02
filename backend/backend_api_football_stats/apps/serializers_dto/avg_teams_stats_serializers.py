from rest_framework import serializers

from ..models.avg_teams_stats import AvgTeamsStats
from ..models.avg_teams_by_basic_positions import AvgTeamsStatsByBasicPositions

from .serializers import TeamSerializer, LeaguesSerializer


class AvgTeamsStatsSerializer(serializers.ModelSerializer):
    
    team_id = TeamSerializer(read_only=True)
    league_id = LeaguesSerializer(read_only=True)
    
    class Meta:
        model = AvgTeamsStats
        fields = '__all__'
        
        
        
class AngAvgTeamsStatsByBasicPositionsSerializer(serializers.ModelSerializer):
    
    team_id = TeamSerializer(read_only=True)
    league_id = LeaguesSerializer(read_only=True)
    
    class Meta:
        model = AvgTeamsStatsByBasicPositions
        fields = '__all__'
      
    
    
    