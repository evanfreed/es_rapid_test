import certifi
import requests
import json
import re

from elasticsearch import Elasticsearch
from multiprocessing import Process

from es_rapid_test.constants import HOSTS, USERNAME, PASSWORD, PORT


es = Elasticsearch(HOSTS,
    http_auth=(USERNAME, PASSWORD),
    port=PORT,
    use_ssl=True,
    verify_certs=True,
    ca_certs=certifi.where(),
)


def get_host():
    try:
        es.info()
    except:
        self.fail("Failed to reach host!")

def create_index():
    try:
        es.indices.create(index='startrek')
        es.indices.create(index='marvel')
        es.indices.create(index='dc')
    except:
        self.fail("Failed during index creation.")

def delete_index():
    try:
        es.indices.delete(index='startrek')
        es.indices.delete(index='marvel')
        es.indices.delete(index='dc')
        es.indices.delete(index='starwars-people')
        es.indices.delete(index='starwars-planets')
    except:
        self.fail("Failed during removal of indexes.")

def insert_data():
    try:
        def insert_people():
            count = 1
            while count <= 150:
                r = requests.get('http://swapi.co/api/people/'+ str(count))
                es.index(index='starwars-people', doc_type='people', id=count, body=json.loads(r.content))
                count=count+1
        def insert_planets():
            count = 1
            while count <= 150:
                r = requests.get('http://swapi.co/api/planets/'+ str(count))
                es.index(index='starwars-planets', doc_type='planets', id=count, body=json.loads(r.content))
                count=count+1
        insert_people()
        insert_planets()
    except:
        self.fail("Failed during indexing of data.")

def get_cluster_health():
    try:
        health = es.cluster.health(filter_path=['status'])
        if health['status'] != 'green':
            raise ValueError('Cluster health is not green.')
    except:
        self.fail('Cluster is not green.')

