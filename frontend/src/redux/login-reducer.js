import { usersAPI } from "../components/api/api";

const SET_USERS = 'SET_USERS';


let initialState = {
    users: [],
    userId: null,
    email: null,
    login: null,
    isAuth: false,    
};

const loginReducer = (state = initialState, action) => {
    switch(action.type){
        case SET_USERS:
            return{
                ...state,
                users: action.users
            }
        default: 
            return state;
    }
}


export const SetUsersAction = (users) => ({type: SET_USERS, users})

// export const requestUsers = () => {
//     console.log("requestUsers")    
//         return 
//         const data =  usersAPI.getUsers();
//         console.log("data")

//         dispatch(SetUsersAction(data));
// }


export const requestUsers = async (dispatch) => {
         
       
        const data = await usersAPI.getUsers();
        console.log("data")
        console.log(data)
        dispatch(SetUsersAction(data));
      
    
}


//рабочий код
// export const requestUsers = async (dispatch) => {
//     console.log("requestUsers")
//     const data = await usersAPI.getUsers();
//     console.log("data")
//     console.log(data)
//     dispatch(SetUsersAction(data));
  

// }

export default loginReducer