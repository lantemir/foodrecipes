import { storyAPI, wordsAPI } from "../components/api/api";

const SET_STORIES = 'SET_STORIES';
const SET_WORDS = 'SET_WORDS';
const SET_STORY = 'SET_STORY';
const SET_CURRENT_PAGE_STORY = 'SET_CURRENT_PAGE_STORY';
const SET_TOTAL_STORIES_COUNT = 'SET_TOTAL_STORIES_COUNT';
const SET_LOADING_STORIES = "SET_LOADING_STORIES";


let initialState = {    
    stories: [],
    pageSize: 10,
    totalStoriesCount: 0,
    currentPage: 1,
    words: [],
    storyById: {},
    loading: false

};

const storyReducer = (state = initialState, action) => {
    switch(action.type){
        case SET_STORIES:
            return{
                ...state,
                stories: action.stories
            }
        case SET_WORDS:
            return{
                ...state,
                stories: action.words
            }
        case SET_STORY:
            return{
                ...state,
                storyById: action.storybyid
            }
        case SET_CURRENT_PAGE_STORY:
            return{
                ...state, currentPage: action.currentPage
            }
        case SET_TOTAL_STORIES_COUNT:
            return{
                ...state, totalStoriesCount: action.totalStoriesCount
            }
        case SET_LOADING_STORIES:
            return{
                ...state, loading: action.loading
            }
        default: 
            return state;
    }
}


export const SetStoriesAction = (stories) => ({type: SET_STORIES, stories})
export const SetWordsAction = (words) => ({type: SET_WORDS, words})
export const SetStoryAction = (storybyid) => ({type: SET_STORY, storybyid})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_STORY, currentPage}) 
export const setTotalStoriesCount = (totalStoriesCount) => ({type: SET_TOTAL_STORIES_COUNT, totalStoriesCount})
export const setLoadingStories = (loading) => ({type:SET_LOADING_STORIES, loading})





export const requestStories =  (dispatch, page, pageSize) => {  
        dispatch(setLoadingStories(true))
        dispatch(setCurrentPageAction(page))

         storyAPI.getStories(page, pageSize).then(res => {
             dispatch(setLoadingStories(false))
             dispatch(SetStoriesAction(res.current_page));    
             dispatch(setTotalStoriesCount(res.stories_count)); 
             
        });

        
        // console.log("reducer: " + data)
    
        // dispatch(SetStoriesAction(data.storiesdb));    
        // dispatch(setTotalStoriesCount(data.totalCount)); 
}

export const requestWords = async (dispatch) => {      

    const data = await wordsAPI.getWords();
    
    console.log(data);
    dispatch(SetWordsAction(data));    
}

export const requestStoryById = async(dispatch, id) => {
    const data = await storyAPI.getStoryById(id);

    dispatch(SetStoryAction(data))


}

export default storyReducer