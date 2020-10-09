# TakeTwo Solution Starter - Data Science

The TakeTwo Chrome browser extension is a plugin to facilitate the capture and categorization words and phrases that could be racially biased through a browser. The words and phrases can be categorized.

The TakeTwo Chrome javascript extension uses the [Highlighter chrome extension](https://github.com/jeromepl/highlighter) library as a basis in order to allow the highlighter functionality for selecting text.

This extension is used to enable the crowdsourcing of data for use in training an ML model. This extension aims to make it as easy as possible for community members who would like to contribute to this initiative to do so quickly and privately.

### TakeTwo Architecture

This Chrome extension  is part of the Call For Code TakeTwo Project. This extension is used to enable the crowdsourcing of data for use in training an ML model. This extension aims to make it as easy as possible for community members who would like to contribute to this initiative to do so quickly and privately.

![](/images/architecture-overview.png)

## Description of TakeTwo Chrome Extension

One of the issues that was identified early on in trying to build a model that can detect racial bias, was the lack of a dataset on racially biased (particularly subtle rather than overt) words and phrases.

The TakeTwo Chrome browser extension is a plugin to facilitate the capture and categorisation words and phrases that could be racially biased through a browser. The words and phrases can be categorised. The categories are defined in our [API](/webapi/README.md).

The words and phrases, along with their category, are sent to a backend database via an API. The data is used to train an ML text classification model on the significance of the context in which the language was used.

The extension intermittently serves an existing data record from the database to the user and asks them to highlight and classify any racial bias present. This can then be used to verify the merit of an existing mark. This enhances the reliability of the model.

### Data

The Chrome extension sends the following data to a backend database via an API:

- ``"flagged_string"``: *The word of phrase that has been highlighted by the user.*
- ``"category"``: *The category that has been selected for the type of racial bias present in the highlighted word or phrase.*
- ``"url"``: *The url from where the word or phrase was highlighted.*


</br>

This project has defined a number of categories of racial bias, which are used by a text classification model (outlined below), however we welcome feedback on these:

- Appropriation
- Stereotyping
- Under-Representation
- Gaslighting
- Racial Slur
- Othering

Definitions of these categories can be found on the TakeTwo [webpage](/README.md).

</br>

## Try out the extension

The following steps will explain how to get started with this extension.


### 1. Install the TakeTwo chrome extension

You will need the chrome browser, which can be installed [here](https://www.google.co.uk/chrome/?brand=CHBD&gclid=Cj0KCQjwjer4BRCZARIsABK4QeVAQkotXkLJlBvJS2V7R2q9__Gk3PchSyhorcBNAZXx7JJwbDeRrBYaAk3TEALw_wcB&gclsrc=aw.ds).


- Clone this git repo.
- In order to install the chrome plugin, navigate to `chrome://extensions` and then select the **load unpacked** option.
- Navigate to the repo folder and `select`. You will now have the browser plug-in available to you.

### 2. Highlight text

When in webpage content where you find racially biased words or phrases that are not already highlighted, highlight and categorise them as follows:

- Click on the plugin icon in the top right Chrome toolbar.
- Click on 'Toggle cursor' to enter highlight mode, your pointer will show as a highlighter pen.
![](/images/toggle-on.png)
- Highlight the word or phrase, by pressing the left mouse button, and moving along the text.
- Once highlighted a bar showing the categories will appear, select the most suitable category.
![](/images/highlight-extension.png)
- To turn off highlight mode, click on the plugin icon and 'Toggle Cursor'.
- As you highlight, your selections are saved. To delete them you can select a highlight a delete using the trashcan icon.
![](/images/delete-single.png)
- Alternatively, you can "REMOVE ALL" via the drop down. This will delete them from the backend database.
![](/images/remove-all.png)
