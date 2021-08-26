import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router'
import { domainInformation } from '../../services/api.service'
import './Results.scss'
import Loader from '../../components/Loader'
import { store } from '../../app/store'
import { logout } from '../../features/auth/auth.slice'


export const Results = () => {
  const [allSuggestions, setAllSuggestions] = useState([])
  const [text, setText] = useState(useParams().text)
  const [mainSearch, setMainSearch] = useState({})
  const [loading, setLoading] = useState(true)
  const navigate = useNavigate()

  useEffect(() => {
    const checkIfVerified = store.getState().auth
    if (!checkIfVerified.verified) {
      alert('Not verified!')
      store.dispatch(logout())
      navigate('/auth');
    }
    domainInformation(text)
      .then((response) => response.data)
      .then((data) => {
        console.log(data)
        const temp = data.all_suggestions
        for (let i = 0; i < temp.length; i++) {
          if (temp[i] === text) {
            temp.splice(i, 1)
            break
          }
        }
        setAllSuggestions(temp)
        setMainSearch(data.result)
        setLoading(false)
      })
      .catch((err) => {
        console.log('ERROR')
        console.log(err)
      })
  }, [text])

  const onURLClick = (newText) => {
    setText(newText)
    setLoading(true)
    navigate(`/results/${newText}`)
  }

  return (
    <div className="results-main-div">
      <h1>
        <span className="color-grey">You Searched for </span>
        {text}
      </h1>
      {loading ? (
        <Loader />
      ) : (
        <>
          {mainSearch.domain_name ? (
            <>
              <span className="content">Country : {mainSearch.country}</span>
              <span className="content">Org : {mainSearch.org}</span>
              <span className="content">
                Registrar : {mainSearch.registrar}
              </span>
              <span className="content">
                Creation date : {mainSearch.creation_date}
              </span>

              <span className="content">Emails : {mainSearch.emails}</span>
            </>
          ) : (
            'NO RESULTS FOUND'
          )}
          <h3>Suggestions</h3>
          <div className="suggestions">
            {allSuggestions.map((suggestion, index) => (
              <span
                onClick={(e) => {
                  onURLClick(suggestion)
                }}
                className="content"
                key={index}
              >
                {suggestion}
              </span>
            ))}
          </div>
        </>
      )}
    </div>
  )
}
