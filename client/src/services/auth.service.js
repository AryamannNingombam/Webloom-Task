import axios from 'axios';
import {
    BACKEND_API
} from '../constants';
import {
    store
} from '../app/store';



export const CheckVerified = (email,token) => {

    console.log(token)
    if (!token) {
        throw new Error("Not authorized!");
    }
    console.log(token)
    return axios.get(`${BACKEND_API}/api/auth/check-user-verified/${email}`, {
        headers: {
            "Authorization": `JWT ${token}`
        }
    })
}


export const SignIn = (body) => {
    console.log(body)
    return axios.post(`${BACKEND_API}/api/auth/token/obtain/`, body, {
        headers: {
            'content-type': 'application/json'
        }
    })
}