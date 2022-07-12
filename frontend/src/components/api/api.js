import * as axios from "axios";

export const usersAPI = {
   
    getUsers(){
        console.log("usersAPI")
        const config = {
            method: "GET",
            timeout: 10000,
            url: "/api/get_users",
            data: null,
        };     
        return axios(config).then(res => {
            return res.data.usersdb
        })
    }
}

