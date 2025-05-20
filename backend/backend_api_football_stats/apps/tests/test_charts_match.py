from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FootballMatch, Player, MatchStatistics, StatsDefenseSummary

class GetStatsToChartViewTests(APITestCase):
    def setUp(self):
        self.match = FootballMatch.objects.create(match_id=1, team_a="Team A", team_b="Team B")
        self.player = Player.objects.create(player_id=1, player_name="Jugador 1")
        self.stats = MatchStatistics.objects.create(match_id=self.match, player_id=self.player, goals=1, assists=0)

        self.defense_stats = StatsDefenseSummary.objects.create(
            stat_id=self.stats,
            player_id=self.player,
            tackles=5,
            blocks=2
        )

    def test_get_stats_chart_default(self):
        url = reverse('get-stats-chart')  # o usa el path directo si no lo nombras en urls.py
        response = self.client.get(url, {'match_id': self.match.match_id})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('stat', response.data[0])
        self.assertIn('values', response.data[0])
        self.assertEqual(response.data[0]['values'][0]['player_name'], 'Jugador 1')
