import {applyMiddleware, combineReducers, createStore} from "redux";
import loginReducer from "./login-reducer";
import  thunkMiddleware from 'redux-thunk'; // обязательно для санок


let reducers = combineReducers({
    loginReducer: loginReducer
})

const store = createStore(reducers, applyMiddleware(thunkMiddleware)); 
//applyMiddleware для санок не забыть скачать npm i redux-thunk

window.__store__ = store

export default store




