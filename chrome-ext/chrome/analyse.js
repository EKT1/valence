var xhr = new XMLHttpRequest();
xhr.open("POST", "http://localhost:5000/valence/color", true);
xhr.onreadystatechange = function() {
  if (xhr.readyState == 4) {
    var doc = xhr.responseXML;
    chrome.extension.sendMessage({text: xhr.responseText});
  }
}
var oData = new FormData();
var txt = window.getSelection().toString();
if (txt.length==0) {
  txt=document.documentElement.innerText;
}
oData.append("text", txt);
oData.append("dataonly", "true");
xhr.send(oData);
