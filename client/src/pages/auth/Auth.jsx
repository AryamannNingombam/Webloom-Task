import React, { useState } from 'react'
import './Auth.scss'
import SignIn from '../../components/auth/SignIn';
import SignUp from '../../components/auth/SignUp';



const Auth = () => {
  const [mode,setMode] = useState('signin');




  return (
    <div className="auth-main-div">
      {mode === 'signin' ? <SignIn
      callback={setMode}
      /> :<SignUp
      callback={setMode}
      /> }
 
    </div>
  )
}
export default Auth
