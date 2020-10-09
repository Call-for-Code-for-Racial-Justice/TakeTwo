![](images/logoblack.png)

## Emb(race): Diverse Representation

Technology has the power to drive action. And right now, a call to action is needed to eradicate racism. **Black lives matter.**

We recognize technology alone cannot fix hundreds of years of racial injustice and inequality, but when we put it in the hands of the Black community and their supporters, technology can begin to bridge a gap. To start a dialogue. To identify areas where technology can help pave a road to progress.

This is one of three open source projects underway as part of the [Call for Code Emb(race) Spot Challenge](https://github.com/topics/embrace-call-for-code) led by contributors from IBM and Red Hat.


</br>

### Problem Statement

*Bias is learned and perpetuated in different ways (e.g. societal beliefs, misrepresentation, ignorance) that consequently create inequitable outcomes across all spheres of life.*

This repo is part of the [Embrace: Diverse Representation](https://github.com/Call-for-Code/Embrace-Diverse-Representation) stream and our focus is on problem statement 3. We decided to focus on the following two predefined hills:

1. A media content editor (e.g., audio, gaming, movies, tv, comics, news, publications) can incorporate bias detection and remediation into their creative process to reduce racial bias and improve representation to Gen Z.

2. A social media user can understand the historical and societal context of racial bias and cultural appropriation reflected in their posts in real time.

We have identified the following issues currently faced by **content platforms**:

- Racially biased content created due to lack of context and information.
- The possibility to perpetuate bias through content.
- Offensive and hurtful language that can cause others pain. 

This project aims to facilitate **content platforms** to:

- Flag words and phrases that may contain racial bias.
- Categorize the type of racial bias that may be present.
- Amend text to reduce the possibility of posting offensive content.
- Become more aware and improve representation in their future content.
- Become a more inclusive platform.


</br>

## Description of the TakeTwo Project

The TakeTwo solution provides a quick and simple tool for **content platforms** to detect and eliminate racial bias (both overt and subtle) from their content. 

This solution is underpinned by a crowd-sourced database of words and phrases that are deemed racially biased. These phrases are categorized in order to train an AI model on the significance of the context in which the language was used. Contributors to the project can be part of the crowdsourcing process by installing a browser extension. This data science repo contains the ML workflow to build the API that handles requests from content creation platforms. 

There are a number of other repositories related to this project:

- [TakeTwo API](https://github.com/embrace-call-for-code/taketwo-api)Contains the API code that sends crowdsource data to the backend db and is used by the data science code.
- [TakeTwo Marker Chrome Extenstion](https://github.com/embrace-call-for-code/taketwo-marker-chromeextension) - Code for the Chrome extension used to crowdsource data for training the ML model. 

</br>

### TakeTwo Architecture

This ML workstream (highlighted in the following diagram) is part of the Call For Code TakeTwo Project. It uses data crowdsourced by a [Chrome extension](https://github.com/embrace-call-for-code/taketwo-marker-chromeextension) and [sent](https://github.com/embrace-call-for-code/taketwo-api) to a backend database.

![](images/architecture-ds.png)

</br>

## Technology Used

The machine learning model code is written in Python and runs in a Jupyter notebook. 

</br>

### Description of TakeTwo Data Science 

This repo contains the code for building a machine learning model to predict whether a word or phrase contains racial bias and, if so, will also predict the category of racial bias. 

### Data

The model uses data from a backend database, populated by crowdsourcing. 

There is also some initial data which was loaded into the backend database. This is composed of racial slurs. These are from the following data sources:

- IBM defined racial slurs

- https://en.wikipedia.org/wiki/List_of_ethnic_slurs

The fields used by the model are:

- ``"flagged_string"``: *The word of phrase that has been crowdsourced.*
- ``"category"``: *The category that has been selected for the type of racial bias present in the highlighted word or phrase.*
- ``"url"``: *The url from where the word or phrase was highlighted.*


## Data Science Evolution 
The vision is that it is to contain an evolving set of versions, with various degrees of sophistication, for the DS/ML component of the solution. Currently, we have started completed DS-MVP-0 and have started to work on DS-MVP-1.

![](images/datascience-prog.png)


The overall goal of the DS/ML component is to use machine learning on text data to provide capability to detect racially biased expressions and usage in context.

It will use as input labeled data collected through crowd sourcing enabled by the MVP1 browser extension ("Marker") and train an ML model to classify text, which is to be used by the MVP2 plug-in to a content editor ("Flagger") to flag racial biased (portions of) text input to the editor. 

Below are a possible series of capabilities (refered to herein as DS-MVP's) that may be developed and included in this component:

- **DS-MVP-0** (this module does not involve "data science/machine learning" models, and may be placed in a different repo - e.g. taketwo-webapi). A module that can detect racially biased terms based on a dictionary look-up, where the look up may be done via calls to a database table containing pre-identified set of racially biased terms. 
 
- **DS-MVP-1** A machine learning module that can learn to detect racially biased terms and expressions based on input labeled data. Here the labeled data consist of <expression, classification> pairs.
 
- **DS-MVP-2** (to be documented) An extended machine learning module that can learn to detect racially biased expressions in context based on input labeled data. Here the labeled data consist of <context, expression, classification> triples.
 
- **DS-MVP-3** (to be documented) An extended machine learning modele that can learn to detect racially biased expressions in context based on input lableled data, without having to specify the "expression" and "context" separtely in the input text. Here the labeled data consist of <text, classification> pairs, and the trained model is to output <expression(s), classification> on a new test text, where expression(s) are sub-expression(s) of the input text that are identified to be biased expressions in context of the rest of the text. 
 
- **DS-MVP-4** (to be documented) An advanced machine learning module that can learn to detect racially biased expressions and to assess the credibility of each marker based on input labeled data, and make use of the estimated credibility in computing the judgement for any given input text. Here the labeled data consist of <expression, classification, marker-ID> triples.
 
- **DS-MVP-5** (to be documented) An advanced on-line active learning module that can learn to detect racially biased expressions and to actively solicit labeled data from selected markers (based on the estimated credibility of the markers). Here the labeled data consist of <expression, classification, marker-ID> triples.

## Contributing 

We welcome contributions! For details on how to contributing please read the CONTRIBUTING.md file in this repo.

This project is still very much a work in progress, however our hope for the future is that this is a step towards a more informed media culture that is more aware of racial bias in media content. We hope this can be built out so that it can be used in a range of areas; news, social media, forums, code etc.

We also hope to expand the project to enable detection of racial bias in audio and video in the future.

We hope you will help us in this open source community effort!

## Authors

- User Researcher: Anna Rodriguez
- Designers: Naagma Timakondu, Sbusiso Mkhombe
- Tester: Merlina Escorcia
- Generalist: Ashley West, Jashu Gorsia, Yolanda Rabun
- Data Scientists: Naoki Abe, Alayt Issak
- Lead Developer: Johanna Saladas
- Architect: Steve Uniack
- Offering Manager: Iain  McCombe
