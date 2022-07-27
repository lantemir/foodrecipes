import React, { useEffect, useState } from "react";
import s from './story.module.css';
import {useParams} from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";
import {requestStoryById} from "../../redux/story-reducer";


let Storyinfo  = () => {
    const {id} = (useParams())
    const dispatch = useDispatch();
   
    const storyInfo = useSelector(state => {
        return state.storyReducer.storyById
    })

const showState = () => {
    console.log(storyInfo)
}


    useEffect(() => {
        console.log("useEffectStoryinfo")
        requestStoryById(dispatch, id);
        
    },[id])

    return(
        <div>
            <h1>{storyInfo.title}</h1>

            <p>{storyInfo.description}</p>

            <button onClick={showState}>test</button>
          
        </div>
    )
}

export default Storyinfo;