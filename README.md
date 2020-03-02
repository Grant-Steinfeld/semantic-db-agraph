#  Learn and Explore Semantic data using Franz AllegroGraph DB

## Try out a SPARQL query in your browser right now:
### DBPedia - discover movies where actress `Shailene Woodley` starred.
Click on this link, then click on the execute query button:

https://bit.ly/39eQd1q





## AllegroGraph
### Lab Notes
### 1. Run Python3 queries to targeted RedHat Linux AGraph server

```sh
python3 Query.py
```

Lets explore how we can link UNESCO heritage sites with Geographic / Regional data in service of potential destination travel
options targeted for enthusiasts who want a vacation itenerary that highlights Ancient and Modern wonders of the world!


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


#### Resources
http://live.dbpedia.org/ontology/WorldHeritageSite

Franz AllegroGraph
https://franz.com/


Evans, Colin. Programming the Semantic Web: Build Flexible Applications with Graph Data by Toby Seg. O'Reilly Media. 


### Dataset Sources: RDF / triple / linked data

[DBPedia datasets](https://wiki.dbpedia.org/develop/datasets)

https://www.w3.org/wiki/DataSetRDFDumps

https://query.wikidata.org/

[N-TRIPLES spec](http://www.w3.org/TR/rdf-testcases/#ntriples)

[Entities Wikimedia](https://dumps.wikimedia.org/wikidatawiki/entities/)

### Query options
#### SPARQL
Comunica: a Modular SPARQL Query Engine for the Web
https://comunica.github.io/Article-ISWC2018-Resource/

#### query by S P O
http://fragments.dbpedia.org/2016-04/en?subject=http%3A%2F%2Fdbpedia.org%2Fontology%2FWorldHeritageSite&predicate=&object=



### IBM Watson and Linked Data
http://iswc2011.semanticweb.org/tutorials/semantic-web-technology-in-watson/index.html


### Other links
https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual







