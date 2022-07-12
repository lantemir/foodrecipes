import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { requestUsers } from "../../redux/login-reducer";


const LoginForm = () => {
    const dispatch = useDispatch();

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

    console.log("render")
    return (

        <div>
            <h1>Hello world</h1>
            <ul>
                {testUsers.map(item => {
                    return (
                        <li key={item.id}>{item.username}</li>
                    )
                })}
            </ul>
            {/* <button onClick={getUsers}>Проверка</button> */}
            <button onClick={getUsersRedux}>getUsersRedux</button>
            <button onClick={gettingUsers}>gettingUsers</button>
        </div>
    )
}





export default LoginForm

