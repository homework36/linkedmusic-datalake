from elasticsearch import Elasticsearch
import requests
import os
import json
import pyld.jsonld

# this step assumes security feature off
es = Elasticsearch("http://localhost:9200")

current_directory = os.getcwd()
cantus_url = current_directory + '\cantusdb\jsonld\compact.jsonld'
simssa_url = current_directory + '\simssadb\jsonld\compact.jsonld'

with open(cantus_url, 'r') as json_file:
    cantus_compact = json.load(json_file)
    cantus_expand = pyld.jsonld.expand(cantus_compact) 


with open(simssa_url, 'r') as json_file:
    simssa_compact = json.load(json_file)
    simssa_expand = pyld.jsonld.expand(simssa_compact) 

# from mapping import cantus_mapping, simssa_mapping
# es.indices.create(index="cantusdb", mappings=cantus_mapping)
# es.indices.create(index="simssadb", mappings=simssa_mapping)

index_name = "cantusdb"  
json_data = cantus_expand
for ind, row in enumerate(json_data):
    response = es.index(index=index_name, document=row, id=index_name+str(ind))
    if response["result"] != "created":
        print("Failed to index the document index", ind)

index_name = "simssadb"  # Replace with your index name
json_data = simssa_expand
for ind, row in enumerate(json_data):
    response = es.index(index=index_name, document=row, id=index_name+str(ind))
    if response["result"] != "created":
        print("Failed to index the document index", ind)


es.search(index='cantusdb', query={"match_all": {}})
