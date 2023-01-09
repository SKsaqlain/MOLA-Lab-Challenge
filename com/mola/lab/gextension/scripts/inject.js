
let xhr = new XMLHttpRequest()
const url="http://localhost:5000/"

let postObj={
    tweet_text:""
}


// data-testid="tweetText"

function getTweet(){

var a=document.querySelector('[data-testId=tweetText]');
console.log(a)
tweetNode=a.getElementsByTagName("span")[0]
var tweetText=tweetNode.innerText
console.log(tweetText)
isEnglish(tweetText)

}


function isEnglish(tweetText){
    postObj['tweet_text']=tweetText
    let post = JSON.stringify(postObj)
    xhr.open('POST', url, true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(post);
    xhr.onload = function () {
    if(xhr.status === 200) {
        console.log("Post successfully created!") 
        console.log("response message"+xhr.response.message)
    }
}
}
setTimeout(load,5000)




