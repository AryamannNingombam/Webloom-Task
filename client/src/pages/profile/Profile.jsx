import React, { useState } from 'react'
import { useEffect } from 'react'
import { GetUserHistory, GetUserInformation } from '../../services/auth.service'
import Loader from '../../components/Loader'
import './Profile.scss'
const Profile = () => {
  const [loading, setLoading] = useState(true)
  const [userInformation, setUserInformation] = useState({})
  const [history, setHistory] = useState([])

  useEffect(() => {
    GetUserInformation()
      .then((response) => response.data)
      .then((data) => {
        setUserInformation(data.user_information)
        console.log(data.user_information)
        GetUserHistory()
          .then((response) => response.data)
          .then((data) => {
            console.log(data)
            const tempArray = data.history.searches.split(',')
            console.log(tempArray)
            setHistory(tempArray.slice(0, tempArray.length - 1))
            setLoading(false)
          })
          .catch((err) => {
            console.log('ERROR')
            console.log(err)
          })
      })
      .catch((err) => {
        console.log('ERROR')
        console.log(err)
      })
  }, [])

  return (
    <div className="profile-main-div">
      {loading ? (
        <Loader />
      ) : (
        <>
          <div className="profile-section">
            <span className="text">Email : {userInformation.email}</span>
            <span className="text">Username : {userInformation.username}</span>
            <span className="text">
              First Name : {userInformation.first_name}
            </span>
            <span className="text">
              Last Name : {userInformation.last_name}
            </span>
          </div>
          <div className="history-section">
            <h1>History</h1>
            {history.map((his, index) => (
              <span key={index} className="history">
                {his}
              </span>
            ))}
          </div>
        </>
      )}
    </div>
  )
}

export default Profile
