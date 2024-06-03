import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
    "graphApi": "https://mic4j0f67e.execute-api.us-east-1.amazonaws.com/MP3-POST-Test",
    "botName": "Shortest_Distances",
    "botAlias": "Shortest_Distances",
    "identityPoolId": "us-east-1:e3710f9a-7de0-4814-95f7-af64fb9f8bb4",
    "accountId": "705443101683",
    "submitterEmail": "jundas2@illinois.edu",
    "secret": "OhQJlYg8DVHNrEs7",
    "region": "us-east-1"
}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
