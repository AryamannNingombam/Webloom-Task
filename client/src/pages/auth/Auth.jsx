import React from 'react'
import './Auth.scss'
import GoogleLogin from 'react-google-login'
import { onGoogleLogin, testLogin } from '../../services/auth.service'

const Auth = () => {
  const onGoogleSignIn = (response) => {
      console.log(response);
      console.log(response.accessToken);
    onGoogleLogin(response.accessToken)
      .then((response) => response.data)
      .then((data) => {
        console.log(data)
      })
      .catch((err) => {
        console.log('ERROR')
        console.log(err)
      })
    
  }

  return (
    <div>
      <GoogleLogin
        clientId="506436750340-5c8l6adi9j1dm41j82dm8tprt8647b79.apps.googleusercontent.com"
        buttonText="LOGIN WITH GOOGLE"
        onSuccess={onGoogleSignIn}
        onFailure={onGoogleSignIn}
      />
    </div>
  )
}

export default Auth
