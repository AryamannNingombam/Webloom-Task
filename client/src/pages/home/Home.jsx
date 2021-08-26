import React, { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router'
import { checkIfSignedIn } from '../../services/auth.service'
import { Button, FormControl } from 'react-bootstrap'
import './Home.scss'
import { domainInformation } from '../../services/api.service'

const Home = () => {
  const navigate = useNavigate()
  const divRef = useRef(null)
  const [inputText, setInputText] = useState('')

  useEffect(() => {
    if (!checkIfSignedIn()) {
      alert('Not signed in!')
      navigate('/auth')
    }
  }, [])

  const onSearchDomainDisplay = (e) => {
    e.preventDefault()
    divRef.current.style.opacity = '1'
  }

  const onSearchButtonClick = (e) => {
    e.preventDefault()
    navigate(`/results/${inputText}`)
  }

  const onProfileClick = (e)=>{
    e.preventDefault();
    navigate('/profile')
  }
  return (
    <div className="home-main-div">
      <Button onClick={onProfileClick} className="button">Profile</Button>
      <Button className="button" onClick={onSearchDomainDisplay}>
        Search Domain
      </Button>
      <div ref={divRef} className="display-item">
        <FormControl
          placeholder="Enter domain"
          onChange={(e) => {
            setInputText(e.target.value)
          }}
        />
        <Button onClick={onSearchButtonClick}>Search</Button>
      </div>
    </div>
  )
}

export default Home
