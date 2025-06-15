import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createHashRouter, RouterProvider } from 'react-router-dom'
import HomePage from './pages/HomePage.tsx'
import MainLayout from './layout/MainLayout.tsx'
import FilterSeasonLeague from './pages/FilterSeasonLeague.tsx'
import FilterMatch from './pages/FilterMatch.tsx'
import ShowMatchStats from './pages/ShowMatchStats.tsx'
import ShowScores from './pages/ShowScores.tsx'
import ShowStatsOfPlayersTables from './pages/stats/ShowStatsOfPlayersTables.tsx'

import { ShowStatsChartFromMatch } from './pages/stats/ShowStatsFromMatch.tsx'
import ShowStatsFromMatch from './pages/stats/ShowStatsChartsFromMatch.tsx'
import About from './pages/About.tsx'
import TfgDocs from './pages/TfgDocs.tsx'
import ShowStatsComparisonFromLeague from './pages/stats/ShowStatsComparisonFromLeague.tsx'
import ShowStatsFromTeams from './pages/stats/ShowStatsFromTeams.tsx'

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
