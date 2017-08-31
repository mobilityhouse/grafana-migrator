import os
import http.client, csv , json, re, yaml

def retrieve_secret():
  with open("/tmp/secret", "r") as f:
    return f.read()

def retrieve_config():
  with open("/tmp/setup.yaml", "r") as f:
    return yaml.load(f)

config = retrieve_config()
secret = config["secret"] # retrieve_secret()

print(f"things could be easier {secret}")
print(config)

conn = http.client.HTTPConnection(
    host = config["host"], port = config["port"]
    )

auth_headers = { "Authorization": f"Bearer {secret}" }
print(auth_headers)

for filename in os.listdir("/tmp/out"):
  with open(f"/tmp/out/{filename}", "r") as source:
    config = json.load(source)
    title = "AUTO " + config["title"]
    config.pop("id", None) # remove the id just to be safe
    data = { "dashboard": config, "overwrite": True }
    payload = json.dumps(data)
    print(f"Updating: {title}")
#    conn.request("POST", "/api/dashboards/db", headers = auth_headers, body = payload)
#    #print(json.dumps(data, indent=2))
#    res = conn.getresponse()
#    print(f"status: {res.status}, reason: {res.reason}, data {res.read()}")
