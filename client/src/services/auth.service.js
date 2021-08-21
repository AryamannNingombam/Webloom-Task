import axios from 'axios';
import {
    BACKEND_API
} from '../constants';


export const onGoogleLogin = async (accessToken) => {

    return axios.post(`${BACKEND_API}/api/auth/google/`, {
        access_token: accessToken,
        code:""
    }, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })

}

export const testLogin = async () => {
    const result = await axios.get(`${BACKEND_API}/api/auth/test`);
    console.log(result.data);
}