import requests
import json
from pprint import pprint

def save_record(server_config, temperature_reading):
    properties = {
        "temperature": temperature_reading['temperature'],
        "reading_time": temperature_reading['reading_time']
    }

    data = {
        "DataSourceId": server_config['data_source_id'],
        "DataSourceVisualizationId": server_config['data_source_visualization_id'],
        "Properties": properties
    }

    headers = {'Content-Type':'application/json; charset=utf-8'}

    json_obj = json.dumps(data, sort_keys=False, indent=2)

    url = server_config['host_name'] + server_config['update_url']

    r = requests.post(url,headers = headers, data=json_obj)

    content = r.content
    pprint(content)
