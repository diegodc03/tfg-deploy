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



const router = createHashRouter([
  {
    path: '/',
    element: <MainLayout />,
    children: [
      { path: '', element: <HomePage /> },
      { path: 'filter-by-season-and-league', element: <FilterSeasonLeague /> },
      { path: 'filter-match/:leagueId', element: <FilterMatch /> },
      { path: 'show-match/:match_id', element: <ShowMatchStats /> },
      { path: 'match-stats-score/:match_id', element: <ShowScores /> },
    ],
  },
  {
    path: '/about',
    element: <h1>About</h1>,
  }
])


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
