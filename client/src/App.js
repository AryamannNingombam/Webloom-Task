import React,{lazy, useEffect,Suspense} from 'react';
import './App.css';
import { useRoutes } from 'react-router';
import Loader from './components/Loader'
import ScrollToTop from './components/ScrollToTop'
import { domainInformation } from './services/api.service';
import { checkIfSignedIn } from './services/auth.service';



const AuthLogin = lazy(()=>import('./pages/auth/Auth'));
const Home = lazy(()=>import('./pages/home/Home'));

function App() {

  useEffect(()=>{
    domainInformation('kryptocards')
    .then(response=>response.data)
    .then(data=>{
      console.log(data);
    })
    .catch(err=>{
      console.log("ERROR");
      console.log(err);
    })
  },[])

  const homeRoutes=  [
    { path: '/auth', element:<AuthLogin/>  },
  ]
  const authRoutes = [
    {path : '/home',element : <Home/>}
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
