import React,{useState} from 'react'
import { Button, FormControl } from 'react-bootstrap'
import { SignInUser } from '../../features/auth/auth.slice'
import { store } from '../../app/store'
import { useNavigate } from 'react-router'
import './SignIn.scss';


const SignIn = ({callback}) => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()
  const onSignIn = (e) => {
    e.preventDefault()
    store
      .dispatch(SignInUser({ username, password }))
      .then((response) => {
        console.log(response)
        if (response.payload) {
          alert('Signed in!')
          navigate('/home')
        } else {
          alert('Wrong!')
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const onSwitch = (e)=>{
    e.preventDefault();
    callback('signup')

  }

  return (
    <div className="auth-main-div">
      <FormControl
        className="form-control-styling"
        placeholder="Username"
        onChange={(e) => {
          setUsername(e.target.value)
        }}
      />
      <FormControl
        type="password"
        className="form-control-styling"
        placeholder="Password"
        onChange={(e) => {
          setPassword(e.target.value)
        }}
      />
      <Button className="sign-in-button" onClick={onSignIn}>
        Sign-In
      </Button>
      <Button className="sign-in-button" onClick={onSwitch}>
        Sign-Up
      </Button>
    </div>
  )
}

export default SignIn
