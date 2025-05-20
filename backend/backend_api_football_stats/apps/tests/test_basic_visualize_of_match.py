



from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from backend_api_football_stats.apps.models.team import Team
from backend_api_football_stats.apps.models.tournament import Tournament

from ..models.football_match import FootballMatch  # o el modelo que uses
from ..serializers_dto.serializers import GeneralComparatorMatchStatsSerializer






class TestBasicVisualizeOfMatch(APITestCase):
    
    
    def setUp(self):
        
        self.team_home = Team.objects.create(team_name="Cádiz")
        self.team_away = Team.objects.create(team_name="Levante")
        self.tournament = Tournament.objects.create(nombre_liga="La Liga")

        self.match = FootballMatch.objects.create(
            match_id=2000,
            Home=self.team_home,
            Away=self.team_away,
            Season=self.tournament,
            # otros campos si los hay
        )
    
    
    def test_get_basic_visualize_of_match_success(self):
        # Crea un objeto de prueba
        
        url = "/api/get-basic-visualize-of-match/?match_id=2000"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['match_id'], 2000)
        self.assertEqual(response.data['local_possession'], 55.0)
        
    
    def test_get_basic_visualize_of_match_invalid_id(self):
        url = "/api/get-basic-visualize-of-match/?match_id=no_es_numero"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        
        
    def test_get_basic_visualize_of_match_no_match_id(self):
        
        url = "/api/get-basic-visualize-of-match/"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        
        
    def test_get_basic_visualize_of_match_not_found_match_id(self):
        url = "/api/get-basic-visualize-of-match/?match_id=9999"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    