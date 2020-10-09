"use strict";

var API_URL = "http://localhost:8000";
var USER_ID = "tester"


// Add option when right-clicking
chrome.contextMenus.create({ title: "Highlight", onclick: highlightTextFromContext, contexts: ["selection"] });
// chrome.contextMenus.create({ title: "Toggle Cursor", onclick: toggleHighlighterCursorFromContext });
// chrome.contextMenus.create({ title: "Highlighter color", id: "highlight-colors" });
// chrome.contextMenus.create({ title: "Yellow", id: "yellow", parentId: "highlight-colors", type: "radio", onclick: changeColorFromContext });
// chrome.contextMenus.create({ title: "Cyan", id: "cyan", parentId: "highlight-colors", type: "radio", onclick: changeColorFromContext });
// chrome.contextMenus.create({ title: "Lime", id: "lime", parentId: "highlight-colors", type: "radio", onclick: changeColorFromContext });
// chrome.contextMenus.create({ title: "Magenta", id: "magenta", parentId: "highlight-colors", type: "radio", onclick: changeColorFromContext });

// Get the initial color value
// chrome.storage.sync.get('color', (values) => {
//     var color = values.color ? values.color : "yellow";
//     chrome.contextMenus.update(color, { checked: true });
// });

// Add Keyboard shortcut
chrome.commands.onCommand.addListener(function (command) {
    if (command === "execute-highlight") {
        trackEvent('highlight-source', 'keyboard-shortcut');
        highlightText();
    }
});

// Listen to messages from content scripts
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action && request.action == 'highlight') {
        trackEvent('highlight-source', 'highlighter-cursor');
        highlightText();
    } else if (request.action && request.action == 'track-event') {
        if (request.trackCategory && request.trackAction) {
            trackEvent(request.trackCategory, request.trackAction)
        }
    }
    if (request.action == "getCategories") {

        axios.get(API_URL + '/categories')
            .then(function (response) {
                // handle success
                // console.log(response);
                sendResponse(response)
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
        return true;
    }
    if (request.action == "saveToServer") {
        axios.post(API_URL + '/mark', {
            user_id: USER_ID,
            flagged_string: request.string,
            category: request.category,
            url: request.url
        })
            .then(function (response) {
                // handle success
                // console.log(response);
                sendResponse(response)
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
        return true;
    }
    if (request.action == "removeFromServer") {
        axios.delete(API_URL + '/mark', {
            params: {
                _id: request._id,
            }
        })
            .then(function (response) {
                // handle success
                // console.log(response);
                sendResponse(response)
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
        return true;
    }
    if (request.action == "updateOnServer") {
        axios.put(API_URL + '/mark/'+request._id, {

                user_id: "",
                flagged_string: "",
                category: request.category,
                url: ""
        })
            .then(function (response) {
                // handle success
                // console.log(response);
                sendResponse(response)
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .then(function () {
                // always executed
            });
        return true;
    }
});

function highlightTextFromContext() {
    trackEvent('highlight-source', 'context-menu');
    highlightText();
}

function highlightText() {
    trackEvent('highlight-action', 'highlight');
    chrome.tabs.executeScript({ file: 'contentScripts/highlight.js' });
}

function toggleHighlighterCursorFromContext() {
    trackEvent('toggle-cursor-source', 'context-menu');
    toggleHighlighterCursor();
}

function toggleHighlighterCursor() {
    trackEvent('highlight-action', 'toggle-cursor');
    chrome.tabs.executeScript({ file: 'contentScripts/toggleHighlighterCursor.js' });
}

function removeHighlights() {
    trackEvent('highlight-action', 'clear-all');
    chrome.tabs.executeScript({ file: 'contentScripts/removeHighlights.js' });
}

function showHighlight(highlightId) {
    trackEvent('highlight-action', 'show-highlight');

    chrome.tabs.executeScript({
        code: `var highlightId = ${highlightId};`
    }, function () {
        chrome.tabs.executeScript({ file: 'contentScripts/showHighlight.js' });
    });
}

function changeColorFromContext(info) {
    trackEvent('color-change-source', 'context-menu');
    changeColor(info.menuItemId);
}

function changeColor(color) {
    trackEvent('color-changed-to', color);
    chrome.storage.sync.set({ color: color });

    // Also update the context menu
    chrome.contextMenus.update(color, { checked: true });
}

function trackEvent(category, action) {
    // _gaq.push(['_trackEvent', category, action]);
}


function setApiUrl(value) {
    console.log("setting api value")
    API_URL = value;
}

function getApiUrl() {
    return API_URL
}

function setUserId() {

}

function getUserId() {

}