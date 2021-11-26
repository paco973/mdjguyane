import json

with open('correspondance-code-insee-code-postal.json') as json_data:
    datas = json.load(json_data)
json_data.close()
print(len(datas))
for data in datas[:2]:
    print(data["fields"]["nom_comm"], data["fields"]["statut"])
