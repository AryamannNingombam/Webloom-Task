import React,{lazy, useEffect,Suspense} from 'react';
import './App.css';
import { useRoutes } from 'react-router';
import Loader from './components/Loader'
import ScrollToTop from './components/ScrollToTop'


const AuthLogin = lazy(()=>import('./pages/auth/Auth'));


function App() {

  useEffect(()=>{
   
  },[])

  const homeRoutes=  [
    { path: '/auth', element:<AuthLogin/>  },
  ]
  
  

  const homeRouting = useRoutes(homeRoutes);


  return (
    <>
    <ScrollToTop />
    <Suspense fallback={<Loader />}>

    {homeRouting}
    </Suspense>
  </>
  );
}

export default App;
