import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { requestStories, requestWords } from "../../redux/story-reducer";
import s from './story.module.css';
import {Link} from "react-router-dom"
import Paginator from "../common/paginator/paginator";
import Loader from "../common/loader/loader";



export default function Story() {
    const dispatch = useDispatch();

    const stories = useSelector(state => {
        return state.storyReducer.stories
    })

    const forPagination = useSelector(state => state.storyReducer);
    const {
        pageSize:pageSize,
        totalStoriesCount,
        currentPage,
        loading
    } = forPagination

    useEffect(() => {
        console.log("useEffectStory")
        requestStories(dispatch, currentPage, pageSize );
    }, []);

    //    const words = useSelector(state => {
    //     return state.storyReducer.words
    // })

    // useEffect(() => {
    //     console.log("useEffect")
    //     requestWords(dispatch);
    // },[]);

    const onPageChanged = (pageNumber) => {
        requestStories( dispatch ,pageNumber,pageSize)
    }

    return (
        <div className={s.wrapper}>
            <div><h1>Story Page</h1></div>

            <Paginator currentPage={currentPage} totalStoriesCount={totalStoriesCount} pageSize={pageSize} onPageChanged = {onPageChanged}  />


        {loading && 
            <div className="d-flex justify-content-center">
                <Loader/>
            </div>
        }
        
           
            

            <div className={s.storyBlocks}>
                {stories.map(item => {
                    return (
                        <div key={item.id} className={s.storyBlock}>
                            <h4>{item.title}</h4>
                            <img src={`${item.image}`}/>
                            <p>картинка</p>                          
                            <Link to={`/story/${item.id}`} className="nav-link active" aria-current="page" ><button>подробнее</button></Link>
                            
                        </div>
                    )
                })}
            </div>            
        </div>
    )
}






