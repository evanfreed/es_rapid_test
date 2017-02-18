import time

from nose.tools import assert_is_not_none, with_setup

from or_es_test.services import get_host, create_index, delete_index, insert_data


def setup():
    pass

def teardown():
    time.sleep(1)  # sleep time in seconds

#@with_setup(setup, teardown)
def test_get_host():
    # Send a request to the API server and store the response.
    response = get_host()

def test_create_index():
    reponse = create_index()

def test_insert_data():
    response = insert_data()

def test_delete_index():
    reponse = delete_index()
