

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from backend_api_football_stats.apps.models.football_match import FootballMatch
from backend_api_football_stats.apps.models.team import Team
from backend_api_football_stats.apps.models.tournament import Tournament

from ..models.general_comparator_match_stats import GeneralComparatorMatchStats  # o el modelo que uses
from ..serializers_dto.serializers import GeneralComparatorMatchStatsSerializer


class GeneralMatchStatsTestCase(APITestCase):

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
        # Crea un objeto de prueba
        self.match_stats = GeneralComparatorMatchStats.objects.create(
            match_id=2000,
            local_possession=55.0,
            visitor_possession=45.0,
            # agrega aquí los demás campos obligatorios
        )

    def test_get_general_stats_success(self):
        url = "/api/get-basic-stats-of-match-comparator/?match_id=2000"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['match_id'], 2000)

    def test_get_general_stats_invalid_id(self):
        url = "/api/get-basic-stats-of-match-comparator/?match_id=no_es_numero"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        
    def test_get_general_stats_no_match_id(self):
        url = "/api/get-basic-stats-of-match-comparator/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
    
    
    def test_get_general_stats_not_found_match_id(self):
        url = "/api/get-basic-stats-of-match-comparator/?match_id=9999"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
