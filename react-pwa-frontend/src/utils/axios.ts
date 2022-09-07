import axios from "axios";

const axiosClient = axios.create();

// BASE URL from the environment variables.

const BASE_URL_PREFIX = "http://";
const BASE_URL_SUFFIX = "/api/v1/";
const BASE_URL_HOST = "localhost";
const BASE_URL = BASE_URL_PREFIX + BASE_URL_HOST + BASE_URL_SUFFIX;

// base url
axiosClient.defaults.baseURL = BASE_URL;
// time out
axiosClient.defaults.timeout = 2000;
