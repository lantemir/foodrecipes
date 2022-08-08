import { Action } from "history";


const SET_CHAT = "SET_CHAT";

let initialState = {
    chat: []
}

const chatReducer = (state = initialState, action) => {
    switch(action.type){
        case SET_CHAT:
           return {
            ...state,
            chat: action.chat
        }
        default:
            return state;
    }
}


export const setChatAction = (chat) => ({type: SET_CHAT, chat }) 


export const setChatrequest = (dispatch, chat) => {
    dispatch(setChatAction(chat));
}


export default chatReducer;