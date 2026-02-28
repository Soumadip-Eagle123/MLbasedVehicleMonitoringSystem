import axios from "axios";

const api = axios.create({
    baseURL: "https://mlbasedvehiclemonitoringsystem.onrender.com"
});

export default api;