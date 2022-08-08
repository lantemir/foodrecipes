import s from './users.module.css';
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { requestUsers } from "../../redux/login-reducer";
import axios from 'axios';
import {useNavigate} from "react-router-dom";

const Users = () => {
    const dispatch = useDispatch();

    const navigate = useNavigate();

    const [access, setAccess] = useState(false);

    const usersfromR = useSelector(state => {
        const { loginReducer } = state;
        return loginReducer
    })

    const testUsers = useSelector(state => {
        return state.loginReducer.users
    })

    const {
        email: email
    } = usersfromR

    // useEffect(()=>{
    //     console.log(`LoginStore: ${usersfromR}`);
    //     console.log(`email: ${email}`);
    //     console.log(`users: ${usersfromR.users}`);
    //     console.log("useEffect");

    // }, [usersfromR]);
    useEffect(() => {
        console.log("useEffect");
        requestUsers(dispatch);
    }, []);

    const [users, setUser] = useState([]);


    // тестовый запрос
    // function getUsers() {

    //     const config = {
    //         method: "GET",
    //         timeout: 10000,
    //         url: "/api/get_users",
    //         data: null,
    //     };
    //     axios(config).then(res => {
    //         const dataUsers = res.data.usersdb;
    //         // console.log(dataUsers)
    //         // console.log(typeof(dataUsers))
    //         setUser(dataUsers)
    //         // console.log(result.usersdb[0].username)
    //      }
    //     )
    // }

    function getUsers2() {
        console.log(users[0].id)
        console.log(email)
    }

    const getUsersRedux = () => {
        console.log("startgetUsersRedux");
        requestUsers(dispatch);
        console.log("endgetUsersRedux");
    }

    const gettingUsers = () => {
        console.log(testUsers)
    }

    const gettingUsersAutorized = () => {

        // let acccess_token = "aW9kaWJya2Fid2t4MmJ6OWJuOWVjejY2MzhhNGE2M3Q";

        const acccessToken = localStorage.getItem('token');
        

        axios.get("/api/get_users", {
            headers: {
                'Authorization': `Bearer ${acccessToken}`
            }
        }).then(response => {

            console.log('responseeeeeeee:'+ response.data)

            if(response.status === 404){
                localStorage.removeItem("token");
            }else{
                    console.log(response.data.usersdb)     
                if(response.data.usersdb.length > 0) {
                    setAccess(true)
                } else{
                    setAccess(false)
                }  
            }
            
        }).catch((error) => {
            localStorage.removeItem("token");
            setAccess(false);
            navigate("/");
        });
    }

    console.log("render")
    return (

        <div>
            <h1>Hello world</h1>
            <ul>
                {/* {testUsers.map(item => {
                    return (
                        <li key={item.id}>{item.username}</li>
                    )
                })} */}
            </ul>
            {/* <button onClick={getUsers}>Проверка</button> */}
            <button onClick={getUsersRedux}>getUsersRedux</button>
            <button onClick={gettingUsers}>gettingUsers</button>

            <button onClick={gettingUsersAutorized}>gettingUsersAutorized</button>

        </div>
    )
}





export default Users
