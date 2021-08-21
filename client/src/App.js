import React,{lazy, useEffect,Suspense} from 'react';
import './App.css';
import { testAPI } from './services/api.service';
import { useRoutes } from 'react-router';
import Loader from './components/Loader'
import ScrollToTop from './components/ScrollToTop'


const AuthLogin = lazy(()=>import('./pages/auth/Auth'));


function App() {

  useEffect(()=>{
    testAPI()
    .then(response=>response.data)
    .then(response=>{
      console.log(response);
    })
    .catch(err=>{
      console.log(err);
    })
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
