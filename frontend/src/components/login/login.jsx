import axios from "axios";
import React, { useState } from "react";


const Login = () => {

    const [userLogin, setUserLogin] = useState("");
    const [password, setPassword] = useState("");

    const formData = (form) => {
        form.preventDefault();

        const formData  = new FormData();
        formData.append("userLogin", userLogin);
        formData.append("password", password);

        axios.post("/login/", formData).then( result => {
            console.log(result)
        })

    }


    return (
        <main className="custom_main_1">
            <div className="container col-xl-10 col-xxl-8 px-4 py-5">
                <div className="row align-items-center g-lg-5 py-5">
                    <div className="col-lg-7 text-center text-lg-start">
                        <h1 className="display-4 fw-bold lh-1 mb-3">
                            Вход
                        </h1>
                        <p className="col-lg-10 fs-4">
                           
                        </p>
                    </div>
                    <div className="col-md-10 mx-auto col-lg-5">
                        <form className="p-4 p-md-5 border rounded-3 bg-light" onSubmit={formData}>
                            <div className="form-floating mb-3">
                                <input
                                    type="text"
                                    className="form-control"
                                    id="floatingInput"
                                    placeholder="name"
                                    min="8"
                                    max="16"
                                    required
                                    value={userLogin}
                                    onChange={(event) => setUserLogin(event.target.value)}
                                />
                                <label htmlFor="floatingInput">Имя пользователя</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input
                                    type="password"
                                    className="form-control"
                                    id="floatingPassword"
                                    placeholder="Password"
                                    min="8"
                                    max="16"
                                    required
                                    value={password}
                                    onChange={(event) => setPassword(event.target.value)}
                                />
                                <label htmlFor="floatingPassword">Введите пароль от аккаунта</label>
                            </div>
                            <label>показать пароль</label>
                            {/* <input onClick={() => TogglePasswordVisibility("floatingPassword")} type="checkbox" id="vehicle1" name="vehicle1" value="Bike" placeholder="показать пароль"></input> */}
                            <button className="w-100 btn btn-lg btn-primary" type="submit">
                                Войти
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
    )
}

export default Login















// import React, { useEffect, useState } from "react";
// import { useDispatch, useSelector } from 'react-redux';
// import { requestUsers } from "../../redux/login-reducer";


// const LoginForm = () => {
//     const dispatch = useDispatch();

//     const usersfromR = useSelector(state => {
//         const { loginReducer } = state;
//         return loginReducer
//     })

//     const testUsers = useSelector(state => {
//         return state.loginReducer.users
//     })

//     const {
//         email: email
//     } = usersfromR

//     // useEffect(()=>{
//     //     console.log(`LoginStore: ${usersfromR}`);
//     //     console.log(`email: ${email}`);
//     //     console.log(`users: ${usersfromR.users}`);
//     //     console.log("useEffect");

//     // }, [usersfromR]);
//     useEffect(() => {
//         console.log("useEffect");
//         requestUsers(dispatch);
//     }, []);

//     const [users, setUser] = useState([]);


//     // тестовый запрос
//     // function getUsers() {

//     //     const config = {
//     //         method: "GET",
//     //         timeout: 10000,
//     //         url: "/api/get_users",
//     //         data: null,
//     //     };
//     //     axios(config).then(res => {
//     //         const dataUsers = res.data.usersdb;
//     //         // console.log(dataUsers)
//     //         // console.log(typeof(dataUsers))
//     //         setUser(dataUsers)
//     //         // console.log(result.usersdb[0].username)
//     //      }
//     //     )
//     // }

//     function getUsers2() {
//         console.log(users[0].id)
//         console.log(email)
//     }

//     const getUsersRedux = () => {
//         console.log("startgetUsersRedux");
//         requestUsers(dispatch);
//         console.log("endgetUsersRedux");
//     }

//     const gettingUsers = () => {
//         console.log(testUsers)
//     }

//     console.log("render")
//     return (

//         <div>
//             <h1>Hello world</h1>
//             <ul>
//                 {testUsers.map(item => {
//                     return (
//                         <li key={item.id}>{item.username}</li>
//                     )
//                 })}
//             </ul>
//             {/* <button onClick={getUsers}>Проверка</button> */}
//             <button onClick={getUsersRedux}>getUsersRedux</button>
//             <button onClick={gettingUsers}>gettingUsers</button>
//         </div>
//     )
// }





// export default LoginForm

