[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue.svg)](https://callforcode.org/slack) [![Hacktoberfest](https://img.shields.io/badge/Celebrate-Hacktoberfest-orange.svg)](https://call-for-code-for-racial-justice.github.io/Hacktoberfest/#/?id=main)

# TakeTwo Solution Starter

TakeTwo aims to help mitigate bias in digital content, whether it is overt or subtle, with a focus on text across news articles, headlines, web pages, blogs, and even code. The solution is designed to leverage directories of inclusive terms compiled by trusted sources like the [Inclusive Naming Initiative](https://inclusivenaming.org/), which was co-founded by the Linux Foundation and CNCF. The terminology is categorized to train an AI model to enhance its accuracy overtime. TakeTwo is built using open source technologies including Python, FastAPI and Docker. The API can be run locally with a CouchDB backend database or IBM Cloudant database.

## Contents

1. [Overview](#overview)
2. [Video](#video)
3. [The idea](#the-idea)
4. [How it works](#how-it-works)
5. [Diagrams](#diagrams)
6. [Datasets](#datasets)
7. [Technology](#technology)
8. [Getting started](#getting-started)
9. [Disclosures](#disclosures)
10. [License](#license)

![TakeTwo logo](images/logoblack.png)

## Overview

### What's the problem?

#### Emb(race): Diverse Representation

Technology has the power to drive action. And right now, a call to action is needed to eradicate racism. **Black lives matter.**

We recognize technology alone cannot fix hundreds of years of racial injustice and inequality. When we put it in the hands of the Black community and their supporters, technology can begin to bridge a gap; to start a dialogue; to identify areas where technology can help pave a road to progress.

This is one of several open source projects underway as part of the [Call for Code for Racial Justice](https://github.com/topics/embrace-call-for-code) led by contributors from IBM and Red Hat.

*Bias is learned and perpetuated in different ways (i.e., societal beliefs, misrepresentation, ignorance) that consequently create inequitable outcomes across all spheres of life.*

This repository is part of the [Embrace: Diverse Representation](https://github.com/Call-for-Code/Embrace-Diverse-Representation) stream and our focus is on problem statement 3. We decided to focus on the following two predefined hills:

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

## Video

[![Video Call for Code for Racial Justice Solution Starter: TakeTwo](https://img.youtube.com/vi/ZYaW7vxj3Ck/0.jpg)](https://www.youtube.com/watch?v=ZYaW7vxj3Ck)

## The Idea

The TakeTwo solution provides a quick and simple tool for **content platforms** to detect and eliminate racial bias (both overt and subtle) from their content.

## How it Works

### What is TakeTwo?

TakeTwo is an API that can be used while you compose social media text, paragraphs, essays, and papers. TakeTwo will scan for potentially racially biased language. The API works by flagging and classifying phrases and words that have a tendency of being perceived as racially biased within the United States. These phrases and words are then catagorized by [common types of detectable racially biased language](#datasets).

### How does TakeTwo work?

TakeTwo leverages a crowd-sourced database of words and phrases that could be viewed as racially biased in the US. Verified, trusted contributors can use TakeTwo's browser extension to select potentially biased language in text-based media. These selections are classified under commonly detected types of racially biased language to train TakeTwo's text-classification machine learning model.

TakeTwo's machine learning model is used to help identify subtle, context-dependent phrases or words that may be perceived as racially biased in the United States.

Users of the API and browser extension can provide feedback on the value of the recommendations provided so that the AI model can be steadily improved and refined over-time.

This API is underpinned by a crowd-sourced database of words and phrases that are deemed racially biased. These phrases are categorized in order to train an AI model on the significance of the context in which the language was used. Contributors to the project can be part of the crowdsourcing process by installing a browser extension. This API repo is part of the data capture process, which is used for modeling.

There are a number of other repositories related to this project:

- [TakeTwo Web API](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-webapi/) - Contains the Python app, FastAPI and database schema.
- [TakeTwo Data Science](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-datascience/) - Contains data science work for building and training the model.
- [TakeTwo Marker Chrome Extenstion](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-marker-chromeextension/) - Code for the Chrome extension used to crowdsource data for training the ML model.

## Technology

TakeTwo is built using open source technologies. The API is built using Python, [FastAPI](https://fastapi.tiangolo.com/), and [Docker](https://www.docker.com) (if running on a Kubernetes cluster).

The racially biased terms are vetted and loaded into a backend database. The code is set up to run the API locally with a [CouchDB](https://couchdb.apache.org/) backend database or [IBM Cloudant](https://www.ibm.com/cloud/cloudant) database.

To run with CouchDB, you will need to deploy a CouchDB docker image either locally or on a Kubernetes cluster.

There is a front-end HTML page that serves as an example text editor.

## Diagrams

### TakeTwo Architecture

![TakeTwo architecture diagram](images/taketwo-architecture.png)

1. The Chrome extension enables an authenticated user to highlight content on the fly within their browser and categorize it as racially biased.
2. An authenticated user can mark text and tag racially biased terms.
3. The information is submitted to the TakeTwo API.
4. The TakeTwo API writes data to the back-end database.
5. The machine learning model reads data from the database to train and refine the model.
6. The client app sends the content as a request to the model, and the model responds by flagging any text that could contain racially biased terms.

</br>

## Datasets

This project has defined a number of data scheme categories of racial bias, which are used by a text classification model (outlined below). We welcome feedback on these categories.

#### Common types of detectable racially biased language

- **Appropriation:** To adopt or claim elements of one or more cultures to which you do not belong, consequently causing offense to members of said culture(s) or otherwise achieving some sort of personal gain at the expense of other members of the culture(s).
- **Stereotyping:** To perpetuate a system of beliefs about superficial characteristics of members of a given ethnic group or nationality, their status, society and cultural norms.
- **Under-Representation:** To have insufficient or disproportionately low representation of Black, Indigenous, People of Color (BIPOC) individuals, for example in mediums such as media and TV adverts.
- **Gaslighting:** To use tactics, whether by a person or entity, in order to gain more power by making a victim question their reality.  To deny or refuse to see racial bias, which may also include the act of convincing a person that an event, slur, or idea is not racist or not as bad as one claims it to be through means of psychological manipulation.
- **Racial Slur:** To insult, or use offensive or hurtful language designed to degrade a person because of their race or culture. This is intentional use of words or phrases to speak of or to members of ethnic groups in a derogatory manner.
- **Othering:** To label and define a person or group as someone who belongs to a "socially subordinate" category of society. The practice of othering persons means to use the characteristics of a person's race to exclude and displace such person from the 'superior' social group and separate them from what is classed as normal.

## Getting started

#### TakeTwo Web Backend API

The Web API is built in Python and handles the following:

- Captures the data crowdsourced by contributors through the [TakeTwo Chrome extension tool](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-marker-chromeextension/blob/main/README.md).
- Captures the data highlighted by contributors and posts it to a backend database. Separately, this data will be used to train a [ML model](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-datascience/blob/main/README.md) that can detect racial bias.
- Fetches the defined categories of racial bias and serves them in the extension tool.

[Follow these instructions for setting up the web back end API](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-webapi/blob/main/README.md)

#### TakeTwo Browser Extension

The TakeTwo Chrome javascript extension uses the [Highlighter Chrome extension](https://github.com/jeromepl/highlighter) library to allow the highlighter functionality for selecting text.

The TakeTwo Chrome browser extension is a plugin to facilitate the capture and categorization words and phrases that could be racially biased through a browser. The words and phrases can be categorized.

This extension is used to enable the crowdsourcing of data for use in training an ML model. This extension aims to make it as easy as possible for community members who would like to contribute to this initiative to do so quickly and privately.

[Follow these instructions for installing the Chrome Extension](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-marker-chromeextension/blob/main/README.md)

#### TakeTwo Data Science

The TakeTwo Data Science workstream uses data crowdsourced by a [Chrome extension](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-marker-chromeextension/blob/main/README.md). The data is sent to a [backend database](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-webapi/blob/main/README.md).

The machine learning model code is written in Python and runs in a Jupyter notebook.

[Follow these instructions for building a machine learning model to predict whether a word or phrase contains racial bias.](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-datascience/blob/main/README.md)

## Steps

To build and use the TakeTwo solution:

1. Get started by cloning the [TakeTwo web API repository](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-webapi), and follow the instructions to build and run the FastAPI server.

   ![FastAPI Swagger Docs](images/fastapi-swagger-finished.jpg)

2. Next, clone the [TakeTwo Chrome extension repository](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-marker-chromeextension), and follow the instructions to build the Chrome extension.

   ![Chrome Extension](images/extension-finished.jpg)

3. Finally, explore the [TakeTwo data science workstream repository](https://github.com/Call-for-Code-for-Racial-Justice/taketwo-datascience) to learn more about the data science model.

## Contributing

We welcome contributions! For details on how to contribute, please read the [CONTRIBUTING](CONTRIBUTING.md) file in this repo.

This project is still very much a work in progress. Our hope for the future is that this is a step towards a more informed media culture that is more aware of racial bias in media content. We hope this can be built out for use in a range of areas: news, social media, forums, code, etc.

We also hope to expand the project to enable detection of racial bias in audio and video.

We hope you will help us in this open source community effort!

## Authors

- User Researcher: Anna Rodriguez
- Designers: Naagma Timakondu, Sbusiso Mkhombe
- Tester: Merlina Escorcia
- Generalist: Ashley West, Jashu Gorsia, Yolanda Rabun
- Data Scientists: Naoki Abe, Alayt Issak
- Lead Developer: Johanna Saladas
- Architect: Steve Uniack
- Offering Manager: Iain McCombe

## Disclosures

## License

This solution starter is made available under the [Apache 2 License](LICENSE).
