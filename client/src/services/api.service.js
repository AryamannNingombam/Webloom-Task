import axios from 'axios';
import {
    BACKEND_API
} from '../constants';



export const testAPI = () => {
    return axios.get(`${BACKEND_API}/api/test/`)
}