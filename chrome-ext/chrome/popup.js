
function init() {
  chrome.tabs.executeScript(null, {file:"analyse.js"});
}

document.addEventListener('DOMContentLoaded', init);
