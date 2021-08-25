import React, { useState } from 'react'
import { signUpUser } from '../../services/auth.service'
import './SignUp.scss'
import { FormControl, Button } from 'react-bootstrap'

const SignUp = ({callback}) => {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')

  const onSignUpButtonClick = (e) => {
    const formData =new FormData();
    formData.append('username',username);
    formData.append('email',email);
    formData.append('password',password);
    formData.append('firstName',firstName);
    formData.append("lastName",lastName);


    e.preventDefault()
    signUpUser(formData)
      .then((response) => response.data)
      .then((data) => {
        alert('Signed up!')
        console.log(data)
      })
      .catch((err) => {
        console.log('ERROR')
        console.log(err)
      })
  }

  const onSwitch = (e)=>{
    e.preventDefault();
    callback('signin');
  }

  return (
    <div className="auth-main-div">
      <FormControl
        className="form-control"
        onChange={(e) => {
          setEmail(e.target.value)
        }}
        placeholder="Email"
      />
      <FormControl
        className="form-control"
        onChange={(e) => {
          setUsername(e.target.value)
        }}
        placeholder="username"
      />
      <FormControl
        className="form-control"
        onChange={(e) => {
          setPassword(e.target.value)
        }}
        placeholder="password"
        type="password"
      />
      <FormControl
        className="form-control"
        onChange={(e) => {
          setFirstName(e.target.value)
        }}
        placeholder="first name"
      />
      <FormControl
        className="form-control"
        onChange={(e) => {
          setLastName(e.target.value)
        }}
        placeholder="last name"
      />
      <Button onClick={onSignUpButtonClick}>Sign up</Button>
    </div>
  )
}

export default SignUp
