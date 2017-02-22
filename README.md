Provides a very simplistic test framework for Elasticsearch.  Feel free to customize the `services.py` file for your own tests.

#### Setup 

```
pip install -r requirements.txt
```

##### constants.py
Update this file to configure connectivity for your target instance.  Values:

```
HOSTS = [] # Array of endpoints
USERNAME = '' # String
PASSWORD = '' # String
PORT = 0 # Int
```

#### Run Test

```
nosetests --verbosity=2 es_rapid_test
```
