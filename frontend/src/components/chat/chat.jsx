import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import s from './chat.module.css';
import { setChatrequest } from "../../redux/chat-reducer";
import { useDispatch, useSelector } from "react-redux";

// const ws = new WebSocket(`ws://${window.location.host}/ws/socket-server/`); //chatSocket

// ws.onmessage = function(e){
//     let data = JSON.parse(e.data)
//     console.log('Data: ', data)
// }

// export type ChangeMessageType = {
//     message: string,
//     photo: string,
//     userId: number,
//     userName: string
// }


const ChatPage = () => {

    return(
        <div>
            <h1>Чат общий</h1>
            <div>
                <Chat/>
            </div>
        </div>
    )
}


const Chat = () => {

 
    return(
        <div>
            <Messages/>
            <AddmessageForm/>
        </div>
    )
}


const Messages = () => { 

    

  
    // const messages = [1,2,3,4];
    const chatStore = useSelector(state => {
        return state.chatReducer.chat
    })


    // {chatStore.map(item => {
    //     return (
    //         <h2>{item.message}</h2>
    //     )
    // })}




    return (
        <div style={{ height: '400px', overflowY: 'auto', marginLeft: '30px' }}>
            <ul>
                {chatStore.map(item => {
                    return (
                        <li key={item.id}>
                            <Message message={item.message}  user={item.username} photo={item.photo} />
                        </li>
                        
                    )
                })}
            </ul>
        </div>
    )
}

const Message = (props) => {
    // const message = {
    //     photo: 'https://via.placeholder.com/30',
    //     userName: 'Temir',
    //     message: "hello my friends"
    // }

    

    return (

        <div className={s.chatRow}>
            <img src={props.photo} /> <b>{props.user}</b>
            <br />
            {props.message}
            <hr />
            {props.id}
        </div>



    )
}



const AddmessageForm = () => {

    

    const [messagesChat, setmessagesChat] = useState([])

    const [message, setmessage] = useState('')

    const ws = new WebSocket(`ws://127.0.0.1:8000/ws/socket-server/`); //chatSocket  http://127.0.0.1:8000/
    const dispatch = useDispatch();
    

    useEffect(() => {
      console.log("useEffect AddmessageForm")
      ws.onmessage = function (e) {
        let data = JSON.parse(e.data)
                 console.log('Data from ws : ', data.message)
            setChatrequest(dispatch, data.message )
      }
     
    }, [messagesChat]);
   
   
    const chatStore = useSelector(state => {
        return state.chatReducer.chat
    })



    const sendMessage = (e) => {
        e.preventDefault();
        // console.log("sendMessage")
        // console.log(message)
        if (message.length >= 1) {
            const acccessToken = localStorage.getItem('token');

            ws.send(JSON.stringify({
                'message': message,
                'token': acccessToken
            }))
            setmessage("");

            ws.onmessage = function (e) {
                let data = JSON.parse(e.data)
                console.log('Data from ws : ', data)

                if (data.type === 'chat') {
                    // setmessagesChat(data.message)
                    // setChatrequest(dispatch, data )
                    console.log('data.type === chat')
                }

               

            }
        }

        
    }


        return (
            <div>
                
               

   

                {/* <h2>{messagesChat}</h2> */}
                <form onSubmit={sendMessage}>
                    <div>
                        <textarea onChange={(e) => setmessage(e.target.value)} value={message}></textarea>
                    </div>
                    <div>
                        <button>Send</button>
                    </div>
                </form>


            </div>
        )
}


export default ChatPage