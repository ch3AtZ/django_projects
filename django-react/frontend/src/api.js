import axios from 'axios';
import { ACCESS_TOKEN } from "./constants";

const api =  axios.create({
    baseURL: import.meta.env.VITE_API_URL
})


api.interceptors.request.use(
    (config) =>{
        const token = localStorage.getItem(ACCESS_TOKEN)  // this if for getting the access token from the local storage 
        if (token){
            config.headers.Authorization = `Bearer $(token)`
        }
    },
    (error) =>{
        return Promise.reject(error)
    }
)

export default api;