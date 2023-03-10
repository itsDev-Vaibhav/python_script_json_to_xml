import json
import requests
from Converter import createXML

try:
    response = requests.get('http://localhost:8091/read_json', timeout=5)
    response.raise_for_status()
    # firstName = "John"
    # Code here will only run if the request is successful
    if response.status_code == 200:
        json_data = json.loads(response.text)
        createXML(json_data)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
