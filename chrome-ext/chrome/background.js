
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
    chrome.extension.getBackgroundPage().console.log(request.text);
    var popups = chrome.extension.getViews({type: "popup"});
    if (popups.length != 0) {
      var popup = popups[0];
      var content = popup.document.getElementById("content");
      if (content) {
        content.innerHTML=request.text;
      } else {
        console.log("No content DIV");
      } 
    }
  }
);

chrome.tabs.onUpdated.addListener(
function(tabId, changeInfo, tab) {
  if (tab.url.indexOf('.ee') > -1) {
    chrome.pageAction.show(tabId);
  }  
}
);

