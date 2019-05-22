import json as j
import requests

with open ('/Users/jacksonoppenheim/Documents/MTGRNN/RNA/RNA2.json', 'r') as f:
    RNA_dict = j.loads(f.read())

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

names = extract_values('RNA2.json', 'name')

endpoint = '/Users/jacksonoppenheim/Documents/MTGRNN/RNA/RNA2.json'

r = requests.get(endpoint)
card_values = extract_values(r.json(), 'name')

print(card_values)
