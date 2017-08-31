import os
import json

def retrieve_input(filename):
  with open(filename, "r") as f:
    return json.load(f)

def produce_output(filename):
  with open(filename, "w") as f:
    return json.dump(content, filename, indent=2)

#def convert_data_row(row):
#  print(row)
#  return row

def convert_field(value):
  if value.startswith("@"):
    return value
  else:
    return f"message.{value}"

def convert_metrics(metric):
  metric["field"] = convert_field(metric["field"])
  metric.pop("inlineScript", None)
  metric.pop("settings", None)
  return metric

def convert_target(target):
  target["metrics"] = list(map(convert_metrics, target["metrics"]))
  return target

def convert_panel(panel):
  panel["targets"] = list(map(convert_target, panel["targets"]))
  panel["datasource"] = "tmh_controller_metric"
  return panel

def convert_row(row):
  row["panels"] = list(map(convert_panel, row["panels"]))
  return row

def convert_templating(templating):
  #templating["list"] = 
  return templating

def convert(data):
  data["rows"] = list(map(convert_row, data["rows"]))
  data["templating"] = convert_templating(data["templating"])
  return data

def replace_templating(data):
  reference = retrieve_input(f"/tmp/templating.json")
  a = data["templating"]
  b = reference["templating"]
  data["templating"] = reference["templating"]
  return data
# targets[metrics.field] currentSOC -> message.currentSOC
# metrics
for filename in os.listdir("/tmp/in"):
  with open(f"/tmp/out/{filename}", "w") as destination:
    print(f"Generation: /tmp/out/{filename}")
    data = replace_templating(convert(retrieve_input(f"/tmp/in/{filename}")))
    json.dump(data, destination, indent=2)
