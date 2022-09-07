import axios from "axios";


// BASE URL from the environment variables.
const HOST_NAME = "localhost"
const BASE_URL = "http://" + HOST_NAME + "/api/v1"



const axiosClient = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    timeout: 2000,
    timeoutErrorMessage: "Request Timed Out"
});


export default axiosClient