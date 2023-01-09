
let xhr = new XMLHttpRequest()
const url=" http://127.0.0.1:5000"
const positive=0x1F60A
const sad=0x1F641
const neutral=0x1F610

let postObj={
    tweet_text:""
}

var requestBody=[]


// data-testid="tweetText"

function addSentimentEmoji(sentimentScore,tweet){
    var time=tweet.getElementsByTagName("time")[0]
    var p=document.createElement("p")
    p.innerHTML="Detected Mood:"
    if(sentimentScore[0].detected_mood==="NEUTRAL"){
        p.innerHTML=p.innerHTML+String.fromCodePoint(neutral)
    }
    else if(sentimentScore[0].detected_mood==="POSITIVE")
    {
        p.innerHTML=p.innerHTML+String.fromCodePoint(positive)
    }
    else{
        p.innerHTML=p.innerHTML+String.fromCodePoint(sad)
    }
    // time.parentNode.appendChild(p)
    time.innerHTML=time.innerHTML+" "+p.innerHTML

}

function getSentiment(tweetText,tweet){
    postObj.tweet_text=tweetText
    requestBody.push(postObj)
    let post = JSON.stringify(requestBody)
    console.log(post)
    sentimentApi=url+"/"+"api/sentiment-score"
    xhr.open('POST', sentimentApi, true)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.setRequestHeader('Access-Control-Allow-Origin','*')
    xhr.send(post);
    xhr.onload = function () {
    if(xhr.status === 200) {
        console.log("Post successfully created!") 
        console.log("response message"+xhr.response)
        response=JSON.parse(xhr.response);
        console.log(response)
        addSentimentEmoji(response,tweet)
    }
}
}

function isEnglish(tweetText,nodeContext){
    postObj.tweet_text=tweetText
    requestBody.push(postObj)
    let post = JSON.stringify(requestBody)
    console.log(post)
    isEnglishApi=url+"/"+"/api/language-detection"
    xhr.open('POST', isEnglishApi, true)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.setRequestHeader('Access-Control-Allow-Origin','*')
    xhr.send(post);
    xhr.onload = function () {
    if(xhr.status === 200) {
        console.log("Post successfully created!") 
        console.log("response message"+xhr.response)
        response=JSON.parse(xhr.response);
        console.log(response[0].is_english)
        if(response[0].is_english){
            getSentiment(tweetText,nodeContext)
        }
    }
}
}

function getTweet(){
// var a=document.querySelectorAll('[data-testId=tweetText]');
var tweets= document.querySelectorAll('[data-testid=tweet]');

//picking only timeline tweets
tweetText=tweets[1].querySelector('[data-testId=tweetText]').getElementsByTagName("span")[0]
var tweetText=tweetText.innerText
console.log(tweetText)
isEnglish(tweetText,tweets[1])

}


setTimeout(getTweet,5000)
