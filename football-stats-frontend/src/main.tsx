import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createHashRouter, RouterProvider } from 'react-router-dom'
import HomePage from './pages/NavContentAndPrincipalPage/HomePage.tsx'
import MainLayout from './layout/MainLayout.tsx'
import FilterSeasonLeague from './pages/FiltersAndSelection/FilterSeasonLeague.tsx'
import FilterMatch from './pages/FiltersAndSelection/FilterMatch.tsx'
import ShowMatchStats from './pages/FiltersAndSelection/ShowMatchStats.tsx'
import ShowScores from './pages/MatchStatistics/ShowScores.tsx'
import ShowStatsOfPlayersTables from './pages/MatchStatistics/ShowStatsOfPlayersTables.tsx'

import {ShowStatsChartFromMatch}  from './pages/MatchStatistics/ShowStatsUnitaryChartFromMatch.tsx'
import ShowStatsFromMatch from './pages/MatchStatistics/ShowStatsChartsFromMatch.tsx'
import About from './pages/NavContentAndPrincipalPage/About.tsx'
import TfgDocs from './pages/AcademicResource/TfgDocs.tsx'
import ShowStatsComparisonFromLeague from './pages/ComparatorTeamsAndLeagues/ShowStatsComparisonFromLeague.tsx'
import ShowStatsFromTeams from './pages/ComparatorTeamsAndLeagues/ShowStatsFromTeams.tsx'
import HelpingPage from './pages/NavContentAndPrincipalPage/HelpingPage.tsx'

const router = createHashRouter([
  {
    path: '/',
    element: <MainLayout />,
    children: [
      { path: '', element: <HomePage /> },
      { path: 'filter-by-season-and-league', element: <FilterSeasonLeague /> },
      { path: 'filter-match/:leagueId', element: <FilterMatch /> },
      { path: 'show-match/:match_id', element: <ShowMatchStats /> },
      { path: 'scores-of-players-match/:match_id', element: <ShowScores /> },
      { path: 'match-players-stats/:match_id', element: <ShowStatsOfPlayersTables /> },
      { path: 'stats-players-match/:match_id', element: <ShowStatsFromMatch /> },
      { path: 'stats-chart-of-match/:match_id', element: <ShowStatsChartFromMatch /> },
      { path: 'contacto', element: <About /> },
      { path: 'documentacion-tfg', element: <TfgDocs /> },
      { path: 'leagues-comparison', element: <ShowStatsComparisonFromLeague />},
      { path: 'show-stats-comparison-from-teams/:league_id', element: <ShowStatsFromTeams /> },
      { path: 'helping-page', element: <HelpingPage /> },
    ],
  },
  {
    path: '/about1',
    element: <h1>About</h1>,
  }
])


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
