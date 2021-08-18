import axios from 'axios';
import {
    BACKEND_API
} from '../constants';



export const testAPI = () => {
    return axios.post(`${BACKEND_API}/api/test/`, {
        url: "kryptocards.tech"
    })
}