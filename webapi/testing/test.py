import requests
#example api test

import json

apiurl = 'https://localhost:8000'
def test_post_headers_body_json():
    url = apiurl + '/mark'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {'user_id': "test", 'flagged_string': "test string", 'category': "stereotyping", 'info': "none", 'url': "example.com"}
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.text)
