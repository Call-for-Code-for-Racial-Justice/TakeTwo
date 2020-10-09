# TakeTwo Solution Starter - Data Science

The Call for Code for Racial Justice TakeTwo machine learning and datascience component uses data crowdsourced by a [Chrome extension](/chromeextension/README.md) and sent to a [backend database](/webapi/README.md).

![](/images/architecture-overview.png)

## Technology Used

The machine learning model code is written in Python and runs in a Jupyter notebook.

</br>

### Description of TakeTwo Data Science

This repo contains the code for building a machine learning model to predict whether a word or phrase contains racial bias and, if so, will also predict the category of racial bias.

### Data

The model uses data from a backend database, populated by crowdsourcing.

Initially the backend database is empty and the open-source community is welcome to take on ownership and stewardship of the data.

The fields used by the model are:

- ``"flagged_string"``: *The word of phrase that has been crowdsourced.*
- ``"category"``: *The category that has been selected for the type of racial bias present in the highlighted word or phrase.*
- ``"url"``: *The url from where the word or phrase was highlighted.*


## Data Science Evolution
The vision is that it is to contain an evolving set of versions, with various degrees of sophistication, for the DS/ML component of the solution. Currently, the repository contains DS-MVP-0 and some work towards DS-MVP-1.

![](/images/datascience-prog.png)

The overall goal of the DS/ML component is to use machine learning on text data to provide capability to detect racially biased expressions and usage in context.

It will use as input labeled data collected through crowd sourcing enabled by the MVP1 browser extension ("Marker") and train an ML model to classify text, which is to be used by the MVP2 plug-in to a content editor ("Flagger") to flag racial biased (portions of) text input to the editor.

Below are a possible series of capabilities (refered to herein as DS-MVP's) that may be developed and included in this component:

- **DS-MVP-0** (this module does not involve "data science/machine learning" models, and may be placed in a different repo - e.g. taketwo-webapi). A module that can detect racially biased terms based on a dictionary look-up, where the look up may be done via calls to a database table containing pre-identified set of racially biased terms.

- **DS-MVP-1** A machine learning module that can learn to detect racially biased terms and expressions based on input labeled data. Here the labeled data consist of <expression, classification> pairs.

- **DS-MVP-2** (to be documented) An extended machine learning module that can learn to detect racially biased expressions in context based on input labeled data. Here the labeled data consist of <context, expression, classification> triples.

- **DS-MVP-3** (to be documented) An extended machine learning modele that can learn to detect racially biased expressions in context based on input lableled data, without having to specify the "expression" and "context" separtely in the input text. Here the labeled data consist of <text, classification> pairs, and the trained model is to output <expression(s), classification> on a new test text, where expression(s) are sub-expression(s) of the input text that are identified to be biased expressions in context of the rest of the text.

- **DS-MVP-4** (to be documented) An advanced machine learning module that can learn to detect racially biased expressions and to assess the credibility of each marker based on input labeled data, and make use of the estimated credibility in computing the judgement for any given input text. Here the labeled data consist of <expression, classification, marker-ID> triples.

- **DS-MVP-5** (to be documented) An advanced on-line active learning module that can learn to detect racially biased expressions and to actively solicit labeled data from selected markers (based on the estimated credibility of the markers). Here the labeled data consist of <expression, classification, marker-ID> triples.
