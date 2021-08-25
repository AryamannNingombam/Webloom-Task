import React,{lazy, useEffect,Suspense} from 'react';
import './App.css';
import { useRoutes } from 'react-router';
import Loader from './components/Loader'
import ScrollToTop from './components/ScrollToTop'
import { checkIfSignedIn } from './services/auth.service';
import { Results } from './pages/results/Results';



const AuthLogin = lazy(()=>import('./pages/auth/Auth'));
const Home = lazy(()=>import('./pages/home/Home'));

function App() {

  useEffect(()=>{
 
  },[])

  const homeRoutes=  [
    { path: '/auth', element:<AuthLogin/>  },

    
  ]
  const authRoutes = [
    {path : '/home',element : <Home/>},
    {path : "/results/:text",element : <Results/>}

  ]  
  

  const homeRouting = useRoutes(homeRoutes);
  const authRouting  = useRoutes(authRoutes);

  return (
    <>
    <ScrollToTop />
    <Suspense fallback={<Loader />}>

    {checkIfSignedIn() ? authRouting : homeRouting}
    </Suspense>
  </>
  );
}

export default App;
