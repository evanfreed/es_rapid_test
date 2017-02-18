import certifi
import requests
import json

from elasticsearch import Elasticsearch

from or_es_test.constants import HOSTS, USERNAME, PASSWORD, PORT


es = Elasticsearch([HOSTS],
    http_auth=(USERNAME, PASSWORD),
    port=PORT,
    use_ssl=True,
    verify_certs=True,
    ca_certs=certifi.where(),
)


def get_host():
    try:
        es.info()
    except ExceptionType:
        self.fail("Failed to reach host!")

def create_index():
    try:
        es.indices.create(index='startrek')
        es.indices.create(index='marvel')
        es.indices.create(index='dc')
    except ExceptionType:
        self.fail("Failed during index creation.")

def delete_index():
    try:
        es.indices.delete(index='startrek')
        es.indices.delete(index='marvel')
        es.indices.delete(index='dc')
        es.indices.delete(index='starwars')
    except ExceptionType:
        self.fail("Failed during removal of indexes.")

def insert_data():
    try:
        count = 1
        while count <= 250:
            r = requests.get('http://swapi.co/api/people/'+ str(count))
            es.index(index='starwars', doc_type='people', id=count, body=json.loads(r.content))
            count=count+1
    except ExceptionType:
        self.fail("Failed during indexing of data.")
