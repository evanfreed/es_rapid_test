import time

from nose.tools import with_setup

from es_rapid_test import services


def test_get_host():
    response = services.get_host()

def test_create_index():
    reponse = services.create_index()

def test_insert_data():
    response = services.insert_data()

def test_cluster_health():
    response = services.get_cluster_health()

def test_delete_index():
    reponse = services.delete_index()
