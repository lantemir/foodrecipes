import * as axios from "axios";


export const usersAPI = {
   
    getUsers(){
        // console.log("usersAPI")
        const config = {
            method: "GET",
            timeout: 10000,
            url: "/api/get_users",
            data: null,
        };     
        return axios(config).then(res => {
            return res.data.usersdb
        })
    },
    // login(){
    //     return axios.post("/login/", {"email": email, "password": password}).then(
    //         result => {
    //             console.log(result);
    //         }
    //     )
    // }
}

export const storyAPI = {

    getStories  (currentPage = 1, pageSize = 5){
        // const config = {
        //     method: "GET",
        //     timeout: 10000,
        //     url: `/api/get_stories?page=${currentPage}&count=${pageSize}`,
        //     data: null,
        // };
        // return axios(config).then(res => {
        //     return res.data.storiesdb
        // })
        return axios.get("/api/get_stories", {
            params: {
                currentPage: currentPage,
                pageSize: pageSize
            }
        }).then(res =>{
           
            return res.data
        })
        .catch( err => {
           return console.log(err.response.data)
        })
    },

    // getStories(currentPage = 1, pageSize = 5){
    //     const config = {
    //         method: "GET",
    //         timeout: 10000,
    //         url: `/api/get_stories?page=${currentPage}&count=${pageSize}`,
    //         data: null,
    //     };
    //     return axios(config).then(res => {
    //         return res.data.storiesdb
    //     })
    // },
    getStoryById(story_id){
        console.log("axios")
        const config ={
            method: "GET",
            url: `/api/story_by_id/${story_id}`,
            data:null,
        };
        return axios(config).then(res =>{
        
            return res.data.storyByIdDb
        })
    }
    
}

export const wordsAPI = {

    getWords(currentPage = 1, pageSize = 10){
        const config = {
            method: "GET",
            timeout: 10000,
            url: "/api/words/",
            data: null,
        };
        return axios(config).then(res => {
            return res.data.wordsdb
        })
    }
}

