
let xhr = new XMLHttpRequest()
const URL="https://app-sgsb6kwvvq-uw.a.run.app/"
const POSITIVE=0x1F60A
const NEGATIVE=0x1F641
const NEUTRAL=0x1F610

let postObj={
    tweet_text:""
}


function addSentimentEmoji(sentimentScores,tweets){
    if(sentimentScores.length==0)
        return
    for(i=0;i<sentimentScores.length;i++){
        var tweet=tweets[i][0]
        var time=tweet.getElementsByTagName("time")[0]
        var p=document.createElement("p")
        p.innerHTML="Detected Mood:"
        if(sentimentScores[i].detected_mood==="NEUTRAL"){
            p.innerHTML=p.innerHTML+String.fromCodePoint(NEUTRAL)
        }
        else if(sentimentScores[i].detected_mood==="POSITIVE")
        {
            p.innerHTML=p.innerHTML+String.fromCodePoint(POSITIVE)
        }
        else{
            p.innerHTML=p.innerHTML+String.fromCodePoint(NEGATIVE)
        }
        console.log(tweets[i][1]+" "+p.innerHTML)
        
        time.innerHTML=time.innerHTML+" · "+p.innerHTML 
    }

}

function createGetSentimentRequest(tweets){
    if(tweets.length==0)
        return  []
    var requestBody=[]
    for(i=0;i<tweets.length;i++){
        postObj.tweet_text=tweets[i][1]
        requestBody.push(postObj)    
    }
    return requestBody
}


function getSentiment(tweets){
    var requestBody=createGetSentimentRequest(tweets)
    let post = JSON.stringify(requestBody)
    sentimentApi=URL+"/"+"api/sentiment-score"
    xhr.open('POST', sentimentApi, true)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.setRequestHeader('Access-Control-Allow-Origin','*')
    xhr.send(post);
    xhr.onload = function () {
    if(xhr.status === 200) {
        // console.log("Post successfully created!") 
        response=JSON.parse(xhr.response);
        addSentimentEmoji(response,tweets)
    }
}
}

function createIsEnglishRequestPayload(tweets){
    var requestBody=[]
    for(i=0;i<tweets.length;i++){
        postObj.tweet_text=tweets[i][1]
        requestBody.push(postObj)
    }
    return requestBody
}

function processIsEnglishResponse(response,tweets){
    if(response.length==0)
        return []
    var english_tweets=[]
    for(i=0;i<response.length;i++){
        if(response[i].is_english){
            english_tweets.push(tweets[i])
        }
    }
    return english_tweets
}

function isEnglish(tweets){
    var requestBody=createIsEnglishRequestPayload(tweets)
    let post = JSON.stringify(requestBody)
    console.log(post)
    isEnglishApi=URL+"/"+"/api/language-detection"
    xhr.open('POST', isEnglishApi, true)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.setRequestHeader('Access-Control-Allow-Origin','*')
    xhr.send(post);
    xhr.onload = function () {
    if(xhr.status === 200) {
        console.log("Post successfully created!") 
        response=JSON.parse(xhr.response);
        english_tweets=processIsEnglishResponse(response,tweets)
        getSentiment(english_tweets)
    }
}
}

function getTweetText(tweet){
    tweetTextNode=tweet.querySelector('[data-testId=tweetText]')
    //ignoring non tweet components
    if(tweetTextNode!=null)
        tweetText=tweetTextNode.getElementsByTagName("span")[0]
        return tweetText.innerText
    return null   
}

function processTweets(tweets){
    // will hold[ tweet_context, tweet_Text]
    processed_tweets=[]
    for(i=1;i<tweets.length;i++){
        tweet_text=getTweetText(tweets[i])
        if(tweet_text!=null)
            processed_tweets.push([tweets[i],tweet_text])
    }
    return processed_tweets
}

function getTweet(){
    // getting all timelime tweets
    var tweets= document.querySelectorAll('[data-testid=tweet]');
    tweets=processTweets(tweets)
     console.log(tweets)
    isEnglish(tweets)
}



setTimeout(getTweet,5000)
