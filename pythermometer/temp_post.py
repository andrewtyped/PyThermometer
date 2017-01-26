import requests
import json
from pprint import pprint

url = 'http://localhost:55878/DataSource/SaveRecord'

Properties = {
    "label": "foo",
    "data": "baz"
}

data = {
    "DataSourceId": "temperature_tracker",
    "DataSourceVisualizationId": "1",
    "Properties": Properties
}

headers = {'Content-Type':'application/json; charset=utf-8'}

json_obj = json.dumps(data, sort_keys=False, indent=2)
print(json_obj)
r = requests.post(url,headers = headers, data=json_obj)

foo = r.content
pprint(r)
