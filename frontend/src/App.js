import React from 'react';
import { Routes, Route, Link  } from 'react-router-dom';

// import {
//   BrowserRouter,
//   Link,
//   Outlet,
//   useRoutes
// } from 'react-router-dom';


import logo from './logo.svg';
// import './App.css';
import Navbar from './components/navbar/navbar';
import Home from './components/home/home';
import LoginForm from './components/login/login';

import Story from './components/story/story';
import Storyinfo from './components/story/storyinfo';
import Users from './components/users/users';
import ChatPage from './components/chat/chat';
import "./css/my.css";
import "./css/bootstrap/bootstrap.css";


export default function App() {


  return(
    <Routes>
      <Route path="/" element = {<Navbar/>}>
        <Route index element= {<Home/>} />
        <Route path='story' element ={<Story/>} />
        <Route path='story/:id' element ={<Storyinfo/>} />
        <Route path='login' element ={<LoginForm/>} />
        <Route path='users' element = {<Users/> } />
        <Route path='chat' element= {<ChatPage/> } />
      </Route>
    </Routes>
  )
}








// export default function App() {

//   let element = useRoutes([    
//     { path: '/', 
//       element: <Navbar />, 
//       children: [
//         { index : true, element: <Home/>},
        
//         {
//           path: "/story",
//           element: <Stories/>,
//           children: [
//             {index: true, element: <Story /> },                       
//             {path: "/story/:id", element: <Storyinfo/>}
//           ]
//         }, 

//         {
//           path: "/login",
//           element: <LoginForm/>,          
//         }, 

//       ],    
//     },
//   ]);

//   return(
//     <div>      
//       {element};
//     </div>
    
//   ) 
// }


// function App() {
//   return (
//     <BrowserRouter>
//       <Navbar />
//       <Routes>
//         <Route path='/' element={<Home />}></Route>
        
//         <Route path='/story' element={<Story />}>
//           <Route path='/story/:id' element={<Storyinfo/>} />
//         </Route>
//         {/* <Route path='/storyinfo' element={<Story />}></Route> */}
        
//         <Route path='/login' element={<LoginForm />}></Route>
//       </Routes>

      
//     </BrowserRouter>

//   );
// }

// export default App;
