

chrome.tabs.query({active:true,windowType:"normal", currentWindow: true},function(id){

   chrome.action.onClicked.addListener(function(activeTab) {
   
      chrome.scripting.executeScript({
         target: {tabId: id[0].id},
         files: ['./scripts/inject.js'],
     });
   
   });
})

