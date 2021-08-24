import axios from 'axios';
import { store } from '../app/store';
import {
    BACKEND_API
} from '../constants';


export const domainInformation = (text) => {
    const token = store.getState().auth.token;
    console.log(token);
    return axios.get(`${BACKEND_API}/api/domain/filter-query/${text}`,{
        headers : {
            "Authorization": `JWT ${token}`
        }
    })
}