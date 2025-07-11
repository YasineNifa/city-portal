import axios from "axios";

const API_BASE_URL = "http://localhost:8002/api"; // TODO use process.env.REACT_APP_API_URL

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
