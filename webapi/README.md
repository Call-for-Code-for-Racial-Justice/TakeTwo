# TakeTwo Solution Starter - WebAPI Backend

The TakeTwo Web API can be used while you compose social media text, paragraphs, essays and papers. TakeTwo will scan for potentially racially biased language. The API is built using Python, [FastAPI](https://fastapi.tiangolo.com/), and [Docker](https://www.docker.com) (if running on a Kubernetes cluster).

The racially biased terms are vetted and loaded into a backend database. The code is set up to run the API locally with a [CouchDB](https://couchdb.apache.org/) backend database or [IBM Cloudant](https://www.ibm.com/uk-en/cloud/cloudant) database.

To run with CouchDB, you will need to deploy a CouchDB docker image either locally or on a Kubernetes cluster.

There is a front-end HTML page that serves as an example text editor.

## Diagrams

### TakeTwo Architecture

This API (highlighted in the following diagram) is part of the Call for Code for Racial Justice TakeTwo Project. This API is used to capture the data highlighted by users through the TakeTwo Chrome extension tool.

![](/images/architecture-highlighted.png)

</br>

### Description of TakeTwo API

This API is part of the Call for Code for Racial Justice TakeTwo project. This API is used to capture the data crowdsourced by our contributors through the [TakeTwo Chrome extension tool](/chromeextension/README.md).

The API is used to fetch the defined categories of racial bias and serve them in the extension tool. It also captures the data highlighted by contributors and posts it to a backend database. This data is used to train an [ML model](/datascience/README.md) that can detect racial bias.

## Datasets

The database contains the following fields:

- ``"_id"``: *Database field* (optional)
- ``"_rev"``: *Database field*
- ``"user_id"``: *The user ID*
- ``"flagged_string"``: *The word or phrase that has been highlighted by the user.*
- ``"category"``: *The category that has been selected for the type of racial bias present in the highlighted word or phrase.*
- ``"info"``: *Additional information; context description provided by the user.* (optional)
- ``"url"``: *The url from where the word or phrase was highlighted.*


</br>

This project has defined a number of categories of racial bias, which are used by a text classification model (outlined below). We welcome feedback on these:

- Appropriation
- Stereotyping
- Under-Representation
- Gaslighting
- Racial Slur
- Othering

Definitions of these categories can be found on the TakeTwo [webpage](/README.md).

</br>

## Learning objectives

In this tutorial, you will learn how to:
- Clone the TakeTwo repository.
- Install the Python prerequisites.
- Start a CouchDB container.
- Launch the application.
- Deploy to Kubernetes.
- Use the API.

## Prerequisites

To complete the steps in this tutorial you need:
- Install Python3
- Install Docker

## Estimated time

Completing this tutorial should take about 15 minutes.

## Getting started

#### Clone the TakeTwo repository

To run this API locally you will need to clone this repo:

```git clone https://github.com/embrace-call-for-code/taketwo.git```

#### Install the Python prerequisites

Navigate into the repo:

```cd taketwo-webapi```

Run the following command to create a virtual environment:

```python3 -m venv env```

Activate virtual environment:

```source env/bin/activate```

Install the packages needed from the requirements.txt file:

```pip install -r requirements.txt```

Navigate to the folder which contains the API code:

```cd taketwo-webapi```

#### Start a CouchDB container

Before launching the application, set the name of your CouchDB database:

```export DBNAME=taketwodatabase```

To run the API with a CouchDB backend, start a couchDB container before running the main.py code:

```docker run -p 5984:5984 -d -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password couchdb```

#### Launch the application

Run the Python api code:

```uvicorn main:app --reload```

</br>

## Deploy to Kubernetes

There is already an [image](https://hub.docker.com/repository/docker/josiemundi/taketwo_v0.1) available in Docker Hub for this API, which you can use to deploy to a Kubernetes cluster. Alternatively, you can build your own using the Dockerfile in this repo.

To build a new image, run the following command in a terminal window:

```docker build -t <dockerusername>/taketwo_api .```

To push the image to Docker Hub, run the following:

```docker login```
```docker push <dockerusername>/taketwo_api```

</br>

## Use the API

When the API is running, the main url will show an example text editor which can be used to make requests to the backend data. You can type in the text box and then press check. Text that could be racially biased will be highlighted as shown in the following example.

Open a browser to [http://localhost:8000](http://localhost:8000)

</br>

![](images/api-example.png)

## Review the TakeTwo OpenAPI documentation

For an overview of the available endpoints, navigate to [http://localhost:8000/docs](http://localhost:8000/docs)

![TakeTwo Swagger Doc](images/api-swaggerdoc.png)

## Summary

Once the TakeTwo database and Python service is running, the TakeTwo endpoints can be called to get, save, delete, update data in the database. New text can be analyzed for potentially racially biased terminology.

## Related Links

There are a number of other components related to this project:

- [TakeTwo Data Science](/datascience/README.md) - Contains data science work for building and training the model.
- [TakeTwo Marker Chrome Extenstion](/chromeextension/README.md) - Code for the Chrome extension used to crowdsource data for training the ML model.
