import React, { useEffect } from 'react'
import { useNavigate } from 'react-router'
import { checkIfSignedIn } from '../../services/auth.service'

const Home = () => {
    const navigate = useNavigate();



    useEffect(()=>{
        if (!checkIfSignedIn()){
            alert("Not signed in!");
            navigate('/auth');
        }
    },[])


    return (
        <div>
            HOME
        </div>
    )
}

export default Home;