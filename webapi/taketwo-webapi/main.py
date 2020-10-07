import os

import json

from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

from fastapi.responses import HTMLResponse

# from fastapi.middleware.cors import CORSMiddleware

from cloudant.client import Cloudant

app = FastAPI()

clear_token = os.getenv("CLEAR_TOKEN")
db_name = os.getenv("DBNAME")
client = None
db = None
creds = None

if "VCAP_SERVICES" in os.environ:
    creds = json.loads(os.getenv("VCAP_SERVICES"))
    print("Found VCAP_SERVICES")
elif os.path.isfile("vcap-local.json"):
    with open("vcap-local.json") as f:
        creds = json.load(f)
        print("Found local VCAP_SERVICES")

if creds:
    username = creds["username"]
    apikey = creds["apikey"]
    url = creds["url"]
    client = Cloudant.iam(username, apikey, url=url, connect=True)
    db = client.create_database(db_name, throw_on_exists=False)

if db is None:
    import couchdb
    client = couchdb.Server('http://admin:password@localhost:5984/')
    try: 
        db = client.create(db_name)
    except couchdb.PreconditionFailed:
        db = client[db_name]


class Flagged(BaseModel):
    _id: Optional[str]
    user_id: str
    flagged_string: str
    category: str
    info: Optional[str]
    url: str


class Text(BaseModel):
    content: str


@app.get("/", response_class=HTMLResponse)
def read_root():
    return open("template.html").read()


@app.get("/mark")
def get_marks():
    return list(map(lambda doc: doc, db))


@app.post("/mark")
def save_mark(item: Flagged):
    data = item.dict()
    if client:
        my_document = db.create_document(data)
        data["_id"] = my_document["_id"]
        return data
    else:
        print("No database")
        return data


@app.put("/mark/{_id}")
def update_mark(_id: str, item: Flagged):
    my_document = db[_id]
    my_document["category"] = item.category
    my_document.save()
    return {"status": "success"}


@app.delete("/mark")
def delete_mark(_id: str):
    my_document = db[_id]
    my_document.delete()
    return {"status": "success"}

if os.path.isfile("vcap-local.json"):
    @app.put("/clear_all")
    def clear_all(confirm: str):
        if confirm == clear_token:
            for doc in db:
                doc.delete()
            return {"status": "success"}
        return {"status": "failed"}


@app.get("/categories")
def read_categories():
    # fmt: off
    return [
        #IBM colour-blindness palette used below https://davidmathlogic.com/colorblind/ 
        {
            "name": "appropriation", 
            "colour": "#648FFF", 
            "description": "To adopt or claim elements of one or more cultures to which you do not belong, consequently causing offence to members of said culture(s) or otherwise achieving some sort of personal gain at the expense of other members of the culture(s)."
        },
        {
            "name": "stereotyping",
            "colour": "#785EF0",
            "description": "To perpetuate a system of beliefs about superficial characteristics of members of a given ethnic group or nationality, their status, society and cultural norms.",
        },
        {
            "name": "under-representation",
            "colour": "#DC267F",
            "description": "To have Insufficient or disproportionately low representation of Black, Indigenous, People of Color (BIPOC) individuals, for example in mediums such as media and TV adverts.",
        },
        {
            "name": "gaslighting", 
            "colour": "#FE6100", 
            "description": "To use tactics, whether by a person or entity, in order to gain more power by making a victim question their reality.  To deny or refuse to see racial bias, which may also include the act of convincing a person that an event/slur/idea is not racist or not as bad as one claims it to be through means of psychological manipulation."
        },
        {
            "name": "racial slur",
            "colour": "#FFB000",
            "description": "To insult, or use offensive or hurtful language designed to degrade a person because of their race or culture. This is intentional use of words or phrases to speak of or to members of ethnical groups in a derogatory manor. ",
        },
        {
            "name": "othering", 
            "colour": "#5DDB2B", 
            "description": "To label and define a person/group as someone who belongs to a 'socially subordinate' category of society. The practice of othering persons means to use the characteristics of a person's race to exclude and displace such person from the 'superior' social group and separate them from what is classed as normal."
        },
    ]
    # fmt: on


@app.put("/analyse")
def analyse_text(text: Text):
    res = []
    for doc in db:
        if doc["flagged_string"] in text.content:
            res.append({"flag" : doc["flagged_string"], "category" : doc["category"], "info" : doc["info"]})
    return {"biased": res}


# @app.post("/texts")
# def post_texts():

# @app.get("/texts")
# def get_texts():
