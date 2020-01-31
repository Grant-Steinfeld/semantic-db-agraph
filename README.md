#  Build Semantic Microservices with AllegroGraph and RedHat Kubernetes OpenShift

## run Query.py

```sh
python3 Query.py
```

take a look a the main segment here
```python

""" example calls to add continent node linked with city-country linked with UNESCO heritage site with year posted """
    addDestination(MAIN_TARGET_REPO,'North Africa','St Floris','Manovo-Gounda St Floris National Park', 1997)
    addDestination(MAIN_TARGET_REPO,'Southern Africa','Nelspruit, South Africa','Kruger National Park', 2019)
    addDestination(MAIN_TARGET_REPO,'Europe','Paris France','Eifell Tower', 2005)
    addDestination(MAIN_TARGET_REPO,'Europe','Vienna Austria','Historic Centre of Vienna', 2017)
    addDestination(MAIN_TARGET_REPO,'South America','Bolivia','City of Potosi', 2014)
    addDestination(MAIN_TARGET_REPO,'Central America','Tulum Mexico','Mayan Ruins of Tulum', 2001)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Chichen Itza', 1985)
    addDestination(MAIN_TARGET_REPO,'Central America','Cancun Mexico','Xichen', 1977)
    addDestination(MAIN_TARGET_REPO,'Central America','Lake Peten Itza Guatemala','Tikal', 1977)
```

### requirements
python3

pip3

AllegroGraph instance / [docker version](https://franz.com/agraph/docker/)


### setup Agraph Client in Python
```sh
pip3 install -r requirements.txt
```
